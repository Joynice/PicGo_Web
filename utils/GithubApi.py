# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

from github import Github
from config import config

class GithubTools(Github):
    
    def __init__(self, username=config.GITHUB_USERNAME, password=config.GITHUB_PASSWORD, repository=config.REPOSITORIES, path=config.PATH, branch=config.BRANCH):
        self.username = username
        self.password = password
        self.repository = repository
        self.path = path
        self.branch = branch
        Github.__init__(self, username, password)

    def __create_repo(self):
        try:
            repo = self.get_repo('{}/{}'.format(self.username, self.repository))
            return repo
        except:
            return '连接Github API失败，请重新测试'

    def create_file(self, filname, content):
        repo = self.__create_repo()
        if isinstance(repo, str):
            return 0, repo
        else:
            try:
                repo.create_file(path=filname, message='add {}'.format(filname), content=content, branch=self.branch) #上传路径,commit信息,上传内容,上传分支
                return 1, 'https://raw.githubusercontent.com/{}/{}/{}/{}'.format(self.username, self.repository, self.branch, filname)
            except Exception as e:
                return 0, '添加失败'

    def delete_file(self, filename):
        repo = self.__create_repo()
        if isinstance(repo, str):
            return 0, repo
        else:
            contents = repo.get_contents(filename)  #获取文件内容
            if contents:
                repo.delete_file(contents.path, "remove {}".format(filename), contents.sha, branch=self.branch)
                return 1, '删除成功'
            else:
                return 0, '删除失败'


if __name__ == '__main__':
    g = GithubTools()




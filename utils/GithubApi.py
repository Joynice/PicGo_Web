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
        repo = self.get_repo('{}/{}'.format(self.username, self.repository))
        return repo

    def create_file(self):
        repo = self.__create_repo()
        message  = repo.create_file('img/test.txt', 'test', 'test', branch=self.branch)
        print(message)

    def delete_file(self):
        repo = self.__create_repo()
        contents = repo.get_contents("img/test.txt")
        if contents:
            message = repo.delete_file(contents.path, "remove test", contents.sha, branch=self.branch)
            print(message)
        else:
            message = {'message': '没有该文件'}

if __name__ == '__main__':
    g = GithubTools()
    g.delete_file()




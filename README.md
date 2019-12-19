# PicGo_Web

## 缘由

忙里抽闲写了这个图床工具，灵感来自于[PicGo](https://github.com/Molunerfinn/PicGo),在使用过程中发现这个工具的强大
于是模仿写了个`Web`端的工具，方便自己搭建一个简易的图床。

## 应用说明

PicGo_Web目前支持

- Github
- 个人服务器

*目前支持的方式比较少，但是也是最稳定的两个图床选择*

`Github`：虽然国内访问慢，但是可以保证图片存在的永久性，插个话“Github都准备把全球开源代码保存在北极，至少保存1000年，那
岂不是子子孙孙都能找到你当前上传的图片，哈哈”。这个图床的设计主要是方便那些没有个人服务器的小伙伴们，在github创建个仓库，就可以
作为图床，保存你上传的图片。

`个人服务器`：如果你不满足于github的速度，你可以选择个人服务器，但是服务器到期的时候，图床也就失效了，个人还是觉得github还是不错的，
白嫖，嘻嘻

## 如何使用

![界面](https://raw.githubusercontent.com/Joynice/image/master/img/picweb.JPG)

本程序`Flask`框架开发，前端使用`layui`，对于没有美感的我，可以说前端设计真是对`layui`的侮辱。

**环境：python3.0+**

#### 安装步骤：

**0x01 git clone**
 ```text
git clone https://github.com/Joynice/PicGo_Web.git
```

**0x02 安装依赖**

切到项目根目录
```text
pip install -r requirements.txt
```

**0x03 数据库迁移**
切到项目根目录
```text
python manages.py db init
python manages.py db migrate
python manages.py db upgrade
```

**0x04 修改config中配置**
```python
STORE_TYPE = 'github' #存储方式（github or server）

#github 配置
GITHUB_USERNAME = 'xxx'
GITHUB_PASSWORD = 'xxx'
REPOSITORIES = 'xxx'  #需要提前创建，仓库名
BRANCH = 'master' #分支
PATH = 'xxx' # 存储路径

# server 配置
LOCAL_STORAGE_PATH = os.path.join(os.getcwd(),'static','images') #默认存储到项目static/images文件夹下
```

**0x05 运行**
```text
python run.py
```
如果有hug，请及时issues，定会及时回复

> 以上步骤可以启动程序，如果你想要高性能部署(gunicorn+nginx)，参照文章:[Gunicorn+Nginx部署Flask项目](http://lr.dropsec.xyz/2019/12/14/Gunicorn-Nginx%E9%83%A8%E7%BD%B2Flask%E9%A1%B9%E7%9B%AE/)

## 贡献

如果你觉得这个工具，还可以，不妨赏点:

![微信](https://raw.githubusercontent.com/Joynice/image/master/img/wx.JPG)
![支付宝](https://raw.githubusercontent.com/Joynice/image/master/img/zfb.JPG)
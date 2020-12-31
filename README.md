# m3u8-downloader
支持下载hls、mp4的python程序，需安装ffmpeg

#### 使用方法

##### 一、安装ffmpeg

- mac： ``brew i ffmpeg``
- linux：``yum/wget install ffmpeg``
- windows：下载安装程序即可

##### 二、安装python环境，这个不再详细说明

##### 三、安装ffmpy3、wxPython

```sh
pip install ffmpy3
pip install wxPython
```

##### 四、打包exe、mac app
1、打包windows exe可执行文件，参考链接：[https://www.cnblogs.com/caiya/p/9743272.html](https://www.cnblogs.com/caiya/p/9743272.html)

1. 先安装pyinstaller

```sh
pip install pyinstaller
```

2. 再执行打包命令

```sh
pyinstaller -F xxx.py（要打包的文件）
```

2、打包mac，使用py2app

```sh
pip install py2app
```

步骤1：

```sh
py2applet --make-setup xxx.py
```

步骤2：

打包开发模式：

```sh
python setup.py py2app -A
```

打包发布模式：

```sh
python setup.py py2app --packages=wx
```
不指定`--packages=wx`选项的话，启动的时候会报错


#### 预览效果
![image](https://imglf3.lf127.net/img/c3pZZ1VJcCsyMGdpZlJiV1lFblRVTWVDRHY0N1EybU54S1JjQ2NNS3ZkdWRVNFowM2tWQXF3PT0.png?imageView&thumbnail=1680x0&quality=96&stripmeta=0)


# 1.主要技术：Flask,requests

 requirements.txt如下
>requests>=2.10.0
Flask>=1.0.2
xmltodict>=0.12.0

# 2.实现的主要功能
- 根据自定义消息回复关键字
- 调用机器人qingyunke的api，实现自动聊天
- 上传永久素材，获取永久素材ID
- 回复关注信息
- ......![在这里插入图片描述](http://mmbiz.qpic.cn/mmbiz_png/f7PI7yfia3SeB52ACgSJtN24iccuN2hXm02f8UZrhXdA8jF2zP2hUWNwM6Lzibky9gTicERVCkbQiaDICavUttAXib5A/0)
# 3.目录说明
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190822224936896.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI2NjI0MzI5,size_16,color_FFFFFF,t_70)
- function/EventProcessing.py为事件处理，这里主要是订阅回复
- function/MessageProcessing.py为消息处理
- function/ReturnMessage.py返回消息组件
- tool/CheckResList.py根据自定义信息，返回永久素材列表，包括资源ID（单独运行的py文件）
- tool/UploadResource.py上传永久素材(单独运行的py文件)
- run.py开启服务器
- resource/KeyWord.json自定义回复关键字（格式如下）
```json
{
  "python": "链接：https://pan.baidu.com/*******",
  "工具": "none",
  "源码": "none",
  "BOTHSAVAGE":"pic_****"
}
```
- /resource/SET.json个人关键信息，包括token等（格式如下）
```json
{
  "APPID":"********",
  "APPSECRET":"******",
  "WECHAT_TOKEN" : "******",
  "MAIN" : "所有资源来自网上可获得的公共资源，仅供学习交流使用，勿做商业用途"
}
```


# 4.运行方式
>1.注册一个微笑公众号（个人），获取上述配置信息
>2.写入SET.json
>3.自定义关键字回复列表KeyWord.json
>4.运行run.py
>5.使用内网穿透把自己电脑放入外网（内网穿透教程在下面）
>6.关注自己公众号，如果配置没有出错，成功

# 5.关于作者
内网穿透教程教程:
https://www.cnblogs.com/simon-idea/p/11355704.html

本公众号开发系列博客：
https://www.cnblogs.com/simon-idea/category/1522621.html

微信公众号：

![在这里插入图片描述](http://mmbiz.qpic.cn/mmbiz_png/f7PI7yfia3SeB52ACgSJtN24iccuN2hXm0ldmHPxEDE6JcBHI2tArxuc2zib3qBrxnEmoibtbKHnsSvV64PnUXS4icA/0)



# Gif制作
可以实现制作简单的gif,可以制作动态表情包，比如增加图片的宽度，键入文字等
# 使用方法
## 安装依赖
本项目依赖Numpy和Pillow
```shell
pip install -r requirements.txt
```
## 使用
```python
from gif import Gif
g=Gif('gif.gif') #打开gif.gif,创建gif对象
g.imgs           #返回一个Image对象的列表
g.imgs[0]        #获取第一帧图片的Image对象
```
`gif.gif`文件如下
![](https://i.imgur.com/lfXPTVj.gif)
## 处理单个图片
第一帧图片
```python
img=g.imgs[0]
img.save('gif.png')
```
![](https://i.imgur.com/eVLIzyD.png)


扩展第一帧图片
第二个参数为左，右，上，下，数值为扩展的像素数,可以为1~4个，对应相应的位置；最后一个参数是RGB的值，254为白色，默认值；返回Image对象
```python
img=g.extend(img,(20,40,60,80)，254)#
img.save('1.png')
```
![](https://i.imgur.com/qToFT5V.png)

如果最后一个参数为0，将变为黑色

![](https://i.imgur.com/hS5edGw.png)


键入文字
```python
img=g.tap(img,'Hello!',local=(10,20),size=30)#第二个参数是键入的内容，第三个参数是位置，第四个参数是大小
img.save('2.png')
```
![](https://i.imgur.com/lR6rLNL.png)
# 处理多个图片
与单个图片参数相同，函数前加字母m
扩展图片
```python
imgs=g.imgs
imgs=g.mextend(g.imgs,(20,10,20))
g.save_gif(imgs,'3.gif')#保存为gif文件
```
![](https://i.imgur.com/eg6HlvD.gif)


键入文字
```python
imgs=g.mtap(imgs,'谢谢老哥',local=(10,5),size=19)
g.save_gif(imgs,'4.gif')#保存为gif文件
```
![](https://i.imgur.com/6vkG44h.gif)
# 未来的工作
功能比较简单，但也基本实现了一般的需求。
调整比较困难，gui暂不考虑。


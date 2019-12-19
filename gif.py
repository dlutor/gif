from PIL import Image, ImageSequence,ImageDraw,ImageFont
import os
import numpy as np
class Gif(object):
    def  __init__(self,filename,index=0):
        self.img=Image.open(filename)
        self.imgiter=ImageSequence.Iterator(self.img)
        self.dir='font/'
        self.check_dirs(self.dir)
        self.imgs = [frame.copy() for frame in self.imgiter]
        print(f"文件{filename} 共有{len(self.imgs)}帧")
        self.imgs[index].save(filename.split('.')[0]+'.png')
        self.array=np.array(self.imgs[index].convert('RGB'))
        print(self.array.shape)
    def save_from_aray(self,filename,array):
        im = Image.fromarray(array).convert('RGB')
        im.save(filename)
    def save_gif(self,imgs,filename,frame=100):#毫秒
        imgs[0].save(filename, save_all=True, append_images=imgs[1:],format='GIF', duration=frame, loop=0)
    def check_dirs(self, dirs):
        self.dirs = dirs
        if not os.path.exists(self.dirs):
            os.makedirs(self.dirs)
    def extend(self,img,size:tuple,color=254):#扩展左，右，上，下个像素
        array = np.array(img.convert('RGB'))
        for index,value in enumerate(size):
            if value==0:
                continue
            a=color*np.ones((value,array.shape[1],3) if index>1 else (array.shape[0],value,3),dtype="uint8")
            array=np.concatenate((array,a) if index%2 else (a,array),axis=1 if index<2 else 0)
        img=Image.fromarray(array).convert('RGB')
        return img


    def mextend(self,imgs,size:tuple,color=254):
        for i,img in enumerate(imgs):
            img=self.extend(img,size,color)
            imgs[i]=img
        return imgs
    def tap(self,img,txt='hello',local=(0,0),size=10,font='font/ZhenHunNvHai-2.ttf'):
        font=ImageFont.truetype(font,size)
        draw=ImageDraw.Draw(img)
        draw.text(local,txt,font=font,fill='black')
        return img
    def mtap(self,imgs,txt='hello',local=(0,0),size=10,font='font/ZhenHunNvHai-2.ttf'):
        for index,img in enumerate(imgs):
            imgs[index]=self.tap(img,txt,local,size,font)
        return imgs


if __name__ == '__main__':
    gif=Gif('gif.gif')
    imgs=gif.mextend(gif.imgs,(20,0,20))
    imgs=gif.mtap(imgs,'谢谢老哥',local=(10,5),size=19)
    gif.save_gif(imgs,'imgs.gif')

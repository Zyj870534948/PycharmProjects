#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"
import urllib2, json, base64, requests
from PIL import Image
import time


class ImageAdd:
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=idES72rtCxCksbAMdtXQey3k&client_secret=R3oeSWsriysUM625v15Ax8a79WY5anGe'
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)

    def __init__(self):
        content = self.response.read()
        token = json.loads(content)
        self.access_token = token['access_token']

    '''
    imageOld:输入要截取人的图片名称girl.png
    imageNew：抠图抠出的人的图片名称girl_new.png
    endIamge:最后合成图片的名称
    '''
    def fenxi(self, imageOld, imageNew,endIamge):
        self.request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg?access_token=" + self.access_token
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        with open(imageOld, 'rb') as fp:
            fp_base64 = base64.b64encode(fp.read())
            self.img_str = str(fp_base64.decode("utf-8"))
        body = {
            'image': self.img_str,
            # 'image_type': 'BASE64'
        }

        resp = requests.post(url=self.request_url, data=body, headers=self.headers)
        # self.display(resp)
        self.showImage(resp, imageNew)
        # self.display(resp)
        backgroundImage=r'.\pepper3.png'
        self.picturesAdd(backgroundImage,imageNew,endIamge)

    def display(self, resp):
        if resp:
            print(resp.content)

    def showImage(self, resp, fileName):
        res = resp.json()
        labelmap = base64.b64decode(res['foreground'])  # res为通过接口获取的返回json
        with open(fileName, 'wb') as fp:
            fp.write(labelmap)

    def picturesAdd(self, backgoundImage, personImage,endImage):
        background = Image.open(backgoundImage)
        person = Image.open(personImage)


        nfi,nfj,nei,nej = 1,1,1,1
        personn = person.convert('RGBA')
        personn = personn.load()
        pw, ph = person.size

        for i in range(pw):
            for j in range(ph):
                if personn[i,j][3] != 0:
                    nfi = i
                    break
            if personn[i, j][3] != 0:
                break

        for i in range(pw-1,-1,-1):
            for j in range(ph):
                if personn[i,j][3] != 0:
                    nei = i
                    break
            if personn[i, j][3] != 0:
                break

        for j in range(ph):
            for i in range(pw):
                if personn[i,j][3] != 0:
                    nfj = j
                    break
            if personn[i, j][3] != 0:
                break

        for j in range(ph-1,-1,-1):
            for i in range(pw):
                if personn[i,j][3] != 0:
                    nej = j
                    break
            if personn[i, j][3] != 0:
                break

        print nei,nfi,nej,nfj

        now,noh=nei-nfi+1,nej-nfj+1
        im = Image.new("RGBA", (now, noh))
        for i1 in range(now):
            for j1 in range(noh):
                im.putpixel((i1, j1), (personn[nfi, nfj][0], personn[nfi, nfj][1],personn[nfi, nfj][2],personn[nfi, nfj][3]))
                nfj+=1
            nfi+=1
            nfj -= noh


        im.save(r".\out2.png")
        im.close()
        im = Image.open(r".\out2.png")
        # 新建一个和背景一样大小的图层
        target = Image.new('RGBA', background.size, (0, 0, 0, 0))
        # 获得人图片的大小
        pw, ph = im.size
        print (pw,ph)
        # 获得背景图片的大小
        bw, bh = background.size
        print (bw, bh)
        # 获得左上角的坐标
        x = ((bw / 2) - (pw / 2)) - 1
        print(x,x + pw)
        y = bh - ph - 1
        print(y,y + ph)
        # #需要黏贴的区域
        box = (x, y, x + pw, y + ph)

        # 将背景图片黏贴在target上
        # target.paste(person,box)
        target.paste(background, (0, 0))
        target.paste(im, box, im)
        target.save(endImage)


    def imageResize1(self, file, scale):
        img = Image.open(file)
        width = 200
        height = img.size[1] * 200 / img.size[0]
        # width = int(img.size[0] * scale)
        # height = int(img.size[1] * scale)
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save('test2.png')

def computing_time(hanshu):
    start = time.clock()
    hanshu()
    end = time.clock()
    return end-start

def main_fun():
    bs = ImageAdd()
    image=r'.\image3.png'
    image_new=r'.\girl_new.png'
    outImage=r'.\out.png'
    bs.fenxi(image, image_new,outImage)


if __name__ == '__main__':
    print computing_time(main_fun)



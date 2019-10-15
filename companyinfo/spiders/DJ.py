from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import base64
from PIL import Image
from aip import AipOcr
import cv2
from io import BytesIO
class unlockScrapy(object):
    def __init__(self, driver):
        super(unlockScrapy, self).__init__()
        # selenium驱动
        self.driver = driver
        self.APP_ID = '17521401'
        self.API_KEY = 'EXRg13y9DtwheaBmlMFvymc8'
        self.SECRET_KEY = '2fPK6F9yZSqA4jG1wGmzY3kgpdQlXf2m'
        self.client = AipOcr(self.APP_ID, self.API_KEY,self.SECRET_KEY)
        print('进入百度')

    # 按顺序点击图片中的文字
    def clickWords(self, wordsPosInfo):
        print('开始点击')
        # 获取到大图的element
        # imgElement = self.driver.find_element_by_xpath(
        #     "/html/body/div[6]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]/img")
        # 根据上图文字在下图中的顺序依次点击下图中的文字
        for info in wordsPosInfo:
            self.driver.move_by_offset(info['location']['left'] + 20,info['location']['top'] + 20).click().perform()
            time.sleep(1)

    # 下载上面的小图和大图
    def downloadImg(self):
        # 全图
        time.sleep(1)
        gif = self.driver.save_screenshot(r"gif.png")
        gif_r = Image.open(r"gif.png")
        # 小图
        # with open('gif.png', 'rb') as f:
        #     return base64.b64encode(f.read())
        gif_r = Image.open(r"gif.png")
        # code = gif_r.crop(674,207,834,256)
        # # 大图
        # check =gif_r.crop(521,257,827,562)

        print(gif_r.shape) # (1080, 1920, 3)
        cropped = gif_r[674:834, 207:256]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imwrite("code.png", cropped)
        print('截图成功')
        print(gif_r.shape) # (1080, 1920, 3)
        cropped = gif_r[521:827, 257:562]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imwrite("checkCode.png", cropped)
        # 保存下载
        # fh = open("code.png", "wb")
        # fh.write(code)
        # fh.close()
        # fh = open("checkCode.png", "wb")
        # fh.write(check)
        # fh.close()
        # print('下载成功')

    # 图片二值化，便于识别其中的文字
    def chageImgLight(self):
        im = Image.open("code.png")
        im1 = im.point(lambda p: p * 4)
        im1.save("code.png")
        im = Image.open("checkCode.png")
        im1 = im.point(lambda p: p * 4)
        im1.save("checkCode.png")

    # 破解滑动
    def unlockScroll(self):
        # 滑块element
        scrollElement = self.driver.find_elements_by_class_name(
            'geetest_slider_button')
        ActionChains(self.driver).click_and_hold(
            on_element=scrollElement).perform()
        ActionChains(self.driver).move_to_element_with_offset(
            to_element=scrollElement, xoffset=30, yoffset=10).perform()
        ActionChains(self.driver).move_to_element_with_offset(
            to_element=scrollElement, xoffset=100, yoffset=20).perform()
        ActionChains(self.driver).move_to_element_with_offset(
            to_element=scrollElement, xoffset=200, yoffset=50).perform()

    # 读取图片文件
    def getFile(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 识别上面小图中的文字
    def iTow(self):
        print('识别文字')
        try:
            res=self.client.basicAccurate(self.getFile("code.png"))
            for item in res['words_result']:
                res = item
        except:
            return 'error'

    # 识别下面大图中文字的坐标
    def getPos(self, words):
        print('识别坐标')
        try:
            res = self.client.accurate(self.getFile('checkCode.png'))
            # 所有文字的位置信息
            allPosInfo = []
            # 需要的文字的位置信息
            needPosInfo = []
            for item in res['words_result']:
                allPosInfo.extend(item['chars'])
            # 筛选出需要的文字的位置信息
            for word in words:
                for item in allPosInfo:
                    if word == item['char']:
                        needPosInfo.append(item)
            return needPosInfo
        except Exception as e:
            print(e)

    def main(self):
        # 破解滑块
        # self.unlockScroll()
        # time.sleep(2)
        # 下载图片
        self.downloadImg()
        time.sleep(2)
        # 图像二值化，方便识别
        self.chageImgLight()
        print('识别图片')
        # 识别小图文字
        text = self.iTow()
        # 获取大图的文字位置信息
        posInfo = self.getPos(list(text))
        # 由于小图或大图文字识别可能不准确，因此这里设置识别出的文字少于4个则重新识别
        # while len(posInfo) != 4 or len(text) != 4:
        #     # 点击重新获取图片，再次识别
        #     self.driver.find_elements_by_xpath('/html/body/div[3]/div[4]/div/a')[0].click()
        #     time.sleep(2)
        #     self.downloadImg()
        #     time.sleep(2)
        #     text = self.iTow()
        #     posInfo = self.getPos(list(text))
        time.sleep(3)
        # 点击下面大图中的文字
        self.clickWords(posInfo)
        # 点击提交按钮
        self.driver.find_elements_by_xpath('/html/body/div[6]/div[2]/div[6]/div/div/div[3]/a/div')[0].click()
def unlock(url):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/button').click()
    unlock = unlockScrapy(driver)
    unlock.main()
    driver.close()

if __name__ == '__main__':
    unlock()
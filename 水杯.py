'''
    属性，行为：
    封装：
        1.先将属性进行隐藏
            __属性
        2.提供set/getxxx用于间接赋值和间接取值


'''
import time

class shuibei:
    __gaodu = 0
    __rongji = 0
    __yanse = ""
    __caizhi = ""


    def setgaodu(self,gaodu):
        if gaodu < 200 or gaodu > 800:
            print("水杯高度不合理！")
        else:
            self.__gaodu = gaodu

    def getgaodu(self):
        return self.__gaodu

    def setrongji(self,rongji):
        if rongji < 300 or rongji > 1000:
            print("水杯的容积不对呀！")
        else:
            self.__rongji = rongji
    def getrongji(self):
        return self.__rongji



    def setcaizhi(self,caizhi):
        if caizhi =="":
            print("输入非法！")
        else:
            self.__caizhi = caizhi

    def getcaizhi(self):
        return self.__caizhi



    def setyanse(self,yanse):
        if yanse == "":
            print("用户名非法！别瞎弄！")
        else:
            self.__yanse =  yanse

    def m(self):
        print("买了一个杯子材质是：",self.__caizhi,"，容积是：",self.__rongji,"高度是：",self.__gaodu,"  颜色是：",self.__yanse)

p = shuibei()
# p.username = "张压缩"
p.setgaodu(500)
# p.age = -25
p.setrongji(500)
# p.high = 1.87
p.setyanse  ("白色")
# p.sex = "male"
p.setcaizhi ("玻璃")

p.m()
















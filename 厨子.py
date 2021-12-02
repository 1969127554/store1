class oldcz :
    name = ""
    age = 0

    def setname(self,name):
        self.__name = name

    def getname(self):
        self.__name

    def setage(self,age):
        self.__age = age

    def getage(self):
        self.__age


    def zhengfan(self):
        print("有一个名曰",self.__name,"的老厨子,今年",self.__age,"岁")


class newcz(oldcz):
    def cc(self,ccname):
        print("老厨子的徒弟新厨子特别会做：",ccname)


    def zhengfan(self):
        super().zhengfan()

class newcz1(newcz):
    def bb(self,bbname):
        print("老厨子徒弟的徒弟，特别会做:",bbname)


    def newcz(self):
        super().cc()




p = newcz1()
p.setname("王大海")
p.setage(35)

p.zhengfan()
p.cc("鱼香肉丝")
p.bb("新疆炒米粉")





























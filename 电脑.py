class computer :
    name = ""
    pingmu = 0
    jiage = 0
    cpu = 0
    neicun = 0


    def dazhi (self,r):
        print("买了一个：",self.name,"每次能打：",r,"字")

    def dayouxi(self,gamename,time):
        print("用我的",self.name,"玩",gamename,"完了",time,"小时")

    def kanshipin(self,vido,time):
        print("用我的",self.name,"看",vido,"看了",time,"小时")


p = computer()
p.name = "华硕"
p.pingmu = 300*200
p.jiege = 365
p.cpu = 25
p.neicun = 15

p.dazhi(3)
p.dayouxi("消消乐",25)
p.kanshipin("甄嬛传",25)


















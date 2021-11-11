import random
# 准备商品
random1 = random.randint(0,10)
random2 = random.randint(0,20)
shop = [
     ["联想电脑" , 6000],
     ["sp5" , 3500],
     ["老干妈" , 7.5],
     ["iphone 18 max pro" , 15000],
     ["huawei watch" ,1200],
     ["mac pc" ,15000],
     ["辣条" ,3],
     ["机械革命" ,7500],
 ]
 # 定义一个空的购物车
mycart = []

# 定义优惠劵使用的次数
a = 0
b = 0
 #初始化自己的余额
salary = int(input("请输入您的余额："))
sal = salary

 #抽取优惠劵
print("恭喜您获得: %d 张辣条三折优惠劵，%d 张机械革命九折优惠劵" %(random1,random2))
 #  买东西
while True:
     # 展示商品架
     for key,value in enumerate(shop):
         print(key,value)

     chose = input("请输入您要买的商品编号：") # "9aa" --> 9
     if chose.isdigit():
         chose = int(chose)
         if chose >= len(shop):
             print("温馨提示：这个商品不存在！别瞎弄！")
         else:
             if salary < shop[chose][1]:
                 print("温馨提示：穷鬼，没钱，别瞎买！")

             else:
                 # 判断是否有优惠劵
                 if random1 > 0 and chose==6:
                     # 判断为输入为辣条
                    random1 -= 1
                    print("辣条优惠劵剩余 %d 张，本次可使用三折优惠劵，原价3元 折后0.9元" % random1)
                    salary -=  (shop[chose][1]*0.3)
                    mycart.append(shop[chose])
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                    a += 1
                     # 判断为输入为机械革命优惠劵
                 elif  random2 >= 1 and  chose == 7:
                     random2 -= 1
                     print("机械革命优惠劵剩余 %d 张，本次可使用九折优惠劵，原价7500元 折后6750元" % random2)
                     salary -= (shop[chose][1] * 0.9)
                     mycart.append(shop[chose])
                     print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                     b += 1


                 else:
                     salary -=  shop[chose][1]
                     mycart.append(shop[chose])
                     print(shop[chose][0],"添加购物车成功！余额还剩:￥",salary)
     elif chose == "q" or chose == "Q":
         print("欢迎下次光临！")
         break  # 跳出循环
     else:
         print("兄弟，商品不存在！别瞎弄！")

# 计算优惠金额
youhui = (3 * 0.3 * a) + (7500 * 0.9 * b)

 # 打印购物小条
print("----------------欢迎下次光临小商店-------------------")
print("以下是您的购物小条，请拿好：")
print("--------------------------------------------------")
m = []
for i in mycart:
    if i not in m:
        m.append(i)
        print(" %s x %s " % (i, mycart.count(i)))
    else:
        continue

print("--------------------------------------------------")
print("您本次消费为：%d ，剩余余额：%d" % (sal-salary , salary))
print("本次消费使用辣条优惠劵 %d张 ，使用机械革命优惠劵 %d张" %(a,b))
print("累计为您节省了：%d" % youhui)



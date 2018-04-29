age = 20

count = 0
while True:

	count += 1# 用于次数的判断
	if count <= 3:# 一个大的框架，所有的东西都在框架中(次数是循环的限制)
		gus_age = input("\n你猜猜我多大：")
		gus_age = int(gus_age)

		if gus_age > age:# 开始判断年龄
			print ("猜小点！")
		elif gus_age < age:
			print ("猜大点！")
		elif gus_age == age:# 成功猜对年龄，退出循环
			print ("小逼崽子，你猜对了！！")
			break

	elif count > 3:# 3次机会使用完，询问是否继续
		message = input("还继续猜不,y/n: ")

		if message == 'y':# 继续游戏
			count = 0
		elif message == 'n':# 退出游戏
			break
		else:
			print ("你他妈瞎几把输啥，y/n")
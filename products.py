products= []   #二維清單包含商品及價格資料(two dimensional)

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	#lists = []
	#lists.append(name)
	#lists.append(price)
	# 前三行可直接寫成 lists=[name, price]，或如下行直接將小清單加入append的內容
	products.append([name, price])
print(products)

(products[0][0], products[0][1])  #大清單中的第0個索引，小清單中的第0個索引，此語法為非清單模式(資料)

for product in products:
	print(product) #此語法為清單模式
	print(product[0], '的價格是',product[1]) #此語法為非清單模式(資料)


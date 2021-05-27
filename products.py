products= []   #二維清單包含商品及價格資料(two dimensional)

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
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

#字串可以作'相加'或'相乘'' Ex. 'abc'+'abc'='abcabc'

with open ('products.csv', 'w', encoding='utf-8') as f:   #'w'為寫入模式, encoding(編碼)設定為'utf-8'
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n') #分格&換行

data = [1, 3, 5, 7, 9] # 清單中裝著一些整數，請開始寫"寫入檔案"的程式碼
with open ('test.txt', 'w') as f:   #'w'為寫入模式
	for n in data:
		f.write(str(n) + '\n') #\n換行




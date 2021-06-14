products = []   #二維清單包含商品及價格資料(two dimensional)

#讀取檔案
# with open('products.csv', 'r', encoding='utf-8') as f:
#	for line in f:
#		s = line.strip().split(',')
#		name = s[0]
#		price = s[1]
#		print(s)

#讀取檔案 
with open ('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #若該行符合前述條件，則跳過該行但繼續執行其他行
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#請使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	#lists = [] 先建立小清單
	#lists.append(name) 小清單加入name
	#lists.append(price) 小清單加入price，方便將此小清單加入products大清單
	# 前三行可直接寫成 lists=[name, price]，或如下行直接將小清單加入append的內容
	products.append([name, price]) #將小清單list加入大清單products
print(products)

print(products[0][0], products[0][1])  #第一個[M]是大清單中的第M個索引，第二個[N]是小清單中的第N個索引，此語法為非清單模式(資料)
print(products[1][0], products[1][1])  #第一個[M]是大清單中的第M個索引，第二個[N]是小清單中的第N個索引，此語法為非清單模式(資料)

#印出所有購買紀錄
for product in products: #小清單模式
	print(product[0], '的價格是',product[1]) #此語法為非清單模式，將小清單的索引項目分開(資料)

#字串可以作'相加'或'相乘'' Ex. 'abc'+'abc'='abcabc'

#寫入檔案
with open ('products.csv', 'w', encoding='utf-8') as f:   #'w'為寫入模式, encoding(編碼)設定為'utf-8' 可以自選從檔案導入數據並選擇'utf-8'
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n') #分格&換行，csv檔用","分格

#練習題
data = [1, 3, 5, 7, 9] # 清單中裝著一些整數，請開始寫"寫入檔案"的程式碼
with open ('test.txt', 'w') as f:   #'w'為寫入模式
	for n in data:
		f.write(str(n) + '\n') #\n換行






products = []
while True: #用while通常是在不知道執行次數的條件下使用
	name = input('請輸入商品名稱： ')
	if name == 'q': #quit
		break
	price = input('請輸入價格： ')	
	price = int(price) #型別轉換成整數
	products.append([name, price])
print(products)

for p in products: 
	print(p[0], '的價格是', p[1])


with open ('products.csv', 'w', encoding='utf-8') as f: #編碼調整
	f.write('商品,價格\n') #增加欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #將price變為字串
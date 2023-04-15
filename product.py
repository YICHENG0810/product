products = []
while True: #用while通常是在不知道執行次數的條件下使用
	name = input('請輸入商品名稱： ')
	if name == 'q': #quit
		break
	price = input('請輸入價格： ')	
	products.append([name, price])
print(products)
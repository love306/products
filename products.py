products = []

while True:
	name = input('請輸入名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print('產品名稱/價格:', products)
product = []
while True:
	nam = input('請輸入名稱')
	if nam == 'q':
		break	
	pri = input('價格')
	pp = [nam, pri]
	
	product.append(pp)
print(product)
for p in product:
	print(p) 
shop = []
while True:
	na = input('名稱:')
	if na == 'q':
		break
	pr = input('價格:')
	shop.append([na, pr])

for s in shop:
	print(s[0],'價格:', s[1], '元')

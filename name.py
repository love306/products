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
for prot in products:
	print('產品名稱:', prot[0], '價格:', prot[1])
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
#print(shop[0])
#print(shop[1])

for s in shop:
	print(s[0],'價格:', s[1], '元')
with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(name[0])
#輸入檔案
while True:
	name = input('請輸入名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
#列出所有購買紀錄	
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
with open('products.csv', 'w',encoding = 'utf-8') as f:
	#f.write('名稱,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

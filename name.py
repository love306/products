import os#=載入作業系統的模組
products = []
if os.path.isfile('products.csv'):
	print('ya!i got some good!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '名稱,價格\n' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print('nothing in here!')
print(products)
#讀取檔案


#輸入檔案
while True:
	
	name = input('請輸入名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	products.append([name, str(price)])
	
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
for op in product:
	print(op) 
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
#寫入檔案
with open('products.csv', 'w',encoding = 'utf-8') as d:	
	d.write('名稱,價格\n')
	for p in products: 	
		d.write(p[0] + ',' + str(p[1]) + '\n')
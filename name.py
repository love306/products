import os#=載入作業系統的模組
#讀取檔案
def read_file(filename):
	products = []			
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格\n' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])		
	return products
#輸入檔案
def user_input(products):	
	while True:		
		name = input('請輸入名稱: ')
		if name == 'q':
			break
		price = input('請輸入價格: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products
#列出所有購買紀錄	
def print_products(products):
	for prot in products:
		print('產品名稱:', prot[0], '價格:', prot[1])
#寫入檔案
def write_file(filename, products):		
	with open(filename, 'w',encoding = 'utf-8') as d:	
		d.write('商品,價格\n')
		for p in products: 	
			d.write(p[0] + ',' + str(p[1]) + '\n')
def when_nofile(filename):
	with open(filename, 'w',encoding = 'utf-8') as d:	
		d.write('商品,價格\n')
	
def main():
	filename = 'products.csv'  	 
	if os.path.isfile(filename):#檢查檔案
		print('ya!i got some good!')
		products = read_file(filename)
	else:
		print('nothing in here!')
		when_nofile(filename)
		products = read_file(filename)				
	user_input(products)
	print_products(products)
	write_file(filename, products)
main()
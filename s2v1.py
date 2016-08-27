import csv

def open_with_csv(filename, d='\t'):
	data = []
	with open(filename, 'r') as tsvin:
		tie_reader = csv.reader(tsvin, delimiter=d)
		for line in tie_reader:
			data.append(line)
	return data

data_from_csv = open_with_csv('data.csv')
#print data_from_csv[0]

import numpy as np 
'''
FIELDNAMES = ['', 'id', 'priceLabel', 'name', 'brandId', 'brandName', 'imageLink', 'desc', 'vendor', 'print', 'material']
DATATYPES = [('myint','i'), ('myid','i'), ('price','f8'), ('name','a200'), ('brandId','<i8'), 
				('brandName','a200'), ('imageUrl','|S500'), ('description','|S900'), ('vendor','|S100'),
				('pattern','|S500'), ('material','|S50'),]

def load_data(filename, d='\t'):
	my_csv = np.genfromtxt(filename, delimiter=d, skip_header = 1, invalid_raise = False, names = FIELDNAMES, dtype=DATATYPES)

my_csv = load_data('data.csv')
print len(my_csv)
'''

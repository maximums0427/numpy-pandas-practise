from s2v1 import *
import numpy

def num_of_records(data_sample):
	return len(data_sample)-1 # exclude header

number_of_ties = num_of_records(data_from_csv)

print 'There are {} ties.'.format(number_of_ties)

def cal_sum(data_sample):
	prices = [float(x[2]) for x in data_sample[1:]]
	return sum(prices),sum(prices)/len(prices)

def check_material(data_sample):
	materials = [x[-1] for x in data_sample[1:]]
	dic = {}
	for i in materials:
		dic[i] = dic.get(i,0)+1 
	return dic

from prettytable import PrettyTable

def my_table(arg):
	x = PrettyTable(['Material','Number'])
	for m,n in arg.items():
		x.add_row([m[1:],n])
	print x

my_table(check_material(data_from_csv))




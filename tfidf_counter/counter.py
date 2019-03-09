""" Author: Syed Alfran Ali """
import sklearn
import math
import numpy
from collections import OrderedDict
from numpy import zeros, array

#Construction of a list of training set and testing set.

set_list=["trn_f1.txt","trn_f2.txt","trn_f3.txt","trn_f4.txt","trn_f5.txt"]

words=[]
files=[]
		
for var in set_list:
	fopen = open(var, "r")
	word_vec=fopen.read().split()
	files.append(len(word_vec))
	for word in word_vec:
		words.append(word.lower())	
	fopen.close()
	
		
	
#Creating an ordered dictionary to find all unique words.
ordered_dict = list(OrderedDict.fromkeys(words))


#Matrix to get the count vector
co_matrix = zeros([6,len(ordered_dict)])
tot=0

#filling the matrix and reading from files, storing count in "tot" variable
for var in set_list:
	fopen = open(var, "r")
	word_vec=fopen.read().split()
	for word in word_vec:
		co_matrix[tot][ordered_dict.index(word.lower())]+=1	
	tot+=1	
	fopen.close()
		
print("Covariance Matrix/ Count Vector: ")
print("   ",end=" ")
for var in ordered_dict:
	print(var,end="  ")
	
print()
numpy.asarray(ordered_dict)
file_numb=0
for var in set_list:
	print("File", file_numb+1, ":")
	for val in range(len(ordered_dict)):
		print(co_matrix[file_numb][val],end=" ")
	print()
	file_numb+=1
	
	
	
	
	
	
	
	

			

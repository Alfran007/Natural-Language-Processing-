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
co_matrix = zeros([5,len(ordered_dict)])
tot=0

print("T.F. Vector: ")
print("   ",end=" ")
for var in ordered_dict:
	print(var,end="  ")
	

print()
numpy.asarray(files)
for var in set_list:
	fopen = open(var, "r")
	word_vec=fopen.read().split()
	for word in word_vec:
		co_matrix[tot][ordered_dict.index(word.lower())]+=1		
		co_matrix[tot][ordered_dict.index(word.lower())]=(co_matrix[tot][ordered_dict.index(word.lower())])/files[tot]	
		co_matrix[tot][ordered_dict.index(word.lower())]=round(co_matrix[tot][ordered_dict.index(word.lower())],3)
	
	tot+=1	
	fopen.close()

numpy.asarray(ordered_dict)
file_numb=0
for var in set_list:
	print("File", file_numb+1, ":")
	for val in range(len(ordered_dict)):
		print(co_matrix[file_numb][val],end=" ")
	print()
	file_numb+=1
	

print()
print("---------------------------------XXX-------------------------------------")
print("I.D.F. Vector:")	
	
idf = zeros([len(ordered_dict)])

for word in ordered_dict:
	for var in set_list:
		fopen = open(var, "r")
		str=fopen.read()
		if(word in str):
			idf[ordered_dict.index(word.lower())]+=1
	if(idf[ordered_dict.index(word.lower())] == 0):
		idf[ordered_dict.index(word.lower())]=0
	else:			
		idf[ordered_dict.index(word.lower())]=round(math.log(5/(idf[ordered_dict.index(word.lower())]),10),3)
				

	
print("   ",end=" ")
for var in ordered_dict:
	print(var,end="  ")
	
	
print()

file_numb=0
for var in set_list:
	print("File", file_numb+1, ":")
	for val in range(len(ordered_dict)):
		print(idf[val],end=" ")
	print()
	file_numb+=1	
	
	
	
	
	

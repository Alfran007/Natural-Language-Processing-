""" Author: Syed Alfran Ali """
import numpy
import sklearn
from numpy import zeros, array
from collections import OrderedDict

#Function to get the similarity between diferent files/corpora.
def cosineSimilarity(w1, w2):
	product_dot = numpy.dot(w1, w2)
	w1Norm = numpy.linalg.norm(w1)
	w2Norm = numpy.linalg.norm(w2)
	return product_dot / (w1Norm*w2Norm)


# Have to enter testing set/ file. 
set_testing=input("Input the name of text file: ")

#Construction of a list of training set and testing set.

set_list=["trn_f1.txt","trn_f2.txt","trn_f3.txt","trn_f4.txt","trn_f5.txt",set_testing]

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



#Creating bag of words
bagOfWords = zeros([6,len(ordered_dict)])
tot = 0

#filling the matrix and reading from files, storing count in "tot" variable
for var in set_list:
	fopen = open(var, "r")
	word_vec=fopen.read().split()
	for word in word_vec:
		bagOfWords[tot][ordered_dict.index(word.lower())]+=1	
	tot+=1	
	fopen.close()
		

#List to store the Cosine similarity between the test file/5th indexed one and the training corpus/0 to 4th indexed.
list_similar=[]
list_similar.append(cosineSimilarity(bagOfWords[0], bagOfWords[5]))
list_similar.append(cosineSimilarity(bagOfWords[1], bagOfWords[5]))
list_similar.append(cosineSimilarity(bagOfWords[2], bagOfWords[5]))
list_similar.append(cosineSimilarity(bagOfWords[3], bagOfWords[5]))
list_similar.append(cosineSimilarity(bagOfWords[4], bagOfWords[5]))

#Getting the similarity index and storing maximum of similarity in "sim" variable
index=list_similar.index(max(list_similar))+1
sim=round(max(list_similar),2)*100

print("The similarity between test data and already trained data.")	
print("Trained file1 vs Test file:{}% ".format(round(cosineSimilarity(bagOfWords[0], bagOfWords[5]),2)*100))
print("Trained file2 vs Test file:{}% ".format(round(cosineSimilarity(bagOfWords[1], bagOfWords[5]),2)*100))
print("Trained file3 vs Test file:{}% ".format(round(cosineSimilarity(bagOfWords[2], bagOfWords[5])*100),2))
print("Trained file4 vs Test file:{}% ".format(round(cosineSimilarity(bagOfWords[3], bagOfWords[5]),2)*100))		
print("Trained file5 vs Test file:{}% ".format(round(cosineSimilarity(bagOfWords[4], bagOfWords[5]),2)*100))	
print("In train file {0} and test file maximum similarity is found which is equal to: {1}% ".format(index,sim))	

# Name: E MA
# Date: 12/07/2017
# Programming: Final

import nltk
import random
import matplotlib.pyplot as plt
import pandas as pd

#lists
lables = ['per_punc','density','read_ab','perc_V','perc_N','perc_ADJ','perc_DT','perc_RB','perc_CC','perc_MD']
authors = [0,0,1,1,1,]

#add author
data = open('data/EMA_data.txt', 'r')
dic = zip(data,authors)

#plot
data2 = pd.DataFrame(pd.read_csv(r'data/EMA_data.txt',header=None, delim_whitespace=True))
data2.plot()
plt.show()

#create a feature list
a = [i for i,j in dic]
D = []
def book_features(a,lables):
    dic = {}
    for i in range(len(a)):
        for j in range(len(lables)):
            #dic[a[i][j]] = lables[j]
            dic[lables[j]]=a[i][j]
            D.append(dic)
        return  D

#shuffled and traning and testing
accuracy = 0
for i in range(3):
    random.shuffle(D)
    train_set, test_set = D[:77],D[77:]
    data.close()
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    accuuacy +=nltk.classify.accuracy(classifier,test_set)

average_accuracy = accuracy/3*100
print("Average Accuracy is : ",average_accuracy)
print classifier.show_most_informative_features(5)




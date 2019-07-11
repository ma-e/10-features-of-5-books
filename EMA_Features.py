# Name: E MA
# Date: 12/07/2017
# Programming: Final

from __future__ import division
import urllib2,nltk
from nltk.corpus import gutenberg
from bs4 import BeautifulSoup

def pip_line(url):
    file = urllib2.urlopen(url).read()
    soup = BeautifulSoup(file,"lxml")
    raw = soup.get_text()
    tokens = nltk.wordpunct_tokenize(raw)
    text = nltk.Text(tokens)
    return text

def percent_punc(url):
    no_punc = [ w for w in pip_line(url) if w.isalpha()]
    have_punc = [w.lower() for w in pip_line(url)]
    return (1-(len(no_punc)/len(have_punc))) * 100

def density(url):
    words = [w.lower() for w in pip_line(url) if w.isalpha()]
    vocabulary = sorted(set(words))
    count_words = len(words)
    count_vocab = len(vocabulary)
    density = (count_vocab / count_words) * 100
    return density

def average_word_length(url):
    total_length = len(' '.join(pip_line(url)))
    num_words = len(pip_line(url))
    mu_w = total_length/num_words
    return mu_w

def average_sentence_length(url):
    total_length = len(' '.join(pip_line(url)))
    file = urllib2.urlopen(url).read()
    soup = BeautifulSoup(file,"lxml")
    raw = soup.get_text()
    num_lines = len(nltk.sent_tokenize(raw))
    mu_s = total_length/num_lines
    return mu_s

def read_ability(url):
    read_ability = 4.71 * average_word_length(url) + 0.5 * average_sentence_length(url) - 21.43
    return read_ability

def percent_V(url):
    num_words = len(pip_line(url))
    pos_tag = nltk.pos_tag(pip_line(url))
    num_V = [w for (w,t) in pos_tag if t == ('VB')]
    percent_V = (len(num_V) /num_words) * 100
    return percent_V

def percent_N(url):
    num_words = len(pip_line(url))
    pos_tag = nltk.pos_tag(pip_line(url))
    num_N = [w for (w,t) in pos_tag if t == ('NN')]
    num_N = len(num_N)
    percent_N = (num_N /num_words) * 100
    return percent_N

def percent_ADJ(url):
    num_words = len(pip_line(url))
    pos_tag = nltk.pos_tag(pip_line(url))
    num_JJ = [w for (w,t) in pos_tag if t == ('JJ')]
    num_JJ = len(num_JJ)
    percent_JJ = (num_JJ /num_words) * 100
    return percent_JJ


def percent_DT(url):
    num_words = len(pip_line(url))
    pos_tag = nltk.pos_tag(pip_line(url))
    num_DT = [w for (w,t) in pos_tag if t == ('DT')]
    percent_DT = (len(num_DT) /num_words) * 100
    return percent_DT

def percent_RB(url):
    num_words = len(pip_line(url))
    pos_tag = nltk.pos_tag(pip_line(url))
    num_RB = [w for (w,t) in pos_tag if t == ('RB')]
    percent_RB = (len(num_RB) /num_words) * 100
    return percent_RB

def percent_CC(url):
    num_words = len(pip_line(url))
    pos_tag = nltk.pos_tag(pip_line(url))
    num_CC = [w for (w,t) in pos_tag if t == ('CC')]
    percent_CC = (len(num_CC) /num_words) * 100
    return percent_CC

def percent_MD(url):
    num_words = len(pip_line(url))
    pos_tag = nltk.pos_tag(pip_line(url))
    num_MD= [w for (w,t) in pos_tag if t == ('MD')]
    percent_MD = (len(num_MD) /num_words) * 100
    return percent_MD






urls_Emma = ["http://www.gutenberg.org/files/21797/21797-8.txt",\
        "http://www.gutenberg.org/files/19136/19136.txt"]

urls_Austen = ["http://www.gutenberg.org/files/141/141-0.txt",\
          "http://www.gutenberg.org/files/25946/25946-8.txt",\
          "http://www.gutenberg.org/files/20687/20687-readme.txt"]

# A Sailor's Lass (Emma Leslie)
# A Tale of the Civil War (Emma Leslie)
# Mansfield Park (Jane Austen)
# Gevoel en verstand (Jane Austen)
# Pride and Prejudice (Jane Austen)


urls = ["http://www.gutenberg.org/files/21797/21797-8.txt",\
        "http://www.gutenberg.org/files/19136/19136.txt",\
        "http://www.gutenberg.org/files/141/141-0.txt",\
        "http://www.gutenberg.org/files/25946/25946-8.txt",\
        "http://www.gutenberg.org/files/20687/20687-readme.txt"]

#titles = "per_punc,density,read_ab,perc_V,perc_N,perc_ADJ,perc_DT,perc_RB,perc_CC,perc_MD"
#print titles

f = open("data/EMA_data.txt","w")
for i in urls:
    
    print ("%.5f    %.5f    %.5f    %.5f    %.5f    %.5f    %.5f    %.5f    %.5f    %.5f \n"% (percent_punc(i),density(i),read_ability(i),percent_V(i),percent_N(i),percent_ADJ(i),percent_DT(i),percent_RB(i),percent_CC(i),percent_MD(i)))
    
    f.write ("%.5f    %.5f    %.5f    %.5f    %.5f    %.5f    %.5f    %.5f    %.5f    %.5f \n"%(percent_punc(i),density(i),read_ability(i),percent_V(i),percent_N(i),percent_ADJ(i),percent_DT(i),percent_RB(i),percent_CC(i),percent_MD(i)))
            
f.close()









          




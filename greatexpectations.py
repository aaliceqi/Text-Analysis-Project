import urllib.request
import string
import sys
from unicodedata import category

#i want to find the most frequent words and see if it can summarize the book


def process_file(filename):
    '''
    In this function, I want to process the text to strip:
    1. the gutenberg headers in the very beginning of the text and the end of the text
    2. There seems to be \r and \n throughout the text, i would like to replace these with either a blank space or empty.
    3. any stopwords: to, a, is, are, etc. These common words will throw off my end results because these words provide no substance and will not be able to summarize the book.
    '''

    hist = {}
    #this url contains book text in string form
    url = 'https://www.gutenberg.org/files/1400/1400-0.txt'
    with urllib.request.urlopen(url) as f:
        text1 = f.read().decode('utf-8')
        
    fp = open(filename,encoding = 'UTF8')
    print(type(fp))
    #find unwanted texts
    unwanted_text1 = "*** START OF THE PROJECT"
    unwanted_text2 = "*** END OF THE PROJECT"

    #remove gutenburg headers and endings
    start_pos = text1.find(unwanted_text1)
    if start_pos != -1:
        text1 = text1[start_pos + len(unwanted_text1)]

    end_pos = text1.find(unwanted_text2)
    if end_pos != -1:
        text1 =text1[:end_pos]
    
    
    # strippables = ''.join(
    #     [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    # )

    for line in fp:
        line = line.replace('-','')
        line = line.replace(chr(8212),'')

    for word in line.split():
        # word = word.strip(strippables)
        word = word.lower()

        hist[word] = hist.get(word,0)+1

    return hist

def skip_gutenberg_header(fp):
    pass
    # for line in fp:
    #     if line.startswith('***START OF THIS PROJECT'):
    #         break

def top_ten(hist, excluding_stopwords=False):
    '''
    I want this function to 
    
    '''
    
def main():
    url = 'https://www.gutenberg.org/files/1400/1400-0.txt'
    with urllib.request.urlopen(url) as f:
        text1 = f.read().decode('utf-8')
        # print(type(text1)) # for testing
    hist = process_file(text1)
    print(type(hist))

    # print(process_file())
    
if __name__ == '__main__':
    main()

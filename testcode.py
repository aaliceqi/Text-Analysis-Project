import urllib.request
import sys
from unicodedata import category
import pprint

def replace_space(file):
    words = ""

    for word in file:
        words += word
    words = words.replace("\n", " ").replace("\r", "").replace(" "," ").replace("-", " ").replace(chr(8212), " ")

    return words

def strip_gutenberg_header(file):
    #find unwanted texts ends and beginnings
    unwanted_text1 = "CONTENTS"  #words you want to remove before this word 
    unwanted_text2 = "*** END OF THIS PROJECT" #words you want to remove after this word and word

    #remove gutenburg headers and endings
    start_pos = file.find(unwanted_text1)
    if start_pos != -1:
        book = file[start_pos:]

    end_pos = book.find(unwanted_text2)
    if end_pos != -1:
        book_update =book[:end_pos]

    return book_update



def strip_stopwords(file):
    '''
    This function strips stopwords and strippables
    '''
    #pull file stopwords.txt
    f= open("stopwords.txt")

    #put context of stopwords.txt file into this string and then make it into a list
    stopwords = ""
    for line in f:
        stopwords += line
    stopwords_strip = replace_space(stopwords)
    stopwords_list = stopwords_strip.split()

    # define what strippables is -- a collection of punctuations and symbols
    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    # if strip_header:
    #     strip_gutenberg_header(file)

    #put context of book file into a new string
    book = ""

    #make sure each word in file is lowercased
    for word in file:
        book += word.lower()
    text_strip = replace_space(book)
    
    # turn string into list & remove strippables
    text_list = text_strip.split()
    text_list = ["".join([c for c in word if c not in strippables]) for word in text_list]
    
    #return only words that are not in stopwords list
    text_list = [word for word in text_list if word not in stopwords_list]

    return text_list



def most_common_words(file, num):
    common = {}
    for word in file:
        common[word] = common.get(word, 0)+1
    res = []
    for word in common:
        freq = common[word]
        res.append((freq,word))
    res.sort(reverse=True)
    return res[:num]




def main():
    #can change this url to book of choice from the gutenberg database
    url = 'https://www.gutenberg.org/cache/epub/398/pg398.txt' #Adam & Eve Bible
    # 'https://www.gutenberg.org/cache/epub/46/pg46.txt' The Christmas Carol
    # 'https://www.gutenberg.org/files/1400/1400-0.txt' Great Expectations
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
    strip_header = strip_gutenberg_header(text)
    stripped_text = strip_stopwords(strip_header)
    number_of_most_frequent_words = 20
    pprint.pprint(most_common_words(stripped_text, number_of_most_frequent_words))
   


if __name__ == '__main__':
    main()




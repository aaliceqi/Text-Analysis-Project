import urllib.request
import sys
from unicodedata import category


def open_file():
    url = 'https://www.gutenberg.org/files/1400/1400-0.txt'
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        return text
book = open_file()
# print(type(book))

def strip(file):
    words = ""

    for word in file:
        words += word
    words = words.replace("\n", " ").replace("\r", "").replace(" "," ").replace("-", " ").replace(chr(8212), " ")

    return words

    
new_book = strip(book)

def strip_gutenberg_header(file):
    #find unwanted texts
    unwanted_text1 = "[Illustration]"
    unwanted_text2 = "*** END OF THE PROJECT"

    #remove gutenburg headers and endings
    start_pos = file.find(unwanted_text1)
    if start_pos != -1:
        book = file[start_pos:]

    end_pos = book.find(unwanted_text2)
    if end_pos != -1:
        book_update =book[:end_pos]

    return book_update
# print(strip_gutenberg_header(new_book))

new_book = strip_gutenberg_header(new_book)
# print(new_book)

def strip_stopwords(file):
    '''
    make function into a list or dictionary 
    '''
    f= open("stopwords.txt")
    stopwords = ""

    for line in f:
        stopwords += line
    stopwords_strip = strip(stopwords)
    stopwords_list = stopwords_strip.split()

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    book = ""

    for word in file:
        book += word.lower()
    
    text_list = book.split()
    text_list = ["".join([c for c in word if c not in strippables]) for word in text_list]
    # print(text_list)
    text_list = [word for word in text_list if word not in stopwords_list]

    return text_list

new_book = strip_stopwords(new_book)

def most_common_words(file):
    common = {}
    for word in file:
        common[word] = common.get(word, 0)+1
    res = []
    for word in common:
        freq = common[word]
        res.append((freq,word))
    res.sort(reverse=True)
    return res[:10]


print(most_common_words(new_book))

def main():
    pass

if __name__ == '__main__':
    main()




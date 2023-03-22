import urllib.request
import string
import sys
from unicodedata import category

def strip(text1):
    a = {}
    a = text1.replace("\n","").replace("\r", "").replace(" "," ")


def process_file(filename, skip_header=False):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')
    print(type(hist))

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THE PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    total = 0 
    for word in hist.keys():
        total += hist[word]
    return total


def different_words(hist):
    """Returns the number of different words in a histogram."""
    # total = 0 
    # for word in hist:
    #     total += 1
    # return total
    return len(hist) #each key is unique


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    stopwords = process_file('data/stopwords.txt')
    print(type(stopwords))
    res = []
    for word in hist:
        if excluding_stopwords:
            if word in stopwords:
                continue

        freq = hist[word]
        res.append((freq, word))
    res.sort(reverse=True)
    # return res

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """

    mostcommon = most_common(hist,excluding_stopwords=True)[:num]
    for freq,word in mostcommon:
        print(f'{word}: {freq}')
    
  

def main():
    url = 'https://www.gutenberg.org/files/1400/1400-0.txt'
    with urllib.request.urlopen(url) as f:
        text1 = f.read().decode('utf-8')
        # print(type(text1))
    hist = process_file(text1, skip_header=True)



    print((hist))
    # print('Total number of words:', total_words(hist))
    # print('Number of different words:', different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    
    # print_most_common(hist, num=10)

    # words = process_file('data/words.txt', skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    # print("\n\nHere are some random words from the book:")
    # for i in range(100):
    #     print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()
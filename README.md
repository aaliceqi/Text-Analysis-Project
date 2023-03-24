# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

## Project Overview
For this project, I chose to use the Project Gutenburg data source to retrieve a plain text utf-8 file of Great Expectations by Charles Dickens because this is one of the most famous book in the American Curriculum. I also decided to use a book because I figured that I could apply what I have learned in the previous exercise on this and could be more creative with it. My main goal in this project is to see if the 10 most frequent words of a book can provide the themes and tone of a book's content. I want to remove common words and really only keep substance words in there. Some of these words include "to, and, a, etc." 

## Implementation
In order to implement this project, there are a couple major step groups. These groups include retrieving and reading the data source, stripping the data source to gain better results, utilizing the stripped data and counting and sorting the frequency of each word. Ultimately, this should return the list of most used words in the text. A large part of my focus in the beginning stages of implementation was figuring out what I wanted to strip. Based off of books in general, there are a lot of stopwords that are essential in grammatically correct sentences, but it wouldn't provide me any information on the context of the book. Since I was using the Project Gutenburg data sources, I also realized that each data text had headings and endings filled with information about Project Gutenburg. I had to remove these as well because they can skew my results with content from these headings/ endings. 

During my strippings, I really struggled with changing from string to list and figuring out how to make a list of the words in the text and not the letters of the text. Here's a picture of me failing terribly and returned all the letters of the text and not the words:
![Screenshot of each letter in list form](images/listerror.JPG) 
Utilizing .strip helped me fix this problem. Furthermore, throughout my implementation process, I was constantly testing my code with different text as well. By the end of the implementation, I was trying to improve my code by stripping away more words or fixing the tense of the words. This was where I utilized ChatGBT the most. ChatGBT helped me navigate how to change the tense of each word. I wouldn't have known to use NLTK if it did not suggest it. Here's an image of ChatGBT helping me: 

## Results
Through this project, I was able to generate a list of the most frequently used words of a given text. My code can be used by any UTF-8 file from the Gutenberg Project database with a couple minor tweeks. (The starting and ending phases of the Gutenberg headers because I noticed that they differ between each book.) Based off of my final results, my results differed widely. For example, books with a strong theme, such as the Christmas Carol by Charles Dickens or Adam and Eve By Rutherford Platt, the generated words did give a good amount of context and the general theme and tone of the book. However, advanced literature that includes more metaphors and analysis, such as The Great Expectations by Charles Dickens, did not truly summarize the book well. Below are the images of the generated results. 

The first book that I analyzed was Great Expectations by Charles Dickens. The results proved

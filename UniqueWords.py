
'''
A Series of python functions that work with Text Files too find the number of Unique Words
'''
import re
from collections import Counter


def WordCount(file):
    '''
    Returns the Total and Unique word count and the percentage of Unique/Total from file path (file)
    '''

    book_txt = ''

    for line in open(file).readlines(): 
        ''.join(e for e in line if e.isalnum())
        book_txt =  book_txt + line

    words = book_txt.split()
    uniq_words = set(words)

    print('\nTotal Word Count: ' + str(len(words)))
    print('Unique Word Count: ' + str(len(uniq_words)) + '\n')
    print( str(round((len(uniq_words)/len(words))*100, 2)) + '%' )


def DefinedWordCount(file):
    book_txt = ''

    for line in open(file).readlines(): 
        ''.join(e for e in line if e.isalnum())
        book_txt =  book_txt + line

    book_txt = re.sub(r"[^a-zA-z0-9]+", ' ' , book_txt)
    words = book_txt.split()

    for word in words:
        word =  word.lower()

    definedUniq = DefinedCount(file, True)
    TotalWords = []

    for word in words:
        if word in definedUniq:
            TotalWords.append(word)

    print('\n' + str(len(TotalWords)) + " is the number of words that are defined in the Dictionary")

def ListUndefined(file):
    book_txt = ''

    for line in open(file).readlines(): 
        book_txt =  book_txt + line

    book_txt = book_txt.lower()
    book_txt = re.sub(r"[^a-zA-z0-9]+", ' ' , book_txt)
    words = book_txt.split()

    definedUniq = DefinedCount(file, True)
    TotalWords = []

    for word in words:
        if word not in definedUniq:
            TotalWords.append(word)

    print(TotalWords)
    print(len(TotalWords))

def ListWords(file):
    '''
    Take a file and Output the set of all words
    '''
    
    book_txt = ''

    for line in open(file).readlines(): 
        ''.join(e for e in line if e.isalnum())
        book_txt =  book_txt + line

    words = book_txt.split()

    print(words)
    print(len(words))

def ListUnique(file):
    '''
    Take a file and Output the set of Unique Words
    '''
    book_txt = ''

    for line in open(file).readlines(): 
        ''.join(e for e in line if e.isalnum())
        book_txt =  book_txt + line

    words = book_txt.split()
    uniq_words = set(words)

    print(uniq_words)
    print(len(uniq_words))


def diff(file1, file2, returnList = False):
    '''
    Take Two Files and show the Unique Words they do not have in common, if verbose is on return the list
    '''
    file1_txt = ''
    file2_txt = ''

    for line in open(file1).readlines():
        ''.join(e for e in line if e.isalnum())
        file1_txt =  file1_txt + line

    for line in open(file2).readlines(): 
        ''.join(e for e in line if e.isalnum())
        file2_txt =  file2_txt + line

    words1 = file1_txt.split()
    uniq_words1 = set(words1)

    words2 = file2_txt.split()
    uniq_words2 = set(words2)

    if returnList != True: print('\n' + str(len( uniq_words1 - uniq_words2 )) + ' Words that are not shared in both text files')
    if returnList == True: return uniq_words1 - uniq_words2
 

def same(file1, file2, returnList = False):
    '''
    Take Two Files and find the unique words that both files share, if Verbose is true return the list - Returns the common list
    '''

    file1_txt = ''
    file2_txt = ''

    for line in open(file1).readlines():
        ''.join(e for e in line if e.isalnum())
        file1_txt =  file1_txt + line

    for line in open(file2).readlines(): 
        ''.join(e for e in line if e.isalnum())
        file2_txt =  file2_txt + line

    words1 = file1_txt.split()
    uniq_words1 = set(words1)

    words2 = file2_txt.split()
    uniq_words2 = set(words2)

    if returnList != True: print('\n' + str(len(set(uniq_words1).intersection(uniq_words2))) + ' Words are used in both text files')
    if returnList == True: return uniq_words1.intersection(uniq_words2)


def DefinedCount(file, returnList = False):
    '''
    Using the included "txtFiles\Dict.txt" file as a list of defined words, find the number of words we know are for sure words
    '''
    file1_txt = ''
    file2_txt = ''

    for line in open(file).readlines():
        file1_txt =  file1_txt + line

    for line in open("txtFiles/Dict.txt").readlines(): 
        file2_txt =  file2_txt + line

    words1 = file1_txt.split()
    uniq_words1 = set(words1)

    words2 = file2_txt.split()
    uniq_words2 = set(words2)

    if returnList != True: print('\n' + str(len(set(uniq_words1).intersection(uniq_words2))) + ' Is the number of  unique words that are defined')
    if returnList == True: return uniq_words1.intersection(uniq_words2)


def DefineWord(word):
    '''
    Adds the word too the list in Dict in case something should be defined as a word
    '''
    f = open("txtFiles/Dict.txt", "a")
    f.write("\n" + word)

def isDefined(word):
    '''
    Test for if a word is in the Dictionary
    '''

    file2_txt = ''

    for line in open("txtFiles/Dict.txt").readlines(): 
        ''.join(e for e in line if e.isalnum())
        file2_txt =  file2_txt + line

    defined = file2_txt.split()

    if word in set(defined):
        print('Word is Defined')
    else:
        print('Word is Undefined')


def main():
    '''
    A main function, anything put in here will run if the file is called as a script
    '''


if __name__ == "__main__":
    main()

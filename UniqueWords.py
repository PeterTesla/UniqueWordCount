'''
A Series of python functions that work with Text Files too find the number of Unique Words
'''

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

def diff(file1, file2, verbose = False):
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

    print('\n' + str(len( uniq_words1 - uniq_words2 )) + ' Words that are not shared in both text files')
    if verbose == True: return uniq_words1 - uniq_words2
    
def same(file1, file2, verbose = False):
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

    print('\n' + str(len(set(uniq_words1).intersection(uniq_words2))) + ' Words are used in both text files')

    if verbose == True: return uniq_words1.intersection(uniq_words2)

def DefinedCount(file, verbose = False):
    '''
    Using the included "txtFiles\Dict.txt" file as a list of defined words, find the number of words we know are for sure words
    '''
    file1_txt = ''
    file2_txt = ''

    for line in open(file).readlines():
        ''.join(e for e in line if e.isalnum())
        file1_txt =  file1_txt + line

    for line in open("txtFiles/Dict.txt").readlines(): 
        ''.join(e for e in line if e.isalnum())
        file2_txt =  file2_txt + line

    words1 = file1_txt.split()
    uniq_words1 = set(words1)

    words2 = file2_txt.split()
    uniq_words2 = set(words2)

    print('\n' + str(len(set(uniq_words1).intersection(uniq_words2))) + ' Is the number of words that are defined')

    if verbose == True: return uniq_words1.intersection(uniq_words2)

def DefineWord(word):
    '''
    Adds the word too the list in Dict in case something should be defined as a word
    '''
    f = open("txtFiles/Dict.txt", "a")
    f.write("\n" + word)

def main():

    pass

if __name__ == "__main__":
    main()
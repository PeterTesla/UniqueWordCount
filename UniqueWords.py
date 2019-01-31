'''
A Python script that works with large text files returning the number of words and number of unique words
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
    pass

def diff(file1, file2, verbose = "False"):
    '''
    Take Two Files and show the Unique Words they do not have in common
    '''
    pass

def same(file1, file2, verbose="False"):
    '''
    Take Two Files and find the unique words that both files share, if Verbose is true return actual list - Returns the common list
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


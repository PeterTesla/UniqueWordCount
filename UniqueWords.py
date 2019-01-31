'''
A Python script that works with large text files returning the number of words and number of unique words
'''

def WordCount(file):
    '''
    Returns the Total and Unique word count and the percentage of Unique/Total from file
    '''

    book_txt = ''

    for line in open(file).readlines(): 
        book_txt =  book_txt + line

    words = book_txt.split()
    uniq_words = set(words)

    print('\nTotal Word Count: ' + str(len(words)))
    print('Unique Word Count: ' + str(len(uniq_words)) + '\n')
    print( str(round((len(uniq_words)/len(words))*100, 2)) + '%' )


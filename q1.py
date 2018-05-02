#'/Users/mwirvine/galvanize/tech-exercise/q1textfile.txt'

'''
Enter commentary here! I'm sure that will be reviewed
write the functions, then write the program below
'''

def open_file(path_to_file):
    with open(path_to_file) as f:
        text_file_string = f.read()
    return text_file_string

def count_words(text_file_string):
    # split the string into a list with space as the delimiter, and count the length to get the word count
    return len(text_file_string.split())

def count_sentences(text_file_string):
    ## count the number of punctuations that end a sentence and total number
    return text_file_string.count('.') + text_file_string.count('?') + text_file_string.count('!')

def count_unique_words(text_file_string):
    ## identify punctuation to remove and create a string with no punctuation
    punc_to_remove = ['!', '.', ',', '?']
    no_punc_string = ''.join([char for char in text_file_string if char not in punc_to_remove])

    ## place all the words in a set so only unique words are added, and return the length of the set
    unique_word_set = set(no_punc_string.split())
    return len(unique_word_set)

def calc_avg_sent_length(text_file_string):
    # replace '!' and '?' with periods so sentence can be split on '.'
    periods_only_string = text_file_string.replace('!', '.')
    periods_only_string = periods_only_string.replace('?', '.')

    # create a list of sentences, using '.' as the delimiter
    periods_only_list = periods_only_string.split('. ')

    # create a new list with the number of words in each sentence
    sentence_word_length = [periods_only_list[i].count(' ') + 1 for i, sentence in enumerate(periods_only_list)]

    # calculate the average sentence length in words
    return round(sum(sentence_word_length) / len(sentence_word_length), 1)

def identify_frequent_words(text_file_string):
    # remove punctuation from the string
    punc_to_remove = ['!', '.', ',', '?']
    no_punc_string = ''.join([char.lower() for char in text_file_string if char not in punc_to_remove])

    # split the string into a list of words
    text_file_list = no_punc_string.split()

    # create a new list with a word count for each word in the string
    word_count_list = [text_file_list.count(word) for word in text_file_list]

    # zip the two lists together into a list of tuples with (word count for whole string, word)
    zipped_list = list(zip(word_count_list, text_file_list))

    # sort by the word count tuple, then reverse to have most frequently used words on top
    zipped_list.sort()
    zipped_list.reverse()

    # pull the words out of the zipped list in order of frequency and place into a new list
    ranked_list_dups = [word[1] for word in zipped_list]

    # remove duplicates from the previous list but keep the order - put in a new list
    no_dup_set = set()
    ranked_list_no_dups = []
    for word in ranked_list_dups:
        if word not in no_dup_set:
            no_dup_set.add(word)
            ranked_list_no_dups.append(word)

    return ranked_list_no_dups

def print_stats(text_file_string):
    print('Total word count: {}'.format(count_words(text_file_string)))
    print('Unique words: {}'.format(count_unique_words(text_file_string)))
    print('Sentences: {}'.format(count_sentences(text_file_string)))
    print('Avg sentence length in words: {}'.format(calc_avg_sent_length(text_file_string)))
    print('List of words used, in order of descending frequency: {}'.format(identify_frequent_words(text_file_string)))

# program to run below

path_to_file = str(input('Enter the path of the text file to analyze: '))

text_file_string = open_file(path_to_file)

print_stats(text_file_string)

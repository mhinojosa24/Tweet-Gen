
'''
- What is the least/most frequent word(s)?
- How many different  awords used?
- What is the average (mean/median/mode) frequency of words in the text?


<--- FUNCTIONS --->

histogram()
    - takes a 'source_text' argument and return a histogram data structure that stores each unique word.

unique_words()
    - takes a histogram argument and returns the total count of unique words in the histogram.

frequency()
    - takes a word and histogram argument and returns the number of times that word appears in a text.
'''

import sys

text = "one fish two fish red fish blue fish"
file = "text_file.txt"
# dictionary is most fast, wasteful in terms of space
def histogram(source_text):
    dictionary = dict()

    with open('{}'.format(source_text), 'r') as f:
        text_file = f.read()
        text = text_file.split(' ')

    for word in text:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary


def unique_words(histogram):
    values = histogram.values()
    sum = 0

    for value in values:
        sum += value
    print(sum)


def frequency(word, histogram):

    if word in histogram:
        appearance = histogram.get('{}'.format(word))
        print("{}: {}".format(word, appearance))
    else:
        print("Not Found")

# less wasteful rather than a dictionary
def list_of_list(source_text):
    text = source_text.split(' ')
    sum_list = []

    for word in text:
        found = False
        for w in sum_list:
            if w[0] == word:
                found = True
                w[1] = w[1] + 1
                break
        if not found:
            sum_list.append([word, 1])


    print(sum_list)

# list of tuples is less wasteful in space rather than list of list
def list_of_tuples(source_text):
    text = source_text.split(' ')
    list = []

    for word in text:
        found = False
        for w in list:
            if word == w[0]:
                found = True
                count = w[1] + 1
                list.remove(w)
                # creates a tuple and appends into a list
                list.append((word, count))
                break

        if not found:
            list.append((word, 1))

    print(list)


# most effient of memory in terms of all
def list_of_counts(source_text):
    text = source_text.split(' ')



def main():
    # histo = histogram(file)
    # unique_words(histo)
    # word = sys.argv[1]
    # frequency(word, histo)
    list_of_list(text)
    # list_of_tuples(text)
    # list_of_counsts(text)

if __name__ == "__main__":
    main()
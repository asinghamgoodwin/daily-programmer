#daily programmer easy challenge - alphabetical words

import sys

def checkOrder(word):
    current = 'a'
    for letter in word:
        if letter < current:
            return checkReverse(word) #we know its not in order, it could either be reverse or not in order from this point.
        else:
            current = letter
    return "IN ORDER"

def checkReverse(word):
    current = 'z'
    for letter in word:
        if letter > current:
            return "NOT IN ORDER"
        else:
            current = letter
    return "REVERSE ORDER"


#input = ['billowy', 'biopsy', 'chinos', 'defaced', 'chintz', 'sponged', 'bijoux', 'abhors', 'fiddle', 'begins', 'chimps', 'wronged']

#for word in input:
#    print word + " " + checkOrder(word)

for line in sys.stdin:
    word = str(line).rstrip()
    print word + " " + checkOrder(word)

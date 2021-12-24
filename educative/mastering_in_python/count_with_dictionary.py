from collections import defaultdict
from collections import OrderedDict

def count_letters(message):

    d = defaultdict(int)    # Making dictionary with int
    for letter in message:
        d[letter] += 1      # Adding 1 with every repetition

    # Sorting on the basis of values
    return OrderedDict(sorted(d.items(), key = lambda t:t[1]))

print(count_letters('Welcome to Educative'))
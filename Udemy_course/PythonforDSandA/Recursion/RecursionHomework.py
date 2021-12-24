def sum_func(n):
    if n % 10 == n:
        return n

    return n % 10 + sum_func(n//10)

def word_split(phrase,list_of_words, output = None):
    if output is None:
        output =[]
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):], list_of_words, output)
    return output

assert sum_func(4321) == 10
assert word_split('themanran',['the','ran','man']) == ['the', 'man', 'ran']
assert word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']) == ['i', 'love', 'dogs', 'John']
assert word_split('themanran',['clown','ran','man']) == []
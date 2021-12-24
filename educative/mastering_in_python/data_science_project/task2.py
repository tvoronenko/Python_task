# decorator for returning length of an iterator
def count(func):
    def wrapper(*args):
        result = func(*args)
        result = len(result)
        return result
    return wrapper


# Getting males from the data
@count
def get_females(data):
    return [entry for entry in data if entry.Gender == '1']


# Getting femlaes from the data
@count
def get_males(data):
    return [entry for entry in data if entry.Gender == '2']
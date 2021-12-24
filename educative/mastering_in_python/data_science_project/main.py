import csv
from collections import defaultdict, Counter
#from ..data_science_project.task1 import group_values_with_columns
from educative.mastering_in_python.data_science_project.task1 import group_values_with_columns
from educative.mastering_in_python.data_science_project.task2 import get_females, get_males, count
from educative.mastering_in_python.data_science_project.cleaner import gpa_cleaner, gender_cleaner, drink_cleaner, exercise_cleaner, fries_cleaner, income_cleaner, sports_cleaner, weight_cleaner

# Getting drink stats
def drink_stats(data):

    d = defaultdict(int) # Creating a dictionary

    for entry in data:
        d[entry.drink] += 1 # Separate key for each drink

    return d


# Getting weight stats
def weight_stats(data, x):
    d = defaultdict(int)
    for entry in data:
        if entry.weight.isnumeric():
            d[entry.weight] += 1

    # 1ST IMPLEMENTATION
    c = Counter(d)

    most = c.most_common(x)
    mweight_result = [i[0] for i in most]

    least = c.most_common()[:-x - 1:-1]
    lweight_result = [i[0] for i in least]

    return get_females([entry for entry in data if entry.weight in mweight_result]), get_males(
        [entry for entry in data if entry.weight in lweight_result])

# Students loving McDonald's fries
Mcdonalds_fries = count(lambda my_data: [entry for entry in my_data if entry.fries == '1'])
# Getting bright students
bright_students = lambda my_data: [entry for entry in my_data if
                                   entry.GPA > '3' and (entry.income == '5' or entry.income == '6')]


# Cleaning the dataset
@weight_cleaner
@sports_cleaner
@income_cleaner
@fries_cleaner
@exercise_cleaner
@drink_cleaner
@gender_cleaner
@gpa_cleaner
def clean_data(data):
    return data

if __name__ == '__main__':
    data = []
    # Reading the dataset in a list
    with open('food_coded.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)  # contains the data in the raw format.

    # Columns you'll deal with in this project
    required_columns = ['GPA', 'Gender', 'drink', 'exercise', 'fries', 'income', 'sports', 'weight']

    # Calling the function
    grouped_data = group_values_with_columns(data, required_columns, n=60)
    #for entry in grouped_data:
     #   print(entry)

    print(get_females(grouped_data))
    print(get_males(grouped_data))
    print(drink_stats(grouped_data))


    print(Mcdonalds_fries(grouped_data))

    students = bright_students(grouped_data)
    #for entry in students:
    #    print(entry)

    print(weight_stats(grouped_data, 2))


    cleaned_data = clean_data(grouped_data)
    print(cleaned_data)


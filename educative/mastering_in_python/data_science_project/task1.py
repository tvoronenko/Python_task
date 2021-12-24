from collections import namedtuple

def group_values_with_columns(orig_data, req_col, **kwargs):
    # Namedtuple to create a pair with column and its values
    Student = namedtuple('Student', 'GPA Gender drink exercise fries income sports weight')
    columns_index = [orig_data[0].index(name) for name in req_col]

    if kwargs:  # if limit is passed
        individuals = orig_data[1:kwargs['n'] + 1]
    else:
        individuals = orig_data[1:51]  # 50 by default

    grouped_data = []  # List of tuples of columns and values

    for individual in individuals:
        value = [individual[i] for i in columns_index]
        grouped_data.append(Student._make(value))

    return grouped_data

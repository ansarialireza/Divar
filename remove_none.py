def remove_none_values(data):
    return [item for item in data if item is not None]

def clean_nested_list(nested_list):
    return [remove_none_values(inner_list) for inner_list in nested_list]

def remove_last_none(data):
    reversed_data = data[::-1]
    index = next((i for i, x in enumerate(reversed_data) if x is not None), None)
    return data[:-index] if index is not None else data

def remove_last_sublist(matrix):
    if not matrix:
        print("The list is empty.")
        return

    matrix.pop()
    return matrix
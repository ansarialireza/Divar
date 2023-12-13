def remove_string_from_list(input_list, string_to_remove):
    cleaned_list = [
        [item.replace(string_to_remove, '') for item in row]
        for row in input_list
    ]
    return cleaned_list



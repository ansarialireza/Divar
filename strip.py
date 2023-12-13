def clean_data(raw_data):
    cleaned_data = []
    # if raw_data is None:
    #     return []

    for item in raw_data:
        if item is not None:
            cleaned_item = [value.strip() if isinstance(value, str) else value for value in item]
            cleaned_data.append(cleaned_item)

    return cleaned_data
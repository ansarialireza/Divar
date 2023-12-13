def convert_to_english_cars(cars_list):
    english_numbers = {'۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'}

    def convert_item(item):
        for persian, english in english_numbers.items():
            item = item.replace(persian, english)
        return item

    converted_cars_list = []
    for car in cars_list:
        converted_car = [convert_item(item) for item in car]
        converted_cars_list.append(converted_car)

    return converted_cars_list
 
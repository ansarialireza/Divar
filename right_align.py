def right_align_list(input_list):
    max_lengths = [max(len(str(item)) for item in col) for col in zip(*input_list)]
    aligned_list = [
        [' ' * (max_len - len(str(item))) + str(item) for max_len, item in zip(max_lengths, row)]
        for row in input_list
    ]
    return aligned_list

# Example usage:
# Assuming your list is named cars_list
# cars_list = [
#     ['پراید صندوق\u200cدار CNG، مدل 1386', '340,000 کیلومتر', '137,000,000 تومان', 'دقایقی پیش در تهران'],
#     ['پیکان وانت بنزینی، مدل 1385', '490,000 کیلومتر', '130,000,000 تومان', 'دقایقی پیش در مشهد']
# ]

# right_aligned_cars_list = right_align_list(cars_list)

# # Print the right-aligned list
# for row in right_aligned_cars_list:
#     print(row)

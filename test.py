import data_cleaner
b=[['220,000 khylwmtr', '560,000,000 twmn', 'dqyqy pysh dr khrmnshh'],['230,000 khylwmtr', '560,000,000 twmn', 'dqyqy pysh dr khrmnshh'],['200,000 khylwmtr', '560,000,000 twmn', 'dqyqy pysh dr khrmnshh']]
for i in b:
    #print(i[0])
    a=data_cleaner.extracting_numbers(i[0])
    c=data_cleaner.extracting_numbers(i[1])
    i[0]=a
    i[1]=c
    #print(i[0])
print(b)
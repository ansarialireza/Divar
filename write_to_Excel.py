import pandas as pd

def write_to_excel(cars_list):
    # Create a DataFrame from the list
    df = pd.DataFrame(cars_list, columns=['نام خودرو', 'کیلومتر', 'قیمت', 'مکان'])

    # Write to Excel
    df.to_excel('output.xlsx', index=False, startrow=1)


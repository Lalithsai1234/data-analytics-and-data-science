def clean_data(data_list):
    cleaned_list = []
    for item in data_list:
        if isinstance(item, str) and item.endswith('k'):
            try:
                number = float(item[:-1]) * 1000
                cleaned_list.append(number)
            except ValueError:
                continue
        elif isinstance(item, (int, float)):
            cleaned_list.append(item)
    return cleaned_list



expenses= [1721, 299, 675, 1456, "1k", None]
revenue= [2000, 1500, 3000, "2k", None, 2500]
print("Original Expenses:", expenses)
print("Original Revenue:", revenue)
cleaned_expenses = clean_data(expenses)
cleaned_revenue = clean_data(revenue)
print("Cleaned Expenses:", cleaned_expenses)
print("Cleaned Revenue:", cleaned_revenue)
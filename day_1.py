# Load required packages
import os
import re

# Define input file name
file_name = "day1_prompt.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2023-advent-of-code/data/{file_name}"
input_data = open(file_path, 'r').read().split('\n')


### Part 1 --------------------------------------------------------------------------------------------------------------------------------------------

# Loop through each line
ttl_list = []
for i in input_data:
    
    # Loop through each character
    num_list = []
    for j in i:
        
        # Check if character is numeric - append to list if so
        if j.isdigit():
            num_list.append(j)

    if len(num_list) == 0:
        num_list.append('0')

    # Append final number from each row
    ttl_list.append(int(num_list[0] + num_list[-1]))

# Define answer #1
answer_1 = sum(ttl_list)        
print(answer_1)

### Part 2 --------------------------------------------------------------------------------------------------------------------------------------------
value_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
value_dict = {'one': 1, 'two': 2, 'three':3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

ttl_list = []
# Loop through each line
for i in input_data:

    # Loop through each character
    num_dict = {}
    num_list = []
    for j in range(len(i)):
        
        # Check if character is numeric - append to list if so
        if i[j].isdigit():
            num_dict[j] = i[j]

    # Chech for written values
    string_dict = {}
    for string in value_list:

        
        # If value exists
        if i.find(string) >= 0:

            # Find all occurences
            val_list = [i.start() for i in re.finditer(string, i)]

            # Loop through positions and add to dict
            for q in val_list:

                string_dict[q] = str(value_dict[string])

    # Join dictionaries
    check_dict = string_dict | num_dict

    # Sort dictionary
    myKeys = list(check_dict.keys())
    myKeys.sort()
    sorted_dict = {i: check_dict[i] for i in myKeys}

    # Track totals
    ttl_list.append(int(list(sorted_dict.values())[0] + list(sorted_dict.values())[-1]))


# Define answer #2
answer_2 = sum(ttl_list)        
print(answer_2)




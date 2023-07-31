import pandas as pd

def add_data_to_excel(roll_num, name):
    # Read existing data from the Excel file, if any
    try:
        df = pd.read_excel('data.xlsx')
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame
        df = pd.DataFrame(columns=['Roll Number', 'Name'])

    # Append the new data to the DataFrame
    new_data = pd.DataFrame({'Roll Number': [roll_num], 'Name': [name]})
    df = pd.concat([df, new_data], ignore_index=True)

    # Save the DataFrame to the Excel file
    df.to_excel('data.xlsx', index=False, engine='openpyxl')

    return "Successfully added data to Excel."

# Taking user input for Roll Number and Name
roll_num_input = input("Enter Roll Number: ")
name_input = input("Enter Name: ")

# Call the function to add data to Excel
result = add_data_to_excel(roll_num_input, name_input)
print(result)

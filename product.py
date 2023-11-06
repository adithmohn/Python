import json

# Read your data from a file (update the path to your data file)
data_file_path = 'python/sample (1).txt'  # Update the path to your data file

# Initialize a dictionary to store the product conditions and their counts for both Description and Short Description
product_conditions = {
    'New': {'Description': 0, 'Short Description': 0, 'Total': 0},
    'Refurbished': {'Description': 0, 'Short Description': 0, 'Total': 0},
    'Renew': {'Description': 0, 'Short Description': 0, 'Total': 0},
    'Remanufactured': {'Description': 0, 'Short Description': 0, 'Total': 0},
    'Recertified': {'Description': 0, 'Short Description': 0, 'Total': 0}
}

# Function to check if a condition word exists in a given string
def check_condition(string, condition):
    return condition.lower() in string.lower()

# Read the data file and process each line
with open(data_file_path, 'r') as data_file:
    for line in data_file:
        description, short_description = line.strip().split('|~|')

        for condition in product_conditions:
            if condition == 'Renew' and ('Renew' in description or 'Renew' in short_description):
                product_conditions[condition]['Description'] += 1
                product_conditions[condition]['Short Description'] += 1
                product_conditions[condition]['Total'] += 2
            else:
                if check_condition(description, condition):
                    product_conditions[condition]['Description'] += 1
                    product_conditions[condition]['Total'] += 1
                if check_condition(short_description, condition):
                    product_conditions[condition]['Short Description'] += 1
                    product_conditions[condition]['Total'] += 1

# Generate a JSON report
report = json.dumps(product_conditions, indent=4)

# Save the report to a JSON file
with open('product_condition_report.json', 'w') as report_file:
    report_file.write(report)

print("Product condition report generated and saved to 'product_condition_report.json'.")

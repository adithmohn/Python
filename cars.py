import csv
import os

# Specify the folder path where the CSV files are located
folder_path = '/home/adith/Documents/2cloud/python/'

# List all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Iterate through each CSV file in the folder
for csv_file in csv_files:
    # Get the full path of the CSV file
    selected_file = os.path.join(folder_path, csv_file)

    # Open the selected CSV file and read the header to determine the column names
    with open(selected_file, 'r') as input_csv:
        csv_reader = csv.DictReader(input_csv)
        fieldnames = csv_reader.fieldnames
        data = list(csv_reader)

    print(f"Processing CSV file: {csv_file}")

    # Check if 'car_name', 'ending_price', and 'fuel_type' are in the fieldnames (case insensitive)
    if 'car_name' in [name.lower() for name in fieldnames] and 'ending_price' in [name.lower() for name in fieldnames] and 'fuel_type' in [name.lower() for name in fieldnames]:
        user_choice = input("Choose an option:\n1. Enter car name\n2. Enter price range (0 to 10000000 for 0 to 10 crores)\n3. Filter by fuel type: ").strip().lower()

        if user_choice == '1':
            user_input = input("Enter the car name: ").strip().lower()
            matching_cars = [row for row in data if row['car_name'].lower() == user_input]

            if matching_cars:
                # Filter and write the matching car data to a CSV file
                with open('matching_car_data.csv', 'w', newline='') as output_csv:
                    csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(matching_cars)

                print(f"Data for the selected car(s) saved to 'matching_car_data.csv'")
            else:
                print("No car data found for the specified car name. Please check your spelling.")
        
        elif user_choice == '2':
            try:
                min_price = 0
                max_price = float(input("Enter the maximum price (0 to 10000000): "))
                
                if max_price < 0:
                    print("Please enter a non-negative maximum price.")
                elif max_price > 10000000:  # Cap the maximum price at 10 crores
                    print("No cars above 10 crores.")
                else:
                    matching_cars = [row for row in data if min_price <= float(row['ending_price']) <= max_price]
                    if matching_cars:
                        # Filter and write the matching car data to a CSV file
                        with open('matching_price_range_data.csv', 'w', newline='') as output_csv:
                            csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
                            csv_writer.writeheader()
                            csv_writer.writerows(matching_cars)

                        print(f"Data for cars within the specified price range saved to 'matching_price_range_data.csv'")
                    else:
                        print("No cars found within the specified price range.")
            except ValueError:
                print("Invalid input. Please enter a valid numerical value for the maximum price.")
        
        elif user_choice == '3':
            fuel_type_choice = input("Choose a fuel type:\n1. Diesel\n2. Petrol\n3. Both Diesel and Petrol: ").strip().lower()
            matching_cars = []

            if fuel_type_choice == '1':
                min_price = 0
                max_price = float(input("Enter the maximum price for Diesel cars (0 to 10000000): "))
                matching_cars = [row for row in data if row['fuel_type'].lower() == 'diesel' and min_price <= float(row['ending_price']) <= max_price]
            elif fuel_type_choice == '2':
                min_price = 0
                max_price = float(input("Enter the maximum price for Petrol cars (0 to 10000000): "))
                matching_cars = [row for row in data if row['fuel_type'].lower() == 'petrol' and min_price <= float(row['ending_price']) <= max_price]
            elif fuel_type_choice == '3':
                min_price = 0
                max_price = float(input("Enter the maximum price for both Diesel and Petrol cars (0 to 10000000): "))
                matching_cars = [row for row in data if row['fuel_type'].lower() in ['diesel', 'petrol'] and min_price <= float(row['ending_price']) <= max_price]

            if matching_cars:
                # Filter and write the matching car data to a CSV file
                with open('matching_fuel_type_data.csv', 'w', newline='') as output_csv:
                    csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(matching_cars)

                print(f"Data for cars within the specified fuel type and price range saved to 'matching_fuel_type_data.csv'")
            else:
                print("No cars found within the specified fuel type and price range.")
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3 to choose an option.")
    
    else:
        print(f"The required columns (car_name, ending_price, fuel_type) do not exist in the CSV file: {csv_file}. Please check the column/header names.")

# Find the least expensive car price and inform the user
if data:
    least_expensive_car = min(data, key=lambda x: float(x['ending_price']))
    least_expensive_car_name = least_expensive_car['car_name']
    least_expensive_car_price = least_expensive_car['ending_price']
    print(f"The least expensive car in the dataset is '{least_expensive_car_name}' with a price of {least_expensive_car_price}")
else:
    print("The dataset is empty.")

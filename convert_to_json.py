import csv
import json

def clean_price(price):
    # Remove currency symbol and commas, then convert to float
    return price.replace('$', '').replace(',', '').replace(' ', '').strip()

def convert_csv_to_json():
    # List to store all car entries
    cars_data = []
    
    # Try different encodings
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            # Read the CSV file
            with open('Cars Datasets 2025.csv', mode='r', encoding=encoding) as csv_file:
                # Create a CSV reader
                csv_reader = csv.DictReader(csv_file)
                
                # Process each row
                for row in csv_reader:
                    # Clean and structure the data
                    car_entry = {
                        "company": row["Company Names"].strip(),
                        "model": row["Cars Names"].strip(),
                        "specifications": {
                            "engine": {
                                "type": row["Engines"].strip(),
                                "capacity": row["CC/Battery Capacity"].strip(),
                                "horsePower": row["HorsePower"].strip(),
                                "torque": row["Torque"].strip()
                            },
                            "performance": {
                                "topSpeed": row["Total Speed"].strip(),
                                "acceleration": row["Performance(0 - 100 )KM/H"].strip()
                            }
                        },
                        "features": {
                            "fuelType": row["Fuel Types"].strip(),
                            "seats": row["Seats"].strip()
                        },
                        "price": clean_price(row["Cars Prices"])
                    }
                    cars_data.append(car_entry)
                
                # If we successfully read the file, break the loop
                break
        except UnicodeDecodeError:
            # If this encoding doesn't work, try the next one
            continue
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return
    
    # Write to JSON file
    with open('cars_data.json', 'w', encoding='utf-8') as json_file:
        json.dump({"cars": cars_data}, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    convert_csv_to_json()
    print("Conversion completed! Check cars_data.json for the result.")

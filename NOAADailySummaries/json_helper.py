import json
import pandas as pd
import os

# implement me
def read_all_json_files(JSON_ROOT):
    all_data = []  # List to store data from all JSON files
    
    # Loop through all files in the directory
    for filename in os.listdir(JSON_ROOT):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            file_path = os.path.join(JSON_ROOT, filename)
            
            # Read the JSON data
            with open(file_path, 'r') as file:
                data = json.load(file)
                data = data['results']
                
            # Add a 'source' column with the file name
            if isinstance(data, list):
                for record in data:
                    record['source'] = filename  # Add the source file name to each record
                all_data.extend(data)  # Add records from the current file to the list
            else:
                data['source'] = filename  # Add the source file name if it's a single object
                all_data.append(data)
    
    # Convert the list of data into a Pandas DataFrame
    df = pd.DataFrame(all_data)
    
    return df
import requests
import json
import time
import os
import time
from datetime import datetime

# Get the current working directory
cwd = os.getcwd()
current_date = datetime.now().strftime("%Y-%m-%d")
fpname = f"{cwd}/data/all_colleges_{current_date}.json"
    
def get_all_colleges(api_key, output_file=fpname):
    base_url = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
    all_results = []
    page = 0
    per_page = 100  # Maximum allowed by the API
    
    print("Starting data extraction...")

    while True:
        # Define parameters: school.operating=1 filters for active schools
        params = {
            "api_key": api_key,
            "page": page,
            "per_page": per_page,
            "school.operating": 1,
            # If you want specific fields, add: "fields": "id,school.name,latest.student.size"
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = data.get("results", [])
            metadata = data.get("metadata", {})
            
            if not results:
                break
                
            all_results.extend(results)
            
            total = metadata.get("total", 0)
            current_count = len(all_results)
            print(f"Downloaded page {page} ({current_count}/{total} colleges)...")

            # Check if we have reached the last page
            if current_count >= total:
                break
                
            page += 1
            
            # Brief sleep to respect rate limits if necessary
            time.sleep(0.1) 

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    # Write the final list to a single JSON file
    with open(output_file, "w") as f:
        json.dump(all_results, f, indent=4)
        
    print(f"Successfully dumped {len(all_results)} colleges to {output_file}")

def get_all_colleges_per_page(api_key, output_file=fpname):
    base_url = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
    page = 0
    per_page = 2  # Maximum allowed by the API
    
    print("Starting data extraction...")

    while True:
        all_results = []
        # Define parameters: school.operating=1 filters for active schools
        params = {
            "api_key": api_key,
            "page": page,
            "per_page": per_page,
            "school.operating": 1,
            # If you want specific fields, add: "fields": "id,school.name,latest.student.size"
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = data.get("results", [])
            metadata = data.get("metadata", {})
            
            if not results:
                break
                
            all_results.extend(results)
            
            total = metadata.get("total", 0)
            current_count = len(all_results)
            print(f"Downloaded page {page} ({current_count}/{total} colleges)...")

            # Check if we have reached the last page
            if current_count >= total:
                break
                
            page += 1
            
            # Write the final list to a single JSON file
            fps = fpname.split('.')
            fp_name =  f"{fps[0]}_{page}.json"
            with open(fp_name, "w") as f:
              json.dump(all_results, f, indent=4)
            
            # Brief sleep to respect rate limits if necessary
            time.sleep(0.1) 

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break
        
    print(f"Successfully dumped {len(all_results)} colleges to {output_file}")

# Usage
# get_all_colleges("YOUR_API_KEY")
# get_all_colleges_per_page("YOUR_API_KEY")

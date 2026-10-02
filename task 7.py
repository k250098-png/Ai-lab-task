import requests
import json
import csv

def experiment_pipeline():
    url = "https://dummyjson.com/products"
    params = {"limit": 10}
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        items = data.get("products", [])
        
        if not items:
            raise ValueError("Empty data returned from API")
            
        avg_price = sum(item.get("price", 0) for item in items) / len(items)
        category_counts = {}
        for item in items:
            cat = item.get("category", "unknown")
            category_counts[cat] = category_counts.get(cat, 0) + 1
            
        print(f"Average Price: {avg_price}")
        print(f"Category Distribution: {category_counts}")
        
        with open("pipeline_data.json", "w") as f:
            json.dump(items, f, indent=4)
            
        with open("pipeline_data.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=items[0].keys())
            writer.writeheader()
            writer.writerows(items)
                
    except requests.exceptions.Timeout:
        print("Pipeline Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Pipeline Error: Connection error.")
    except requests.exceptions.HTTPError:
        print("Pipeline Error: HTTP error occurred.")
    except ValueError as e:
        print(f"Pipeline Error: Invalid JSON Data - {e}")
    except IOError:
        print("Pipeline Error: Failed to write files.")
    else:
        print("Data retrieval and saving completed successfully.")
        try:
            with open("pipeline_data.json", "r") as f:
                saved_data = json.load(f)
                print(f"Verification Check: Read {len(saved_data)} items from JSON file.")
        except IOError:
            print("Verification Check: Could not read back the saved file.")
    finally:
        print("Pipeline execution process finalized.")

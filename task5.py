import requests
import json
import csv

def collect_nlp_data(query="technology"):
    url = f"https://dummyjson.com/quotes/search?q={query}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        quotes = data.get("quotes", [])
        extracted_data = [{"text": q.get("quote"), "author": q.get("author")} for q in quotes]
        
        for item in extracted_data:
            print(f"[{item['author']}] {item['text']}")
        
        with open("nlp_data.json", "w", encoding="utf-8") as f:
            json.dump(extracted_data, f, indent=4)
            
        with open("nlp_data.csv", "w", newline="", encoding="utf-8") as f:
            if extracted_data:
                writer = csv.DictWriter(f, fieldnames=["text", "author"])
                writer.writeheader()
                writer.writerows(extracted_data)
                
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
    except IOError as e:
        print(f"File handling error: {e}")

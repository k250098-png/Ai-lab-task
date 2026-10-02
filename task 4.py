import requests

def fetch_prediction_data(name_query):
    url = f"https://api.agify.io/?name={name_query}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        print(f"Input Data: {data.get('name')}")
        print(f"Prediction Result (Age): {data.get('age')}")
        print(f"Confidence/Count: {data.get('count')}")
        
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"API cannot provide the requested result: {e}")
    except ValueError:
        print("Error: Invalid JSON response received.")

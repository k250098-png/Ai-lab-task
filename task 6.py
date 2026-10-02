import requests

def demonstrate_rest_operations():
    base_url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        get_response = requests.get(f"{base_url}/1", timeout=5)
        print(f"GET Status: {get_response.status_code}")
        print(get_response.json())
        
        post_payload = {"title": "Vision Prediction", "body": "Input Image Data", "userId": 101}
        post_response = requests.post(base_url, json=post_payload, timeout=5)
        print(f"POST Status: {post_response.status_code}")
        print(post_response.json())
        
        put_payload = {"id": 1, "title": "Updated Prediction", "body": "Modified image parameters", "userId": 1}
        put_response = requests.put(f"{base_url}/1", json=put_payload, timeout=5)
        print(f"PUT Status: {put_response.status_code}")
        print(put_response.json())
        
        delete_response = requests.delete(f"{base_url}/1", timeout=5)
        print(f"DELETE Status: {delete_response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Network or API exception encountered: {e}")

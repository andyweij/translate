import httpx
import json

# User Config
API_KEY = "AFSO2045WHtNv4Fp0va7VMaeE16Ymy7q"
BASE_URL = "https://202.5.254.29:8080/v1/chat/completions"
MODEL = "Llama3.2-FFM-11B"

def test_raw_request():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": "Hello"}],
        "stream": False # Explicitly requesting JSON
    }
    
    print(f"Sending request to {BASE_URL}...")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    try:
        # Use verify=False to skip SSL check
        response = httpx.post(BASE_URL, json=payload, headers=headers, verify=False, timeout=30.0)
        
        print(f"\nStatus Code: {response.status_code}")
        print("\n--- Response Headers ---")
        for k, v in response.headers.items():
            print(f"{k}: {v}")
            
        print("\n--- Response Body ---")
        print(response.text)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_raw_request()

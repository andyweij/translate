import httpx
from langchain_openai import ChatOpenAI

# User's current config (Failing)
API_KEY = "AFSO2045WHtNv4Fp0va7VMaeE16Ymy7q"
BASE_URL_BAD = "https://202.5.254.29:8080/" # Missing /v1
BASE_URL_GOOD = "https://202.5.254.29:8080/v1" # Correct
MODEL = "Llama3.1-FFM-8B"

def test_config(name, base_url, verify_ssl):
    print(f"\n--- Testing {name} ---")
    print(f"URL: {base_url}")
    print(f"SSL Verify: {verify_ssl}")
    
    http_client = httpx.Client(verify=verify_ssl)
    
    try:
        llm = ChatOpenAI(
            api_key=API_KEY,
            base_url=base_url,
            model=MODEL,
            temperature=0,
            http_client=http_client,
            max_retries=1 # Don't wait too long
        )
        response = llm.invoke("Hello")
        print("SUCCESS!")
        print(response.content)
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    # 1. Replicate User's Error
    test_config("User Config (Failing)", BASE_URL_BAD, True)
    
    # 2. Proposed Fix
    test_config("Proposed Fix", BASE_URL_GOOD, False)

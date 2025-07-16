

import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Custom authentication class for token-based auth."""
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'Bearer {self.token}'
        return r

def main():
    base_url = 'http://127.0.0.1:5001'

    # 1. Custom Headers and Authentication
    print("\n--- 1. Custom Headers and Authentication ---")
    auth_response = requests.post(f'{base_url}/auth')
    token = auth_response.json()['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{base_url}/resource', headers=headers)
    print(response.json())

    # 2. URL Parameters
    print("\n--- 2. URL Parameters ---")
    params = {'q': 'test query'}
    response = requests.get(f'{base_url}/search', params=params)
    print(response.json())

    # 3. Request Bodies (POST and PUT)
    print("\n--- 3. Request Bodies ---")
    post_data = {'key': 'value'}
    response = requests.post(f'{base_url}/resource', json=post_data, headers=headers)
    print(response.json())
    put_data = {'new_key': 'new_value'}
    response = requests.put(f'{base_url}/resource', json=put_data, headers=headers)
    print(response.json())

    # 4. Diverse Content Types
    print("\n--- 4. Diverse Content Types ---")
    headers['Accept'] = 'application/xml'
    response = requests.get(f'{base_url}/content', headers=headers)
    print(response.text)

    # 5. Timeouts
    print("\n--- 5. Timeouts ---")
    try:
        response = requests.get(f'{base_url}/slow', timeout=2)
    except requests.exceptions.Timeout:
        print("Request timed out as expected.")

    # 6. Redirects
    print("\n--- 6. Redirects ---")
    response = requests.get(f'{base_url}/redirect')
    print(response.url)
    print(response.history)

    # 7. Error Handling
    print("\n--- 7. Error Handling ---")
    response = requests.get(f'{base_url}/error')
    print(f"Error response status code: {response.status_code}")
    response.raise_for_status() # This will raise an HTTPError if the status is 4xx or 5xx

if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


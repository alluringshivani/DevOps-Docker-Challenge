import requests

# Define the base URL of the API
BASE_URL = "http://localhost:8000"  # Update with the appropriate URL for your FastAPI server

# Function to test the '/hello' endpoint
def test_hello():
    response = requests.get(f"{BASE_URL}/hello")
    print("Response from /hello endpoint:")
    print(response.text)

# Function to test the '/user/add' endpoint
def test_add_user():
    user_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "full_name": "John Doe"
    }
    response = requests.post(f"{BASE_URL}/user/add", json=user_data)
    print("Response from /user/add endpoint:")
    print(response.json())

# Function to test the '/user/retrieve/{username}' endpoint
def test_retrieve_user(username):
    response = requests.get(f"{BASE_URL}/user/retrieve/{username}")
    print(f"Response from /user/retrieve/{username} endpoint:")
    print(response.json())

# Main function to run the tests
def main():
    test_hello()
    test_add_user()
    test_retrieve_user("john_doe")

if __name__ == "__main__":
    main()


import requests

def get_public_ip():
    try:
        # Use ipinfo.io API to get IP information
        response = requests.get('https://ipinfo.io/json')
        data = response.json()

        # Extract and print the IP address
        ip_address = data['ip']
        print(f"Your IP Address is: {ip_address}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Run the function
get_public_ip()

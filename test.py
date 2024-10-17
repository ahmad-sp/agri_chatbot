import requests
import certifi

def check_ssl_certificate(url):
    try:
        response = requests.get(url, verify=certifi.where())
        print("SSL certificate is valid.")
    except requests.exceptions.SSLError as e:
        print(f"SSL certificate is not valid: {e}")

check_ssl_certificate("https://api.generativeai.com")
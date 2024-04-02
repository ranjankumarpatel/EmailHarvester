import requests

# Set up the proxy to use Tor's SOCKS proxy
proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

# Make a request through the Tor network
response = requests.get('http://httpbin.org/ip', proxies=proxies)
print(response.text)

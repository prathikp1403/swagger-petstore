import requests

def extract_endpoints(url):
    response = requests.get(url)
    data = response.json()
    for path in data.get("paths", {}):
        print(path)

if __name__ == "__main__":
    swagger_url = "https://petstore.swagger.io/v2/swagger.json"
    extract_endpoints(swagger_url)

import requests

# Replace with your actual API key
api_key = "678ef97c72b14973bc93101457789383"
url = f"https://newsapi.org/v2/top-headlines/sources?apiKey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    
    if 'sources' in data:
        for source in data["sources"]:
            print(f"{source['id']} - {source['name']}")
    else:
        print("No sources found or invalid response format.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

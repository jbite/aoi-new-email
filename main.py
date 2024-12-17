import requests
from key import key

api_Key = key.api_Key
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-11-17&sortBy=publishedAt&apiKey={api_Key}"

#make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article["title"])
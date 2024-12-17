import requests
from key import key
import send_email
api_Key = key.api_Key
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-11-17&sortBy=publishedAt&apiKey={api_Key}"

#make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
title = []
for article in content['articles']:
    title.append(article["title"])

sender_email = key.email
sender_password = key.email_pass 
recipient_email = key.email
subject = "News for Tesla"
body = title[0]

send_email.send_email(sender_email, sender_password, recipient_email, subject, body)
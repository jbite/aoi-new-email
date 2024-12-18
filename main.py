import requests
from key import key
import send_email
from datetime import datetime, timedelta

def get_date_before_days(days):
  """
  Calculates the date 'days' before today.

  Args:
    days: The number of days to go back.

  Returns:
    A datetime object representing the date 'days' before today.
  """
  today = datetime.today()
  past_date = today - timedelta(days=days)
 
  return past_date

api_Key = key.api_Key
topic = input("Please type the topic you want to receive: ")
numberNews = int(input("How many news you want to receive?: "))
fromday = get_date_before_days(30)

url = f"https://newsapi.org/v2/everything?q={topic}&from={fromday}&sortBy=publishedAt&apiKey={api_Key}&language=zh"

#make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
body = ""
# Add news to email
for article in content['articles'][:numberNews]:
    if len(article['title']) > 0:
        body = body + f"Title: {article['title']}\nContent: {article['description']}\nLink: {article['url']}\n==" + 2*"\n"

# Access the article titles and description
# Send email to yourself
sender_email = key.email
sender_password = key.email_pass 
recipient_email = key.email
subject = f"News for {topic}"

send_email.send_email(sender_email, sender_password, recipient_email, subject, body)
import requests
from twilio.rest import Client


stock = "TSLA"
company = "Tesla Inc"

endpoint = "https://www.alphavantage.co/query"
news_ep = "https://newsapi.org/v2/everything"

api_key = "x"


twilio_sid = "x"
twilio_token = "x"


stk_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock,
    "apikey": api_key,

}
print(str(perc)+"%")

if abs(perc)>=.5:
    news_params = {
        "apiKey": "x",
        "qinTitle": company,
    }

    resp2 = requests.get(news_ep, params=news_params)
    articles = resp2.json()["articles"][:1]

    msgs = [f"{stock}:{emoji}{perc}%\nHeadline:{v['title']}\nBrief:{v['description']}" for v in articles]
    client = Client(twilio_sid, twilio_token)

    for msg in msgs:
        msg = client.messages \
            .create(
                body=msg,
                from_="+x",
                to="+x"
            )
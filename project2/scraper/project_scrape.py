from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

accounts=['NRA','CDCEmergency','netflix']

def tweets_to_csv(account):
    url=f'https://twitter.com/{account}'
    html = rq.get(url) 
    soup = bs(html.text, 'html.parser')
    tweets=list(soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"))
    tweet_list=[]
    for x in tweets:
        tweet_list.append(str(x.get_text()))
    tweets_df=pd.DataFrame({account:tweet_list})
    tweets_df.to_csv(r'C:\Users\phili\Documents\GitHub\project2\tweet_csvs\{}_tweets.csv'.format(account), index=False)

for account in accounts:
    tweets_to_csv(account)
    

    
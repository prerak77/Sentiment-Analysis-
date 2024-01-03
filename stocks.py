# Import libraries
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urllib.request import urlopen, Request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
import nltk
nltk.download('vader_lexicon')

# list of stocks to extract sentiment data
n = 3
tickers = ['AAPL', 'TSLA', 'AMZN']

# Get Data
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
finwiz_url = 'https://finviz.com/quote.ashx?t='
news_tables = {}

for ticker in tickers:
    url = finwiz_url + ticker
    req = Request(url=url, headers=headers)
    resp = urlopen(req)
    html = BeautifulSoup(resp, features="lxml")
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table


"""
<tr class="cursor-pointer has-label"
    onclick="trackAndOpenNews(event, 'InvestorPlace', 'https://investorplace.com/2023/12/buy-apple-stock-in-the-down-months-youll-be-glad-you-did/');">
    <td width="130" align="right">
        08:34AM
    </td>
    <td align="left">
        <div class="news-link-container">
            <div class="news-link-left">
                <a class="tab-link-news"
                    href="https://investorplace.com/2023/12/buy-apple-stock-in-the-down-months-youll-be-glad-you-did/"
                    target="_blank" rel="nofollow">Buy Apple Stock
                    in the Down Months. You'll Be Glad You Did.</a>
            </div>
            <div class="news-link-right">
                <span>(InvestorPlace)</span></div>
        </div>
    </td>
    </tr>




"""
# this is just for printing out the main headlines
# related to the company
try:
    for ticker in tickers:
        df = news_tables[ticker]
        df_tr = df.findAll('tr')
        print('\n')
        print('Recent News Headlines for {}: '.format(ticker))

        for i, table_row in enumerate(df_tr):
            a_text = table_row.a.text
            td_text = table_row.td.text
            td_text = td_text.strip()
            print(a_text, '(', td_text, ')')
            if i == n-1:
                break
except KeyError:
    pass


# Iterate through the news
parsed_news = []
for file_name, news_table in news_tables.items():
    for x in news_table.findAll('tr'):
        text = x.a.get_text()
        date_scrape = x.td.text.split()

        if len(date_scrape) == 1:
            time = date_scrape[0]

        else:
            date = date_scrape[0]
            time = date_scrape[1]

        ticker = file_name.split('_')[0]

        parsed_news.append([ticker, date, time, text])


# Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()

columns = ['Ticker', 'Date', 'Time', 'Headline']
news = pd.DataFrame(parsed_news, columns=columns)
scores = news['Headline'].apply(analyzer.polarity_scores).tolist()
breakpoint()
df_scores = pd.DataFrame(scores)
news = news.join(df_scores, rsuffix='_right')

# View Data

unique_ticker = news['Ticker'].unique().tolist()
news_dict = {name: news.loc[news['Ticker'] == name] for name in unique_ticker}

values = []
for ticker in tickers:
    dataframe = news_dict[ticker]
    dataframe = dataframe.set_index('Ticker')
    dataframe = dataframe.drop(columns=['Headline'])
    print('\n')
    print(dataframe.head())

    mean = round(dataframe['compound'].mean(), 3)
    values.append(mean)

df = pd.DataFrame(list(zip(tickers, values)), columns=[
                  'Ticker', 'Mean Sentiment'])
df = df.set_index('Ticker')
df = df.sort_values('Mean Sentiment', ascending=False)
print('\n')
print(df)

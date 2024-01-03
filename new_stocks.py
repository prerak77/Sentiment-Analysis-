'''##############  libraries used  #########################'''
from dotenv import load_dotenv
import os
import json
import urllib.request
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
'''########################################################'''


# Loads the API key used to access the Gnews API for
# access to all archived new artilces for the past 50 years
load_dotenv()
api_key = os.environ.get("API_KEY")


"""Parameters used to make the API calls, this includes 3 fundamental attributes including:-
        1) the Company name
        2) the time frame from which the articles are needed(start_date and end_date)
        3) the language of the articles
        4) the contry from which the new should originate
        5) Numer of articles tat need to be called that belong to the specified time frame"""
company = "APPLE"
start_date = "2022-08-1"
end_date = "2022-08-30"
language = "en"
country = "us"
no_articles = "5"


url = f"https://gnews.io/api/v4/search?q={company}&apikey={api_key}&from={start_date}&to={end_date}&lang={language}&country={country}&max={no_articles}"


with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))
    # all the articles recieved from the API call
    articles = data["articles"]

    # creats a new dataframe for that stores the data with form
    """ Ticker       Date                                           Headline    neg    neu    pos  compound
        0  APPLE  2022-08-1  Start your journal today! Apple Support video ...  0.000  0.842  0.158    0.4574
        1  APPLE  2022-08-1  This sweet new AirPods Pro 2 deal (with USB-C)...  0.075  0.751  0.173    0.4019
    """

    columns = ['Ticker', 'Date', 'Headline']
    news = pd.DataFrame(columns=columns)

    for i in range(len(articles)):
        # articles[i].title
        # extracting just the headline of the articles
        headline = articles[i]['title']

        # Data to add
        data_to_add = [company, start_date,
                       headline]

        # Add data to DataFrame
        news.loc[len(news)] = data_to_add

# Impliments a sentiment analysis algorthm based on vedar_lexcon to extract the sentiment of the news headline
analyzer = SentimentIntensityAnalyzer()
scores = news['Headline'].apply(analyzer.polarity_scores).tolist()

# adding the analysis to the dataframe
df_scores = pd.DataFrame(scores)
news = news.join(df_scores, rsuffix='_right')
print(news.head())

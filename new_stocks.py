'''##############  libraries used  #########################'''
import calendar
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
import os
import json
import urllib.request
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
'''########################################################'''


"""##### Variables #######"""
compaies_lst = ["AMZN"]      # Add stock tickers to this list
month = "01"                 # enter as number eg:- may ----> 05
year = "2022"
"""#######################"""


# Loads the API key used to access the Gnews API for
# access to all archived new artilces for the past 50 years
load_dotenv()
api_key = os.environ.get("API_KEY")


# function to return all teh dates in a given month and year
def get_dates_in_month(year, month):
    cal = calendar.monthcalendar(year, month)
    dates_in_month = [day for week in cal for day in week if day != 0]
    return dates_in_month

# function to return the next date of teh current date


def get_next_date(current_date):
    # Convert the input date string to a datetime object
    current_date = datetime.strptime(current_date, '%Y-%m-%d')

    # Calculate the next date by adding one day
    next_date = current_date + timedelta(days=1)

    # Convert the next date back to a string
    next_date_str = next_date.strftime('%Y-%m-%d')

    return next_date_str


"""
Parameters used to make the API calls, this includes 3 fundamental attributes including:-
        1) the Company name
        2) the time frame from which the articles are needed(start_date and end_date)
        3) the language of the articles
        4) the contry from which the new should originate
        5) Numer of articles tat need to be called that belong to the specified time frame
"""

for company in compaies_lst:
    company = company
    dates = get_dates_in_month(int(year), int(month))
    new_data = []
    for date in dates:
        start_date = f"{year}-{month}-{date}"
        end_date = get_next_date(start_date)
        language = "en"
        country = "us"
        no_articles = "50"

        # add a 1 sec delay to avoid the too many requests error
        time.sleep(1)

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

        """
        To extract more data from the sentiment analysis this code finds 
        1) the mean of all the sentiments of the news headline for the specified time frame
        2)the highest sentiment of the day
        3)the lowest sentiment of the day"""
        average_sen = news['compound'].mean()
        print("Average Compound:", average_sen)

        largest_sen = news['compound'].max()
        print("Largest Compound Value:", largest_sen)

        smallest_sen = news['compound'].min()
        print("Smallest Compound Value:", smallest_sen)

        # Creating a new dataframe that will store the mean,max and min sentiment over a specific time frame

        new_data.append([company, start_date,
                         average_sen, largest_sen, smallest_sen])

    columns = ['Ticker', 'Date', 'Mean', "Max", "Min"]
    stock_sen = pd.DataFrame(new_data, columns=columns)

    csv_file_path = f'{company}_{month}_{year}_sent.csv'
    stock_sen.to_csv(csv_file_path, index=False)

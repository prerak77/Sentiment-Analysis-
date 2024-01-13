# Stock Sentiment Analysis

## Project Overview

This project focuses on extracting news headlines related to a specific company within a designated time frame. The primary objective is to perform sentiment analysis on the news headlines, determining whether they convey a positive, negative, or neutral sentiment towards the company.

The output presents a structured table with key information, including the company's ticker, the publication date of the news, the headline itself, and sentiment analysis metrics. The sentiment metrics are derived from a compound sentiment score, providing an overall rating for each news article.

## Output Format

The final output table includes the following columns:

- **Ticker:** The stock ticker symbol of the company.
- **Date:** The publication date of the news headlines.
- **Headline:** The news headline related to the company.
- **neg, neu, pos:** Individual sentiment scores representing the negativity, neutrality, and positivity of the headline.
- **compound:** The compounded sentiment score, offering a specific rating for each news article.

## Example Output

| Date       | Open               | High               | Low                | Close              | Adj Close          | Volume   | Mean   | Max    | Min     |
| ---------- | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | -------- | ------ | ------ | ------- |
| 2021-01-04 | 163.5              | 163.60000610351562 | 157.2010040283203  | 159.3314971923828  | 159.3314971923828  | 88228000 | 0.4415 | 0.8555 | 0.0     |
| 2021-01-05 | 158.30050659179688 | 161.16900634765625 | 158.2530059814453  | 160.92550659179688 | 160.92550659179688 | 53110000 | 0.3561 | 0.8658 | 0.1779  |
| 2021-01-06 | 157.32400512695312 | 159.87550354003906 | 156.55799865722656 | 156.91900634765625 | 156.91900634765625 | 87896000 | 0.4162 | 0.7096 | 0.0     |
| 2021-01-07 | 157.85000610351562 | 160.427001953125   | 157.75             | 158.10800170898438 | 158.10800170898438 | 70290000 | 0.3094 | 0.8555 | -0.7845 |
| 2021-01-08 | 159.0              | 159.53199768066406 | 157.11000061035156 | 159.13499450683594 | 159.13499450683594 | 70754000 | 0.3158 | 0.7351 | 0.0     |
| 2021-01-11 | 157.40049743652344 | 157.81900024414062 | 155.5              | 155.7104949951172  | 155.7104949951172  | 73668000 | 0.3149 | 0.7096 | -0.0516 |
| 2021-01-12 | 156.0              | 157.10699462890625 | 154.3000030517578  | 156.04150390625    | 156.04150390625    | 70292000 | 0.0772 | 0.5106 | -0.4939 |
| 2021-01-13 | 156.4219970703125  | 159.49749755859375 | 156.10400390625    | 158.29449462890625 | 158.29449462890625 | 66424000 | 0.2294 | 0.7096 | -0.5423 |
| 2021-01-14 | 158.37600708007812 | 158.89999389648438 | 156.0294952392578  | 156.37350463867188 | 156.37350463867188 | 61418000 | 0.1158 | 0.7096 | -0.296  |

## Sentiment Analysis

The key metric for sentiment comparison is the `compound` score. This score provides a specific rating for each news article, and it can be averaged across all articles for a particular day to obtain the stock sentiment for that day.

## How to Use

### 1. Clone the Codebase

Clone the repository onto your local machine using the following command:

```bash
git clone https://github.com/prerak77/Sentiment-Analysis-
```

### 2. Install Dependencies

Navigate to the project directory and install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

The primary dependencies include:

- [yfinance](https://pypi.org/project/yfinance/)
- [pandas](https://pypi.org/project/pandas/)
- [nltk](https://pypi.org/project/nltk/)

### 3. Adjust Parameters

In the `new_stocks.py` file, there are three main parameters: `company_name` and `year` for sentiment analysis. Modify these parameters according to the company and year of interest.

### 4. Create an .env File

This project uses the G News API for collecting news articles. Obtain your API token by creating an account at [G News](https://gnews.io/), and copy the token from the dashboard. Create a new `.env` file in the root directory and paste the API token as follows:

```env
API_TOKEN_1=your-api-token
```

### 5. Run the Script

Execute the `main.py` file to perform sentiment analysis and generate a CSV file with the necessary data:

```bash
python main.py
```

This script will collect news articles, perform sentiment analysis, and save the results in a CSV file.

Feel free to explore and customize the code to suit your specific requirements!

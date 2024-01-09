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

```plaintext
  Ticker       Date                                           Headline    neg    neu    pos  compound
0  APPLE  2022-08-1  Start your journal today! Apple Support video ...  0.000  0.842  0.158    0.4574
1  APPLE  2022-08-1  This sweet new AirPods Pro 2 deal (with USB-C)...  0.075  0.751  0.173    0.4019
2  APPLE  2022-08-1  Apple TV+ spy drama Slow Horses is coming back...  0.000  1.000  0.000    0.0000
3  APPLE  2022-08-1  This Apple Watch Ultra case expands your color...  0.000  0.851  0.149    0.1027
4  APPLE  2022-08-1    AirPods Pro 2 with USB-C hits lowest price ever  0.271  0.729  0.000   -0.3818
```

## Sentiment Analysis

The key metric for sentiment comparison is the `compound` score. This score provides a specific rating for each news article, and it can be averaged across all articles for a particular day to obtain the stock sentiment for that day.

## How to Use

1. **Extract News Headlines:**
   Use the provided code to extract news headlines for a specific company within a designated time frame.

2. **Perform Sentiment Analysis:**
   Analyze the sentiment of each news headline using the compound sentiment score.

3. **Interpret Results:**
   Review the output table to understand the overall sentiment towards the company on each analyzed day.

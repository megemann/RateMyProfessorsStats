import pandas as pd
from textblob import TextBlob

def normalize_polarity(polarity_value, original_mean=0.17367111985615713, original_std=0.27919562061398756, 
                      normalized_mean=-0.0004245127633839519, normalized_std=0.9955001068123789):
    """
    Normalize polarity values using the pre-calculated statistics
    """
    # Z-score normalization
    z_score = (polarity_value - original_mean) / original_std
    # Adjust to desired distribution
    normalized_value = z_score * normalized_std + normalized_mean
    return normalized_value

def get_sentiment(reviews):
    reviews = reviews[reviews['comment'].notna()]
    #lets do a little example with the first review
    reviews['sentiment'] = reviews['comment'].apply(lambda x: TextBlob(x).sentiment)

    # Extract polarity and subjectivity from sentiment tuples
    reviews['polarity'] = reviews['sentiment'].apply(lambda x: x[0])
    reviews['subjectivity'] = reviews['sentiment'].apply(lambda x: x[1])

    reviews['normalized_polarity'] = reviews['polarity'].apply(normalize_polarity)
    return reviews[['datetime', 'normalized_polarity', 'polarity', 'subjectivity']]

def avg_sentiment_over_time(df):
    df = df.sort_values('datetime')
    df['avg_sentiment'] = df['normalized_polarity'].expanding().mean()
    return df[['datetime', 'avg_sentiment']]

def rolling_avg_sentiment(df, window_years=1):
    window_days = f"{365 * window_years}D"
    df = df.sort_values('datetime')
    # Calculate rolling average with specified window
    df = df.set_index('datetime')  # Set datetime as index
    df['rolling_avg_sentiment'] = df['normalized_polarity'].rolling(window=window_days, min_periods=1).mean()
    df = df.reset_index()  # Reset index
    return df[['datetime', 'rolling_avg_sentiment']]

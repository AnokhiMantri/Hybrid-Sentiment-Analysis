import pandas as pd

# Load dataset
df = pd.read_csv("data/twitter_airline_sentiment_clean.csv")

print("Columns:")
print(df.columns)

print("\nSentiment Distribution:")
print(df['airline_sentiment'].value_counts())

print("\nFirst 5 rows:")
print(df.head())

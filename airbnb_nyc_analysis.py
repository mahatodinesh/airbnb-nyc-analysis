
# Import necessary libraries
import pandas as pd

# Load the datasets
df_price = pd.read_csv("data/airbnb_price.csv")
df_room_type = pd.read_excel("data/airbnb_room_type.xlsx")
df_review = pd.read_csv("data/airbnb_last_review.tsv", sep='\t')

# Merge the datasets on 'listing_id'
df_combined = df_price.merge(df_room_type, on="listing_id").merge(df_review, on="listing_id")

# View the first few rows of the combined dataset
print(df_combined.head())

# Get basic summary statistics of price by room type
room_price_summary = df_combined.groupby("room_type")["price"].describe()
print("\nPrice Summary by Room Type:")
print(room_price_summary)

# Find the top 5 most expensive listings
top_5_expensive = df_combined.sort_values(by="price", ascending=False).head(5)
print("\nTop 5 Most Expensive Listings:")
print(top_5_expensive[["listing_id", "price", "nbhood_full", "room_type"]])

# Count of listings by neighborhood
nbhood_counts = df_combined["nbhood_full"].value_counts().head(10)
print("\nTop 10 Neighborhoods by Listing Count:")
print(nbhood_counts)

# Check how many listings were reviewed in the last year (2019)
df_combined["last_review"] = pd.to_datetime(df_combined["last_review"], errors='coerce')
recent_reviews = df_combined[df_combined["last_review"].dt.year == 2019]
print(f"\nTotal listings reviewed in 2019: {recent_reviews.shape[0]}")

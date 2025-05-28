# Airbnb NYC Analysis

This project explores the Airbnb rental market in New York City using data from multiple file formats: CSV, TSV, and Excel. The goal is to combine and analyze data from different sources to gain insights into pricing, room types, and host activity across NYC neighborhoods.

## 📁 Dataset Overview

The dataset includes the following three files located in the `data/` directory:

- `airbnb_price.csv`  
  Contains prices and neighborhood information.
  - `listing_id`: Unique listing ID  
  - `price`: Nightly price in USD  
  - `nbhood_full`: Borough and neighborhood  

- `airbnb_room_type.xlsx`  
  Contains descriptions and room types.
  - `listing_id`: Unique listing ID  
  - `description`: Listing description  
  - `room_type`: Shared, Private, or Entire home  

- `airbnb_last_review.tsv`  
  Contains host names and last review dates.
  - `listing_id`: Unique listing ID  
  - `host_name`: Host’s name  
  - `last_review`: Date of last review  

## 🛠️ Technologies Used

- Python
- Pandas
- Jupyter Notebook (optional for visualization/testing)

## 📊 Features

- Load and merge data from CSV, TSV, and Excel formats
- Clean and explore listings by price, room type, and activity
- Prepare the data for further analysis or visualization

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/airbnb-nyc-analysis.git
   cd airbnb-nyc-analysis

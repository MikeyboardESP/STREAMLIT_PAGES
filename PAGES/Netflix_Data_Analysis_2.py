# the libraries you have to use
import pandas as pd
import matplotlib.pyplot as plt

# Some extra libraries for date conversions and build the webapp
import streamlit as st


# ----- Page configs -----
st.set_page_config(
    page_title="<Miguel Martin Oviedo > Portfolio",
    page_icon="📊",
)

# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.write("Interactive Project to load a dataset with information about Netflix Movies and Series, extract some insights using Pandas and displaying them with Matplotlib.")
    st.write("Data extracted from: https://www.kaggle.com/datasets/shivamb/netflix-shows (with some cleaning and modifications)")

# ----- Title of the page -----
st.title("🎬 Netflix Data Analysis")
st.divider()

# ----- Loading the dataset -----

@st.cache
def load_data():
    data_path = "data/netflix_titles.csv"
    movies_df = pd.read_csv(data_path, index_col="show_id")  # Ex 2.1: Load the dataset using Pandas, use the data_path variable and set the index column to "show_id"
    return movies_df

movies_df = load_data()

# Displaying the dataset in an expandable table
with st.expander("Check the complete dataset:"):
    st.dataframe(movies_df)

# ----- Extracting some basic information from the dataset -----

# Ex 2.2: What is the min and max release years?
min_year = movies_df['release_year'].min()
max_year = movies_df['release_year'].max()

# Ex 2.3: How many director names are missing values (NaN)?
num_missing_directors = movies_df['director'].isnull().sum()

# Ex 2.4: How many different countries are there in the data?
n_countries = movies_df['country'].nunique()

# Ex 2.5: How many characters long are on average the title names?
avg_title_length = movies_df['title'].str.len().mean()

# ----- Displaying the extracted information metrics -----

st.write("##")
st.header("Basic Information")

cols1 = st.columns(5)
cols1[0].metric("Min Release Year", min_year)
cols1[1].metric("Max Release Year", max_year)
cols1[2].metric("Missing Dir. Names", num_missing_directors)
cols1[3].metric("Countries", n_countries)
cols1[4].metric("Avg Title Length", round(avg_title_length, 2))

# ----- Pie Chart: Top year producer countries -----

st.write("##")
st.header("Top Year Producer Countries")

cols2 = st.columns(2)
year = cols2[0].number_input("Select a year:", min_value=min_year, max_value=max_year, value=2005)

# Ex 2.6: For a given year, get the Pandas Series of how many movies and series combined were made by every country, limit it to the top 10 countries.
if st.button("Calculate Top 10 Countries"):
    top_10_countries = movies_df[movies_df['release_year'] == year]['country'].value_counts().head(10)
    if not top_10_countries.empty:
        fig = plt.figure(figsize=(8, 8))
        plt.pie(top_10_countries, labels=top_10_countries.index, autopct="%.2f%%")
        plt.title(f"Top 10 Countries in {year}")
        st.pyplot(fig)
    else:
        st.write("No data available for the selected year.")

# ----- Line Chart: Avg duration of movies by year -----

st.write("##")
st.header("Avg Duration of Movies by Year")

# Ex 2.7: Make a line chart of the average duration of movies (not TV shows) in minutes for every year across all the years.
if st.button("Calculate Avg Duration"):
    movies_avg_duration_per_year = movies_df[movies_df['type'] == 'Movie'].groupby('release_year')['duration'].mean()
    if not movies_avg_duration_per_year.empty:
        fig = plt.figure(figsize=(9, 6))
        plt.plot(movies_avg_duration_per_year.index, movies_avg_duration_per_year.values)
        plt.xlabel("Year")
        plt.ylabel("Average Duration (minutes)")
        plt.title("Average Duration of Movies Across Years")
        st.pyplot(fig)
    else:
        st.write("No movie data available.")

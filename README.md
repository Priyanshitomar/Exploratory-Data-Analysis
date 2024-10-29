# Exploratory-Data-Analysis


Netflix Movie Ratings - Exploratory Data Analysis (EDA)

Project Overview

This project is an exploratory data analysis (EDA) of a Netflix movie ratings dataset. The objective is to analyze rating patterns, identify trends across genres and years, and uncover any interesting insights within the data.

Dataset

The dataset used in this project is from Kaggle and includes:

movie_title: Title of the movie

rating: User rating for each movie

genre: Movie genre

release_year: Year the movie was released

duration: Duration of the movie in minutes


Analysis Steps

This analysis was structured as follows:

1. Data Loading and Overview

Loaded the dataset using Pandas.

Explored the shape, columns, data types, and previewed the first few rows.

Summarized numerical columns to understand basic statistics.


2. Data Cleaning

Checked for missing values and handled any that were present.

Removed duplicate entries if any were found.


3. Exploratory Data Analysis (EDA)

Ratings Distribution:

Plotted a histogram of ratings to see the general trend. Most ratings were clustered around 4.0, indicating positive user ratings overall.


Outlier Analysis:

Used a box plot to detect outliers in ratings, identifying movies with exceptionally high or low ratings for further exploration.


Genre Analysis:

Created bar plots and box plots to visualize the distribution of ratings across genres.

Found that genres like Drama and Action generally had higher ratings.


Release Year Analysis:

Analyzed the distribution of release years and their relation to ratings, showing that older movies had more varied ratings.


Correlation Analysis:

Generated a correlation heatmap to identify relationships between numeric columns. There was no significant correlation between ratings and other numeric variables.



Key Insights

Positive Rating Trend: Most Netflix movies have ratings around 4.0.

Genre Impact: Some genres, particularly Drama and Action, have slightly higher ratings.

Outliers: A few movies had very low ratings, which could be analyzed to understand audience feedback.


Libraries Used

Pandas: For data manipulation and analysis.

Matplotlib & Seaborn: For visualizations.


How to Run the Code

1. Clone this repository.


2. Install the required libraries:

pip install pandas matplotlib seaborn


3. Run the Python notebook or script file to execute the analysis and view the plots.



Future Work

Investigate reasons for low ratings in certain movies or genres.

Explore if other factors (e.g., movie duration) impact user ratings.




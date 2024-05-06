import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('movies.csv')

# 1. Top voted movies
top_voted = data.sort_values(['No_of_Votes'], ascending = False)
fig,axs=plt.subplots(figsize=(15,5))
g=sns.barplot(x=top_voted['Series_Title'][:7],y=top_voted['No_of_Votes'][:7], palette = 'hls')
g.set_title("Top Voted Movies", weight = "bold")
plt.show()

# 2. Top rated movies
imdb = data.sort_values(['IMDB_Rating'], ascending = False)
fig,axs=plt.subplots(figsize=(15,5))
g=sns.barplot(x=imdb['Series_Title'][:7],y=imdb['IMDB_Rating'][:7], palette = 'hls')
g.set_title("Top Rated Movies", weight = "bold")
plt.show()

# 3. genre movies
genre = data.sort_values(['Genre'], ascending = False)
fig,axs=plt.subplots(figsize=(15,5))
plt.pie(
    genre['Genre'].value_counts(),
    labels = genre['Genre'].value_counts().index,
    autopct = '%1.1f%%'
)
plt.title("Genre", weight = "bold")                     

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

def movie(nogui=False, movielenspath=''):
    user_columns = ['user_id', 'age', 'gender']
    users = pd.read_csv(movielenspath + 'movie_lens/u.user', sep='|', names=user_columns, usecols=range(3))

    rating_columns = ['user_id', 'movie_id', 'rating']
    ratings = pd.read_csv(movielenspath + 'movie_lens/u.data', sep='\t', names=rating_columns,  usecols=range(3))

    movie_columns = ['movie_id', 'title']
    movies = pd.read_csv(movielenspath + 'movie_lens/u.item', sep='|', names=movie_columns, usecols=range(2), encoding="iso-8859-1")

    # create one merged DataFrame
    movie_ratings = pd.merge(movies, ratings)
    movie_data = pd.merge(movie_ratings, users)

    # Top rated movies
    print("Top rated movies (overall): \n" , movie_data.groupby('title').size().sort_values(ascending=False)[:20])
    print("\n")


if __name__ == "__main__":
    movie()
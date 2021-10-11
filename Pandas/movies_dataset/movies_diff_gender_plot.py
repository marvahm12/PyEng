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
    
    ratings_by_title = movie_data.groupby('title').size()
    popular_movies = ratings_by_title.index[ratings_by_title >= 250]

    ratings_by_gender = movie_data.pivot_table('rating', index='title',columns='gender')

    ratings_by_gender = ratings_by_gender.loc[popular_movies]


    ratings_by_gender['diff'] = ratings_by_gender['M'] - ratings_by_gender['F']
    gender_diff = ratings_by_gender['diff']

    #print("Difference by gender \n", ratings_by_gender.head())
    #print("\n")

    gender_diff = ratings_by_gender['diff']
    # Only get absolute values
    gender_diff = abs(gender_diff)
    #Sort by size
    gender_diff.sort_values(inplace=True, ascending = False)
    # Show top 10 differences
    gender_diff[:10].plot(kind='barh')
    plt.show()
    plt.savefig('output/plot.png')


  

if __name__ == "__main__":
    movie()
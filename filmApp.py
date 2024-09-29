import streamlit as st
import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

# Veri dosyalarını yükleme
movies = pd.read_csv('/Users/berkaybakac/Downloads/movie.csv')
ratings = pd.read_csv('/Users/berkaybakac/Downloads/rating.csv')

# Puanlar veri setinden küçük bir alt küme oluşturma
ratings_small = ratings.sample(100000, random_state=42)

# Puanlar veri setini Surprise kütüphanesi için hazırlama
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings_small[['userId', 'movieId', 'rating']], reader)

# Veri setini eğitim ve test seti olarak ayırma
trainset, testset = train_test_split(data, test_size=0.2)

# SVD modeli oluşturma ve eğitme
model = SVD()
model.fit(trainset)

# Kullanıcıya öneri yapma fonksiyonu
def get_user_recommendations(user_id, model, movies, ratings, num_recommendations=10):
    # Kullanıcının daha önce puan verdiği filmleri alalım
    watched_movies = ratings[ratings['userId'] == user_id]['movieId'].tolist()
    
    # Kullanıcının henüz puanlamadığı filmleri bulma
    all_movies = movies['movieId'].tolist()
    unseen_movies = [movie for movie in all_movies if movie not in watched_movies]
    
    # Henüz puanlanmamış filmler için tahmin yapma
    predictions = [model.predict(user_id, movie_id) for movie_id in unseen_movies]
    
    # Tahminleri puanlara göre sırala
    predictions = sorted(predictions, key=lambda x: x.est, reverse=True)
    
    # En iyi tahmin edilen filmleri al ve başlıklarını döndür
    top_predictions = predictions[:num_recommendations]
    recommended_movie_ids = [pred.iid for pred in top_predictions]
    
    return movies[movies['movieId'].isin(recommended_movie_ids)][['title', 'genres']]

# Kullanıcının daha önce izlediği filmleri gösterme fonksiyonu
def get_watched_movies(user_id, ratings, movies):
    watched_movies_ids = ratings[ratings['userId'] == user_id]['movieId'].tolist()
    watched_movies = movies[movies['movieId'].isin(watched_movies_ids)][['title', 'genres']]
    return watched_movies

# Streamlit arayüzü
st.title("Film Öneri Sistemi")

# Kullanıcı ID'si girdisi
user_id = st.number_input("Kullanıcı ID'si girin:", min_value=1, max_value=138493)

if st.button("Öneri Al"):
    # Kullanıcının izlediği filmleri gösterme
    watched_movies = get_watched_movies(user_id=user_id, ratings=ratings_small, movies=movies)
    st.subheader("Daha önce izlediğiniz filmler:")
    st.write(watched_movies)

    # Kullanıcıya öneriler yapma
    recommendations = get_user_recommendations(user_id=user_id, model=model, movies=movies, ratings=ratings_small)
    st.subheader("Sizin için önerilen filmler:")
    st.write(recommendations)

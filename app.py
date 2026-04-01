import gdown
import os

if not os.path.exists("artifacts/similarity.pkl"):
    gdown.download(
        "https://drive.google.com/uc?id=1SlXeOXQY36FUQJV4N_Ny5ogm6P4Uksgw",
        "artifacts/similarity.pkl",
        quiet=False
    )

import pickle
import streamlit as st
import requests 
import pandas as pd

#page title
st.set_page_config(
    page_title = "Movie Recommendation System",
    page_icon = "🎬",
    layout = "wide"
)

#load model files
@st.cache_resource
def load_artifacts():
    movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
    return movies, similarity
movies, similarity = load_artifacts()

if isinstance(movies, pd.DataFrame):
    movie_list = movies['title'].values
else:
    movie_list = movies


@st.cache_data(show_spinner=False)
def fetch_poster(movie_title : str):
    try:
        url = (
            f"https://api.themoviedb.org/3/search/movie"
            f"?api_key=1ef5596d75582678fb95d04405adf351&query={requests.utils.quote(movie_title)}"
        )
        data = requests.get(url, timeout = 5).json()
        poster_path = data["results"][0]["poster_path"]
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception:
        return "https://via.placeholder.com/500x750?text=No+Poster"
    
    

#recommendation logic
def recommendation(movie_title: str, n :int = 5):
    if isinstance(movies, pd.DataFrame):
        idx = movies[movies['title'] == movie_title].index[0]
    else:
        idx = movies.index[movies == movie_title][0]

    distances = sorted(
        enumerate(similarity[idx]), key = lambda x: x[1], reverse=True
    )

    recommendations = []
    for i, score in distances[1 : n+1]:
        if isinstance(movies, pd.DataFrame):
            recommendations.append(movies.iloc[i]['title'])
        else:
            recommendations.append(movies[i])


    return recommendations

#UI
st.title("Movie Recommendation System")
st.markdown("Select a movie you like ")
col1, col2, col3 = st.columns([4,2,1])

with col1:
    selected_movie = st.selectbox("SEARCH OR SELECT A MOVIE",
                                  options =  movie_list,
                                  index = 0,
                                  placeholder = "Type to search..."
                                )
    
with col2:
    n_recommendations = st.slider("Number of Recommendations", 3,10,5)

with col3:
    st.markdown("<br>", unsafe_allow_html=True)
    recommend_btn = st.button("Recommend", use_container_width=True)

if recommend_btn:
    with st.spinner("Finding similar movies..."):
        recommended_movies = recommendation(selected_movie, n = n_recommendations)
        posters = [fetch_poster(m) for m in recommended_movies]
        
    st.subheader(f"Movies similar to {selected_movie}")
    st.divider()

    cols = st.columns(len(recommended_movies))
    for col, title, poster in zip(cols, recommended_movies, posters):
        with col:
            st.markdown(
                f"""
                <div style="text-align:center;">
                    <img src="{poster}"
                    style="width:100%; border-radius:10px; object-fit:cover;"
                    alt="{title}"/>
                    <div style="
                        background:#1e1e2e;
                        border-radius:8px;
                        padding:8px 4px;
                        margin-top:8px;
                    ">
                        <span style="color:white; font-size:13px; font-weight:600;">{title}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


# footer 
st.markdown("---")
st.caption("Content-Based Filtering . Built with stream lit")
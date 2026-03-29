# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System that suggests movies based on user preferences. This project uses similarity scores to recommend movies similar to the one selected by the user and displays them using an interactive Streamlit web app.

---

## 🚀 Features

* Select a movie from a dropdown list
* Get top 5 similar movie recommendations
* Clean and interactive UI using Streamlit
* Fast recommendation using precomputed similarity matrix
* Poster support (can be enabled using TMDB API)

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

---

## 📁 Project Structure

```
Movie Recommendation System/
│
├── app.py
├── artifacts/
│   ├── movie_list.pkl
│   └── similarity.pkl
├── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone <your-repo-link>
cd Movie Recommendation System
```

2. Create a virtual environment:

```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 🎯 How It Works

* The system uses a **content-based filtering approach**
* Movies are compared using similarity scores
* Based on the selected movie, the system recommends the most similar ones

---

## 📌 Future Improvements

* Add movie posters using TMDB API
* Improve recommendation accuracy
* Deploy the app online
* Add search functionality

---

## 👩‍💻 Author

**Saara Sugandh**

---

## ⭐ Acknowledgements

* Dataset used for training the model
* TMDB API (for posters - optional)

---

## 📄 License

This project is for educational purposes.

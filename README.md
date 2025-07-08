# 🎬 Bollywood-Movie-Recommender-System

An interactive AI-based movie recommendation system built using **Python**, **Pandas**, **Scikit-learn**, and **CustomTkinter**. This project recommends Bollywood movies based on **genre similarity** using **TF-IDF** and **cosine similarity**.

---

## 🚀 Features

- Select a movie from a dropdown
- View top 5 recommended movies based on genre
- AI logic using TF-IDF + cosine similarity
- Modern GUI with `CustomTkinter`
- No internet or database required

---

## 🧠 Tech Stack

- Python 3.8+
- Pandas
- Scikit-learn
- CustomTkinter
- CSV as dataset source

---

## 📂 Folder Structure

AImovie_recommender/
├── movie_gui.py # Main GUI script
├── movies_metadata.csv # Dataset (must be in same folder)

---

## 💾 Dataset

- Uses a `movies_metadata.csv` file with columns:
  - `title`
  - `genre`
- You can replace it with a Bollywood dataset from Kaggle or TMDb.

---

## 🖥️ How to Run

### Install Dependencies

```bash
pip install pandas scikit-learn customtkinter
```
Run
```bash
python movie_gui.py
```

## 🧠 AI Logic
- Extract genre text
- Convert genres to TF-IDF vectors
- Compute cosine similarity
- Recommend top 5 similar movies

---

## 🛠️ Future Ideas
- Add plot and cast info for smarter recommendations
- Add movie posters using TMDb API
- Export recommendations to file

---

## 🙋‍♂️ Author
Suyash Tiwari
- Bollywood movie magic meets machine learning. Get started now and discover your next favorite film!

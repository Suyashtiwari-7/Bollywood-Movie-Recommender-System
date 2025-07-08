# ✅ Bollywood Genre-Based Movie Recommender with CustomTkinter (Final Version)

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import customtkinter as ctk

# ----------------------------
# Step 1: Load CSV (absolute path-safe)
# ----------------------------

# Find the folder of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "movies_metadata.csv")

# Load the CSV using safe path
df = pd.read_csv(csv_path, low_memory=False)

# Clean and use correct columns
df.columns = df.columns.str.strip().str.lower()  # normalize column names
df = df[['title', 'genre']].dropna()
df.columns = ['title', 'genre_text']  # rename for code consistency

# ----------------------------
# Step 2: TF-IDF + Similarity on genre_text
# ----------------------------

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre_text'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()

def recommend(title, n=5):
    title = title.lower()
    if title not in indices:
        return []
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

# ----------------------------
# Step 3: Build GUI
# ----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("520x470")
app.title("🎬 Bollywood Genre-Based Recommender")

# Dropdown for movie titles
movie_titles = sorted(df['title'].dropna().unique().tolist())
combo = ctk.CTkComboBox(app, values=movie_titles, width=400)
combo.pack(pady=20)
combo.set("Select a movie")

# Output box
result_box = ctk.CTkTextbox(app, width=460, height=250, font=("Arial", 12))
result_box.pack(pady=10)

# Button action
def show_recommendations():
    title = combo.get().strip()
    result_box.delete("1.0", "end")

    if not title or title == "Select a movie":
        result_box.insert("end", "⚠️ Please select a movie title.")
        return

    results = recommend(title)
    if results:
        result_box.insert("end", f"🎯 Genre-based recommendations for '{title}':\n\n")
        for i, rec in enumerate(results, 1):
            result_box.insert("end", f"{i}. {rec}\n")
    else:
        result_box.insert("end", "❌ Movie not found in dataset.")

# Recommend button
button = ctk.CTkButton(app, text="Recommend", command=show_recommendations)
button.pack(pady=10)

# Run app
app.mainloop()

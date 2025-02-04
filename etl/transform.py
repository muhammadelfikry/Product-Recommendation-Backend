from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def transform(df):
    try:
        data = df[["Name", "Brand", "Description", "Notes", "Image URL"]].copy()
        data = data.dropna()

        note_list = data["Notes"].str.split(",")
        note_list = [[note for note in sublist if note.strip() != ''] for sublist in note_list]
        
        data["Notes"] = note_list
        data["Notes"] = data["Notes"].apply(lambda x: ", ".join(x))
        data['Notes'] = data['Notes'].str.strip()
        
        data['Description'] = data['Description'].str.strip()
        
        tf = TfidfVectorizer()
        tf.fit(data["Notes"])

        tfidf_matrix = tf.fit_transform(data["Notes"])
        tfidf_matrix.todense()

        cosine_sim = cosine_similarity(tfidf_matrix)
        
        cosine_sim_df = pd.DataFrame(cosine_sim, index=data["Name"], columns=data["Name"])

        return cosine_sim_df, data
    
    except Exception as e:
        print("Data transform error: " + str(e))
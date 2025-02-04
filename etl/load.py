from etl.setup import *
import pandas as pd

def product_recommendation(product_name, similarity_data, items, k=5):
    index = similarity_data.loc[:, product_name].to_numpy().argpartition(
        range(-1, -k, -1)
    )

    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    closest = closest.drop(product_name, errors="ignore")

    recomended_df = pd.DataFrame(closest).merge(items).head(k)
    recomended_df = recomended_df.to_dict(orient="records")
    
    return recomended_df

def load(name, similarity_df, items):
    try:
        recommendation = product_recommendation(name, similarity_df, items)
        
        return recommendation

    except Exception as e:
        print("Data load error: " + str(e))
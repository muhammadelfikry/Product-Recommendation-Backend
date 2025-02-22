from fastapi import FastAPI
from etl.setup import *
from etl.extract import extract
from etl.transform import transform
from etl.load import load
import sqlalchemy as sqla

app = FastAPI()

db = sqla.create_engine(src_url)

sql = 'SELECT * FROM product'
df = extract(db=db, sql=sql)

cosine_sim_df, items = transform(df)

@app.get("/products")
def get_products():
    return items.to_dict(orient="records")

@app.get("/recommendation")
def get_recommendation(product_name: str):
    user_input = product_name

    recommendation = load(user_input, similarity_df=cosine_sim_df, items=items)
    
    return recommendation

if __name__=="__main__":
    app.run(debug=True, port=8000)
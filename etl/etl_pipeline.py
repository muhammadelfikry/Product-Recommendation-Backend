from setup import *
from extract import extract
from transform import transform
from load import load
import sqlalchemy as sqla

db = sqla.create_engine(src_url)

sql = "select * from product"
df = extract(db=db, sql=sql)

cosine_sim_df = transform(df)

load(df=cosine_sim_df)
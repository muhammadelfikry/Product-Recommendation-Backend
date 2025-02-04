from etl.setup import *
import sqlalchemy as sqla
import pandas as pd

def extract(db, sql):
    try:

        df = pd.read_sql(sql, db)
        
        return df
    
    except Exception as e:
        print("Data export error: " + str(e))


if __name__ == "__main__":
    db = sqla.create_engine(src_url)
    sql = "SELECT * FROM product"
    df = extract(db=db, sql=sql)
    print(df.head(5))
    print(df.count())
from setup import *
from supabase import create_client

def load(df):
    try:
        print("Data loaded success")
        print(df[:5])
        print(df.shape)

    except Exception as e:
        print("Data load error: " + str(e))
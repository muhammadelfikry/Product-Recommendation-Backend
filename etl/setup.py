from dotenv import load_dotenv
import os

load_dotenv()

PWD = os.environ["PASSWORD"]
USER_ID = os.environ["USER_ID"]
SERVER = os.environ["SERVER"]
DB = os.environ["DATABASE"]
PORT = os.environ["PORT"]

src_url = f"postgresql://{USER_ID}:{PWD}@{SERVER}:{PORT}/{DB}"
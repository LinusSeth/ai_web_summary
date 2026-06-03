import json, argparse, os, re, requests 
from bs4 import BeautifulSoup
from dotenv import load_dotenv

#--utils--
def load_env()->str:
    load_dotenv()
    k= os.getenv("API_KEY")
    if not k:
        raise SystemExit("set API_KEY in env")
    return k

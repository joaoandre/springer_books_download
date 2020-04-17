import requests
import pandas as pd
from urllib.parse import urlparse


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

invalid_chars = '<>:"/\|?*'.split()


session = requests.Session()
df = pd.read_csv("books.csv")

for i, book in df.iterrows():
    urlObject = urlparse(book['DOI URL'])
    url = f"https://link.springer.com/content/pdf/{urlObject.path}.pdf"
    print(f"Downloading {book['Book Title']} by {book['Author']} on URL {url}")
    print("-------------------------------------------------------------------")
    f = requests.get(url)
    file_name = ""
    for c in book['Book Title']:
        file_name += '_' if c in invalid_chars else c
        
    open(f"{file_name}.pdf", "wb").write(f.content)

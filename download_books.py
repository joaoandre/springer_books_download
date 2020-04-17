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


session = requests.Session()
# http: // doi.org/10.1007/978-0-387-21736-9	http: // link.springer.com/openurl?genre = book & isbn = 978-0-387-21736-9
df = pd.read_csv("books.csv")

for i, book in df.head().iterrows():
    urlObject = urlparse(book['DOI URL'])
    url = f"https://link.springer.com/content/pdf/{urlObject.path}.pdf"
    print(
        f"Downloading {book['Book Title']} by {book['Author']} on URL {url}")
    print("-------------------------------------------------------------------")
    f = requests.get(url)
    open(f"{book['Book Title']}.pdf", "wb").write(f.content)

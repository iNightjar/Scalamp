# Scalamp :snake: Python Web Scraping

## Getting Started

```python
from bs4 import BeautifulSoup as bs
import requests


# WebSite Page
Url = "Url Link"
results = requests.get(Url)
doc = bs(results.text, "html.parser")



# local HTML File Inside Your Directory
with open("Filename.html", "r") as Alias:
    doc = bs(Alias, "html.parser")
```

<br>

### Get It Work 🐛

```
git clone https://github.com/iNightjar/Scalamp.git
cd Scalamp
git checkout master
rm -rf .git
git init .
git branch [branch-name] # make it descriptive
git add [file]  # individual commits for each file are prefered
git commit -m "Your Commit Message"
```

### Create virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate
```

Use `.\venv\Scripts\activate` if on windows

### Install requirements

```
(venv) python -m pip install pip --upgrade
(venv) python -m pip install -r requirements.txt
```

### Open VSCode & Start Coding

```bash
cd /path/ProjectX
code .
```
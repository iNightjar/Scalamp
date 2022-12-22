# Scalamp :snake: Python Web Scraping

## In Stock 3080 Graphics Card <img class="emoji" alt="snake" src="https://user-images.githubusercontent.com/60796459/208253879-71ec67fe-d25d-4d21-bc2f-94cb46948fc2.png" width="20" height="20">  Price:dollar: and Product Link:link:

<https://user-images.githubusercontent.com/60796459/208224658-766e537e-7033-4d0a-8ad2-3b673a1ae950.mp4>

## Code Snippets :star:

```python
from bs4 import BeautifulSoup as bs
import requests


# WebSite Page
Url = "Url Link"
results = requests.get(Url)
doc = bs(results.text, "html.parser")



# Local HTML File Inside Your Directory
with open("Filename.html", "r") as Alias:
    doc = bs(Alias, "html.parser")


# Writes Down Changes into New Html file
for tag in tags:
    tag['placeholder'] = "I changed you!"  # Change The value in placeholder attr
    # print(type(tag)) > Element

with open("v2CourseRegistration.html", "w") as file:
    file.write(str(doc))


# dictionary that contains each item:{price, link}
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

# looping through items to print them
for item in sorted_items:
    print("-------------------------")
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("-------------------------")

```

### Clone The Repository 🐛

```bash
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

```bash
(venv) python -m pip install pip --upgrade
(venv) python -m pip install -r requirements.txt
```

### Open VSCode & Start Coding

```bash
cd /path/Sclamp
code .
```

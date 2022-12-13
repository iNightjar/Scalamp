# Scalamp :snake: Python Web Scraping
## Getting Started

```python
from bs4 import BeautifulSoup as bs
import requests


with open("Filename.html", "r") as Alias:
    doc = bs(Alias, "html.parser")
```


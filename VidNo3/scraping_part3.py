from bs4 import BeautifulSoup as bs
import requests

url = "https://coinmarketcap.com/"  # website page URL

# GithubPageURL = "https://bluelimelearning.github.io/my-fav-quotes/"
result = requests.get(url).text
document = bs(result, "html.parser")

TreeBody = document.tbody

# print(TreeBody.contents)

tableRows = TreeBody.contents

# grap next sibling to the first element in table row
# print(tableRows[0].next_siblings)
# print(list(tableRows[0].next_siblings))
# print(tableRows[1].previous_sibling)
# print(tableRows[0].parent.name) # Can use a list with it, List()
# print(list(tableRows[0].contents))
# you can replace the contents attr with children
# print(list(tableRows[0].contents))


prices = {}


for tr in tableRows[:10]:
   name, price = tr.contents[2:4]
   fixed_name = name.p.string
   fixed_price = price.a.string

   prices[fixed_name] = fixed_price

print(prices)

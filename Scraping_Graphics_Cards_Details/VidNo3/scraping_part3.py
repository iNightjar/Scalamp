from bs4 import BeautifulSoup as bs
import requests

url = "https://coinmarketcap.com/"  # website page URL

# GithubPageURL = "https://bluelimelearning.github.io/my-fav-quotes/"
result = requests.get(url).text
document = bs(result, "html.parser")

TreeBody = document.tbody

# print(TreeBody.contents)

tableRows = TreeBody.contents

# print(tableRows)

# grap next sibling to the first element in table row
# print(tableRows[0].next_siblings)
# print(list(tableRows[0].next_siblings))
# print(tableRows[1].previous_sibling)
# print(tableRows[0].parent.name) # Can use a list with it, List()
# # print(list(tableRows[0].contents))
# # you can replace the contents attr with children
# print(list(tableRows[0].contents))


prices = {}  # contains pair of name : price

# for iterator in tableRows:
#    for td in iterator.contents:
#       print(td)
#       print()


for iterator in tableRows[:10]:
   coin, price = iterator.contents[2:4]
   coinName = coin.p.string
   coinPrice = price.a.string
   prices[coinName] = coinPrice  # giving each pair of {coin : price}


print(prices)

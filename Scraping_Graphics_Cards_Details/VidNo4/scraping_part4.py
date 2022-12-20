from bs4 import BeautifulSoup as bs
import requests
import re

# url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

search_term = input("What products do you want to search for?  ")


url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
document = bs(page, "html.parser")

pageNumbers = document.find(
    class_="list-tool-pagination-text").strong

# print the second element from behind, which is number of lastPage
lastPage = int(str(pageNumbers).split("/")[-2].split(">")[-1][:-1])
# print(lastPage) # checking the output

items_found = {}

for page in range(1, lastPage + 1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={lastPage}"
    page = requests.get(url).text
    document = bs(page, "html.parser")

    # Dev: Class name
    # item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell
    # it has only the items that iam searching for
    div = document.find(
        class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    # re.compiel >> match any text contain the search_term
    items = div.find_all(text=re.compile(search_term))

    for item in items:
        parent = item.parent

        if parent.name != "a":
            continue

        link = parent["href"]
        # print(link)

        # to get the product pirce
        # classes: "item-container" , "item-action " , "price", "price-current"

        # interesting method
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(
                class_="price-current").find("strong").string
            # print(price)
            items_found[item] = {"price": int(
                price.replace(",", "")), "link": link}
        except:
            pass


# dictionary that contains each item:{price, link}
# print(items_found)

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

# looping through items to print them
for item in sorted_items:
    print("-------------------------")
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("-------------------------")

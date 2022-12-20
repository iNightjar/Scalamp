from bs4 import BeautifulSoup as bs
import requests


# with open("dummyhtml.html", "r") as file:
#     doc = bs(file, "html.parser")


# tag = doc.find_all("p")[0]
# print(tag.find_all("b"))


# for i in tag:
#   print(i.string)


# githubIoPage = "https://inightjar.github.io/Software1-3rd-IS/CVTempleteUsingHTMLCSS/index.html"  # private github repo deployed on github pages.. CV Template made with ReactJS
# url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

githubPage = "https://bluelimelearning.github.io/my-fav-quotes/"

with open("codeResultFavQoutes.html", "r") as qoutes:
    doc = bs(qoutes, "html.parser")
# results = requests.get(githubPage)
# doc = bs(results.text, "html.parser")

job = doc.find_all(text="Confucious")
parent = job[0].parent
print(parent.string)

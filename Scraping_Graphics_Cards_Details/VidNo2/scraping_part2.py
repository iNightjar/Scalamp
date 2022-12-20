from bs4 import BeautifulSoup as bs
import re  # regular expressions


# Reading from dummyhtml_CourseRegistration.html file
with open("../CourseRegistration.html", "r") as index:
    doc = bs(index, "html.parser")


# limit finds to 10 objects
# tags = doc.find_all(text=re.compile("\$.*"), limit=10)

#c
tags = doc.find_all("input", type="text")
# value = tag["selected"]= "false"
# tag['color'] = "black"
# for tag in tags:
#     print(tag.strip())      # strip and remove spaces
# print(tags)
# print(tag.attrs)


for tag in tags:
    tag['placeholder'] = "I changed you!"
    # print(type(tag))

with open("v2CourseRegistration.html", "w") as file:
    file.write(str(doc))

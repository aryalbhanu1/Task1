"""
It is always represent in the form of:
my_dictionary = {"key":"Value"}
"""

#why we need dictionary?
#--> To overcome the problem exist in list.
#for eg:
#user_detail=["Sachin","Shrestha",20,["English","Nepali","Spanish"],9999999999,["jpani","teipani"]]

from http.server import SimpleHTTPRequestHandler


user_details={
     "first_name":"Sachin",
      "last_name":"Shrestha",
      "language_spoken":["English","Nepali","Chinese"],
      "contact":9810119909


}
print(user_details["first_name"])

for key,value in user_details.items():
    print(f"The key is:{key} and its value is: {value}")

for key in user_details.items():
    print(f"The key is:{key}")

for value in user_details.items():
    print(f"The value is:{value}")``
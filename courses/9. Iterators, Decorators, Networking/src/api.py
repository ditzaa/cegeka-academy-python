import requests

# CREATE a product -> POST
new_product = {"title": "notebook", "price": 19.99}
response = requests.post('https://dummyjson.com/products/add', data=new_product)
print(response.status_code, response.text)

# READ a product -> GET
product_id = 100
response = requests.get(f'https://dummyjson.com/products/{product_id}')
print(response.status_code, response.text)

# READ multiple products -> get
response = requests.get(f'https://dummyjson.com/products/', params={"limit": 5})
response_json = response.json()
print(response.status_code, response.text)
for product in response_json["products"]:
    print(product["title"])

# UPDATE a product -> PUT / PATCH
updated_product = {"id": 100, "title": "Notebook", "price": 59.99}
response = requests.put(f'https://dummyjson.com/products/100', data=updated_product)
print(response.status_code, response.text)

updated_product = {"price": 100.99}
response = requests.patch(f'https://dummyjson.com/products/100', data=updated_product)
print(response.status_code, response.text)

# DELETE a product -> DELETE
response = requests.delete("https://dummyjson.com/products/100")
print(response.status_code, response.text)

# Authentication with username and password
credentials = {"username": "emilys", "password": "emilyspass"}
response = requests.post("https://dummyjson.com/auth/login", data=credentials)
print(response.status_code, response.text)
token = response.json()["accessToken"]

# GET with token authorization
response = requests.get("https://dummyjson.com/auth/me", headers={"Authorization": "Bearer " + token})
print(response.status_code, response.text)

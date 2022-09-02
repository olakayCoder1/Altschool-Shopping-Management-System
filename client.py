import requests

response = requests.get('https://fakestoreapi.com/products')
data = response.json()
print(len(data))
def upload_items_to_file():
    file = open('items.txt','w') 
    response = requests.get('https://fakestoreapi.com/products')
    data = response.json()
    for item in data:
        file.write(f"{item['category']},{item['title']},{int(item['price'])*100}\n")
    file = open('items.txt','r') 
    print(file.read())
    file.close() 


user_cart = []





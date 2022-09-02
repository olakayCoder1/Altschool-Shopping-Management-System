import requests
import store

response = requests.get('https://fakestoreapi.com/products')
data = response.json()

def upload_items_to_file():
    file = open('items.txt','w') 
    response = requests.get('https://fakestoreapi.com/products')
    data = response.json()
    for item in data:
        file.write(f"{item['category']},{item['title']},{int(item['price'])*100}\n")
    file = open('items.txt','r') 
    print(file.read())
    file.close() 


user_cart = {}
items_store = store.store

def program():


    print('WELCOME TO OLAKAY SHOPPING MALL')
    print('Kindly select the from the option below the transaction you wish to perform')
    print("A : View list of all product")
    print("B : Search product by category")
    print("C : View list of all product")
    print("D : View list of all product")
    user_response = input(':::: ')
    print('***'*19)
    if user_response.lower() == 'a' :
        items_store.print_items()
    if user_response.lower() == 'b' :
        print('You can search product by the following category: ')
        print("men's clothing")
        print("women's clothing")
        print("jewelery")
        print("electronics")
        search_query = input('Type any of the above category...  : ')
        print('***'*19)
        items_store.search_by_category(search_query)

        pass 

    cart = store.Cart()
    cart.add_to_cart(2)
    cart.add_to_cart(2)
    cart.add_to_cart(2)
    cart.add_to_cart(2)
    cart.add_to_cart(9)
    cart.add_to_cart(2)
    # if user_cart.get(['name']) != None :
    #     user_cart['name']['quantity'] += 1 
    # else:
    #     user_cart['name'] = 7
    #     user_cart['quantity'] = 1
        
    # print(cart.items)

program()
    







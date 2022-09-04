import requests
import store



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
    cart = store.Cart()
    start = True 
    while start :
        print('🥳🥳🥳🥳🥳 ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \nWELCOME TO OLAKAY SHOPPING MALL\n ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡🥳🥳🥳🥳🥳')
        print('Kindly select the from the option below the transaction you wish to perform')
        print("A : View list of all product")
        print("B : Search product by category")
        print("C : view cart")
        print("D : Check out")
        print("E : QUIT")
        user_response = input(':::: ')
        print('***'*25)
        if user_response.lower() == 'a' :
            items_store.print_items()
            print('***' * 25 )
            print('To add an item to cart enter the item corresponding id eg for  "Mens Cotton Jacket" enter "3"')
            print('For multiple item enter their corresponding id separated by comma(",") eg for "Mens Casual Slim Fit" and "Mens Cotton Jacket" enter "4,3" ')
            print('***' * 25 )
            item_to_add_input = input('Select :::: ')
            item_to_add_id = item_to_add_input.replace(" ","").split(",")
            print(item_to_add_id)
            for id in item_to_add_id :
                try:
                    cart.add_to_cart(int(id))
                except:
                    pass
            print('***' * 25 )
        if user_response.lower() == 'b' :
            print('You can search product by the following category : ')
            print("men's clothing")
            print("women's clothing")
            print("jewelery")
            print("electronics")
            search_query = input('Type any of the above category.....  : ')
            print('***' * 25 )
            items_store.search_by_category(search_query)

        if user_response.lower() == 'c' :
            cart.view_cart()

        if user_response.lower() == 'd' :
            cart.check_out()
            start = False

        if user_response.lower() == 'e' :
            start = False
        

    







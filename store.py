



from hashlib import new


items_category = {
    'men clothing': {
        'items': []
    },

    'women clothing': {
        'items': [] 
    },
    # 'food items': {
    #     'items': [] 
    # },
    # 'fashion' : {
    #     'items': [] 
    # },
}




def add_item_to_items_category( name , price , category , id ):
    if items_category.get(str(category)) != None :
        category_dict = items_category.get(str(category))
        if len(category_dict['items']) > 0 :
            for item_object in category_dict['items'] :
                if item_object['name'] == name :
                    item_object['quantity'] += 1 
                    item_object['price'] = price 
                    return
            new_item = dict()
            new_item['name'] = name
            new_item['price'] = price
            new_item['quantity'] = 1
            new_item['id'] = id
            items_category.get(str(category))['items'].append(new_item)
        else:
            new_item = dict()
            new_item['name'] = name
            new_item['price'] = price
            new_item['id'] = id
            items_category.get(str(category))['items'].append(new_item) 



class Item:
    def __init__(self , category , name , price = 10.00 ):
        self.name = name 
        self.price = price
        self.id = 0
        self.category = category
        self.next_item = None



class Store:

    def __init__(self):
        self.head = None

    
    def items_length(self):
        if self.head == None :
            return 0
        current_node = self.head
        length = 0
        while current_node.next_item != None :
            length += 1
            current_node = current_node.next_item
        length = length + 1
        return length

    


    def add_new_item(self, name , price , category ):
        new_item = Item( category , name, int(price) )
        if self.head == None:
            new_item.id = self.items_length() + 1
            self.head = new_item
            add_item_to_items_category(name, price , category , id=new_item.id)
            items_category[category] 
            return
        current_node = self.head
        while current_node.next_item != None :
            current_node = current_node.next_item
        current_node.next_item = new_item
        new_item.id = self.items_length() 
        add_item_to_items_category(name, price , category, id=new_item.id)


    

    
    def print_items(self):
        if self.head == None :
            return None
        current_node = self.head
        while current_node.next_item != None :
            print(f'{current_node.id} -> {current_node.name} -> {current_node.price}$ -> {current_node.category}' )
            current_node = current_node.next_item
        print(f'{current_node.id} -> {current_node.name} -> {current_node.price}$ -> {current_node.category}' )
        return


    def display_search(self, result : list ):
        for items in result:
            print(f"{ items['name'] } -> { items['price']}")
    def search_by_category(self,query):
        category_dict = items_category.get(str(query))
        if category_dict != None :
            self.display_search(category_dict['items'])
        else:
            print('We do not have item in your search category\nThese are the categories we have: ')
            for category  in items_category.keys() :
                print(category)

    def add_to_cart(self):
        pass


m = Store()
m.add_new_item('Vintage', 2000 , 'men clothing')
m.add_new_item('Vintage3', 23000 , 'men clothing')
m.add_new_item('Vintage5', 26000 , 'men clothing')


print(m.print_items())
# m.search_by_category('men clothing')



# add_item_to_items_category('Vintage',9000000,'men clothing')
# add_item_to_items_category('gean',900000,'men clothing')


print(items_category)

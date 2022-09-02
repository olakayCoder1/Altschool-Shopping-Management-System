



from hashlib import new


items_category = {
    "men's clothing": {
        'items': []
    },

    "women's clothing": {
        'items': [] 
    },
    "electronics": {
        'items': [] 
    },
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
            new_item['quantity'] = 10
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
            print(f'{current_node.id} | {current_node.name} | {current_node.price}$ | {current_node.category}' )
            current_node = current_node.next_item
        print(f'{current_node.id} | {current_node.name} | {current_node.price}$ | {current_node.category}' )
        return

    def display_search(self, result : list ):
        for items in result:
            print(f"{ items['id'] } | { items['name'] } | { items['price']}")


    def search_by_category(self,query):
        search_result = [] 
        for category in items_category.keys():
            if category.find(query) != -1 :
                for item in items_category[category]['items']:
                    search_result.append(item)
        if len(search_result) <= 0 :
            print('We do not have item in your search category\nThese are the categories we have: ')
            return
        else:
            self.display_search(search_result)


    def user_add_to_cart(self,id):
        if self.head == None:
            return
        current_node = self.head
        while current_node.next_item != None :
            if current_node.id == id :
                return (current_node.name , current_node.price)
            current_node = current_node.next_item
        if current_node.id == id :
            return (current_node.name , current_node.price )
        return
        pass

    def find_food_detail(self,id):
        if self.head == None:
            return
        current_node = self.head
        while current_node.next_food != None :
            if current_node.id == id :
                return (current_node.name , current_node.price)
            current_node = current_node.next_food
        if current_node.id == id :
            return (current_node.name , current_node.price )
        return


store = Store()

file = open('items.txt','r') 
line = file.readline()
while line:
    current_item = line.split(',')
    category = current_item[0]
    title = current_item[1]
    price = current_item[2].strip('\n')
    store.add_new_item( title, price , category)
    line = file.readline()
file.close()

store.add_new_item('Vintage', 2000 , 'men clothing')
store.add_new_item('Vintage3', 23000 , 'men clothing')
store.add_new_item('Vintage5', 26000 , 'men clothing')


# print(store.print_items())
store.search_by_category('men')



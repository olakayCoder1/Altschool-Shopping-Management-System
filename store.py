
class Item:


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
        
    def __init__(self , category , name , price = 10.00 ):
        self.name = name 
        self.price = price
        self.id = 0
        self.category = category
        self.next_item = None

    @classmethod
    def decrease_item_quantity(cls , category , id):
        for item in cls.items_category[category]['items'] :
            if item['id'] == int(id) :
                item['quantity'] -= 1

    @classmethod
    def add_item_to_items_category( cls , name , price , category , id ):
        if cls.items_category.get(str(category)) != None :
            category_dict = cls.items_category.get(str(category))
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
                cls.items_category.get(str(category))['items'].append(new_item)
            else:
                new_item = dict()
                new_item['name'] = name
                new_item['price'] = price
                new_item['id'] = id 
                new_item['quantity'] = 10
                cls.items_category.get(str(category))['items'].append(new_item) 



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
            new_item.add_item_to_items_category(name, price , category , id=new_item.id)
            new_item.items_category[category] 
            return
        current_node = self.head
        while current_node.next_item != None :
            current_node = current_node.next_item
        current_node.next_item = new_item
        new_item.id = self.items_length() 
        new_item.add_item_to_items_category(name, price , category, id=new_item.id)
  


    def print_items(self):
        if self.head == None :
            return None
        current_node = self.head
        while current_node.next_item != None :
            print(f'{current_node.id} | {current_node.name} | {current_node.price}$ ' )
            current_node = current_node.next_item
        print(f'{current_node.id} | {current_node.name} | {current_node.price}$ ' )
        return


    def display_search(self, result : list ):
        for items in result:
            print(f"{ items['id'] } | { items['name'] } | { items['price']}")


    def search_by_category(self,query):

        custom_instance = Item( name='' , price=0 , category='' )
        if custom_instance.items_category.get(str(query)) != None :
            self.display_search(custom_instance.items_category[query]['items'])
            return
        else:
            print('We do not have item in your search category\nThese are the categories we have: ')


    def pick_to_cart(self,id):
        if self.head == None:
            return
        current_node = self.head
        while current_node.next_item != None :
            if current_node.id == id :
                current_node.decrease_item_quantity(current_node.category , current_node.id )
                return {'id': current_node.id  , 'name' : current_node.name , 'price' : current_node.price }
            current_node = current_node.next_item
        if current_node.id == id :
            current_node.decrease_item_quantity(current_node.category , current_node.id )
            return {'id': current_node.id  , 'name' : current_node.name , 'price' : current_node.price }
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


class Cart:
    def __init__(self):
        self.items = {}
        

    def add_to_cart(self , id ):
        item = store.pick_to_cart(id)
        if self.items.get(item['name']) != None :
            self.items[item['name']]['quantity'] += 1 
        else:
            self.items[item['name']] = dict()
            self.items[item['name']]['quantity'] = 1
            self.items[item['name']]['price'] = item['price']
            self.items[item['name']]['id'] = item['id']
            return 

    def view_cart(self):
        if len(self.items) == 0 :
            print('There is no item in the cart')
            return
        else:
            print('⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \nCART DETAILS\n ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡')
            print('ITEM     |     PRICE     |     QUANTITY')
            for key , value in self.items.items() :
                print(f"{key} |  {value['price']}  | {value['quantity']}")

    def check_out(self):
        if len(self.items) == 0 :
            print('There is no item in the cart')
            return
        else:
            print('⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \nPURCHASE DETAILS\n ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡')
            sum = 0
            for key , value in self.items.items() :
                item_total_cost = int(value['price']) * int(value['quantity'])
                print(f"{key} |  {value['price']}  | {value['quantity']} |  {item_total_cost}")
                sum += item_total_cost

            print(f'TOTAL COST : {sum}')
            print('Thanks for your patronage')







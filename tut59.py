# write a class view which takes input from users


class Shopping:
    list_option = {}

    def __init__(self):
        self.option = input('Please choose the item in Item_List: ')
        self.quantity = input('Choose the quantity:')
        self.option_again = input(
            'You want to choose the option again yes or no: ')

    def check_option_again(self):
        self.option = input('Please choose the item in Item_List: ')
        self.quantity = input('Choose the quantity:')
        self.option_again = input(
            'You want to choose the option again yes or no: ')
        self.item_search()

    def item_search(self):
        if self.option in self.list_option:
            self.list_option[self.option] += int(self.quantity)
        else:
            self.list_option[self.option] = int(self.quantity)
        if self.option_again == 'yes':
            self.check_option_again()
            return
        print('Data:', self.list_option)


obj1 = Shopping()
obj1.item_search()

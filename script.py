from menu import Menu
from franchise import Franchise
from business import Business

######## MENU IMPLEMENTATION ########
# brunch is served from 11am to 4pm
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("brunch", brunch_items, 11, 16)
brunch_bill = brunch.calculate_bill(["pancakes", "home fries", "coffee"])
# print(brunch_bill)

# early bird dinners are served from 3pm to 6pm
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("early bird", early_bird_items, 15, 18)
early_bird_bill = early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])
# print(early_bird_bill)

# dinner is served from 5pm to 11pm
dinner_menu_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("dinner", dinner_menu_items, 17, 23)
print(dinner)

# kids menu is available from 11am to 9pm
kids_menu_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("kids", kids_menu_items, 11, 21)
print(kids)
######## END - MENU IMPLEMENTATION ########



######## FRANCHISE IMPLEMENTATION ########
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
# print(flagship_store.available_menus(17))

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(new_installment)
######## END - FRANCHISE IMPLEMENTATION ########



######## BUSINESS IMPLEMENTATION ########
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# New Business
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas = Menu("arepas", arepas_items, 10, 20)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas])
take_a_arepa = Business("Take a' Arepa", [arepas_place])
print(take_a_arepa.franchises[0].available_menus(18))
######## END - BUSINESS IMPLEMENTATION ########

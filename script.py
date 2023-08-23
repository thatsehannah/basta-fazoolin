class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def convert_times(self, time):
    if type(time) is int:
      twelve_hour = time
      period = "am"

      if time >= 12:
        period = "pm"

      if time > 12:
        twelve_hour = time - 12

      return "{}:00{}".format(twelve_hour, period)
    
    return None

  def __repr__(self):
    converted_start_time = self.convert_times(self.start_time)
    converted_end_time = self.convert_times(self.end_time)
    
    return "The {} menu is available from {} to {}".format(self.name, converted_start_time, converted_end_time)
  
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price += self.items[item]
    return total_price

# brunch is served from 11am to 4pm
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("brunch", brunch_items, 11, 16)
brunch_bill = brunch.calculate_bill(["pancakes", "home fries", "coffee"])
print(brunch_bill)

# early bird dinners are served from 3pm to 6pm
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("early bird", early_bird_items, 15, 18)
early_bird_bill = early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])
print(early_bird_bill)

# dinner is served from 5pm to 11pm
dinner_menu_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("dinner", dinner_menu_items, 17, 23)

# kids menu is available from 11am to 9pm
kids_menu_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("kids", kids_menu_items, 11, 21)
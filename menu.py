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
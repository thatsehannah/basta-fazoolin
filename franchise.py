class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "The address to this restaurant is {}".format(self.address)
  
  def available_menus(self, time):
    menus = []
    for menu in self.menus:
      if time >= menu.start_time and time < menu.end_time:
        menus.append(menu)
    return menus
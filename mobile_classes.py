class Mobile:
    def __init__(self, model, battery):
        self.model = model
        self.battery = battery

    def get_battery(self):
        print('the current battery is', self.battery)

    def display(self):
        print('mobile model : ', self.model)
        print('battery level : ', self.battery)

    def charge(self, amount):
        self.battery = self.battery + amount

    def use(self, amount):
        self.battery = self.battery - amount


mobile1 = Mobile('Samsung Galaxy', 50)
mobile1.get_battery()
mobile1.charge(50)
mobile1.get_battery()
mobile1.use(75)
mobile1.get_battery()
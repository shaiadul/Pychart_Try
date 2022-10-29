class Phone:

    def set_color(self, color):
        self.color = color
        print("color is", self.color)
    def set_cost(self, cost):
        self.cost = cost
        print("cost is", self.cost)




p2 = Phone()
p2.set_color("blue")
p2.set_cost(5000)

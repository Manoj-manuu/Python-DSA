class Cookie:
    def __init__(self,color):
     self.color = color

    def get_Color(self):
        return self.color

    def set_Color(self,color):
        self.color = color

cookie_One = Cookie("Green")
cookie_Two = Cookie("Blue")

print("Cookie_one_color is ",cookie_One.get_Color())

print("Cookie_two_color is ",cookie_Two.get_Color())

cookie_One.set_Color("yellow")

print("\nThe color of cookie_one is ", cookie_One.get_Color())
print("The color of cookie_two is still ",cookie_Two.get_Color())
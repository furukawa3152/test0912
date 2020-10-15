# name="itaru"
# screen_name="@"+name.upper()
# print(screen_name)

class User_name:
    def __init__(self,name):
        if not(2 <= len(name) <= 10):
           print("2文字以上１０文字以下にしてください")
           name=name+"<不正な名前です"
        # if not(2 <= len(name) <= 10):
        #     raise ValueError("2文字以上１０文字以下にしてください")
        self.name = name
    def screen_name(self):
        return "@"+ self.name.upper()
    def special_name(self):
        return (self.name+self.name[::-1]).upper()

a=User_name("i")
b=User_name("satomi")
print(a.screen_name())
print(b.screen_name())
print(a.special_name())


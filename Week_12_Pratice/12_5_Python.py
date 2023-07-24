class MyInt:
    def __init__ (self,number):
        self.value = number
        self.roman = {
            "M" : 1000,
            "CM" : 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "I" : 1,
        }
    
    def __add__(self,object2):
        result = int((self.value + object2.value)*1.5)
        return MyInt(result)
        
         
    def toRoman(self):
        temp = self.value
        self.back_roman = ""
        while(temp > 0):
                for key, val in self.roman.items():
                    if val <= temp:
                        self.back_roman = self.back_roman + key
                        temp -= val
                        break
        return self.back_roman


print(' *** class MyInt ***')
num1, num2 = [int(x) for x in input('Enter 2 number : ').split()]
new1 = MyInt(num1)
new2 = MyInt(num2)
print(f"{new1.value} convert to Roman : {new1.toRoman()}")
print(f"{new2.value} convert to Roman : {new2.toRoman()}")
print(f"{new1.value} + {new2.value} = {(new1 + new2).value}")



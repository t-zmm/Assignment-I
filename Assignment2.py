a=int(input("This is the first number: "))
b=int(input("This is the second number: "))
c=input("Choose your operation(+,-,*,/,//,%):")

all_a=id(a)
all_b=id(b)

print("The allocation of a is",all_a)
print("The allocation of b is",all_b)

print("Hex of a is",hex(a))
print("Hex of b is",hex(b))

def addition(x,y):
    print(x+y)

def subtraction(x,y):
    print(x-y)
    
def multiplication(x,y):
    print(x*y)

def division(x,y):
    print(x/y)

def floor_division(x,y):
    print(x//y)

def modulus(x,y):
    print(x % y)

if c=="+":
    addition(a,b)

elif c=="-":
     subtraction(a,b)
     
elif c=="*":
     multiplication(a,b)

elif c=="/":
     if b!=0:
         division(a,b)
     else:
         print("Cannot divide by zero!")
elif c=="//":
     if b !=0:
         floor_division(a,b)
     else:
         print("Cannot divide by zero!")

elif c=="%":
     if b !=0:
         modulus(a,b)
     else:
         print ("Cannot divide by zero!")

else:
   print("Invalid function!")

            


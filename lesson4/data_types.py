# string data type

# literal assignment
first = "Dave"
last = "Grey"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)
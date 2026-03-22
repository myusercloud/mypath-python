print("Hello world")

#functions
def greet():
    print("Hello from Harrizon")


greet()

def add(a, b):
    return a  + b

result = add(78, 3)
print("The sum is:", result)

#function with parameters

def happy_birthday(name, age):
    print("Happy birthday to", name)
    print("Happy birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you")
    print(f"you are now {age} years old")


happy_birthday("faith", 25)


#function with multiple parameters
def display_invoice(username, amount, due_date):
    print("Hello", username)
    print(f"Your invoice of amount: {amount} is due on {due_date}")


display_invoice("Bro Code", 500, "01/01/2026")

display_invoice("Joash", 50340, "01/01/2026")
display_invoice("Joash", 50340, "01/01/2026")
display_invoice("Joash", 50340, "01/01/2026")
display_invoice("Joash", 50340, "01/01/2026")


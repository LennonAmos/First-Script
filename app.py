name = input("what is your name?")
age = int(input("what is your age?"))
print("Welcome", name, "you are", age)
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a Teenager")
else:
    print("you are a kid")
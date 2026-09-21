
#Ask user for their name
name = input("What's your name? ")

# Remove any leading/trailing whitespace
name = name.strip().title() 

first, last = name.split(" ", 1) if " " in name else (name, "")

#Greet the user
print("Hello, " + name + "!", end =" ")
print("Hello,", name, "!", sep = "")
print(f"Hello, {last}!")
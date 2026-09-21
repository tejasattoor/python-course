def main():
    name = input("Enter your name: ")
    hello(name)

def hello(to="world"):
    print(f"Hello, {to}!")

main()
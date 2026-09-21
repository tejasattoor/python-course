def main():
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    score = int(input("Enter score: "))

    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is less than {y}")
    else:
        print(f"{x} is equal to {y}")

    if x < y or x > y:
        print("X and Y are not equal")
    else:
        print("X and Y are equal")

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

    

main()
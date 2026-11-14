age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 18:
    if marks >=40:
        print("Eligible")
    else:
        print("Failed")
else:
    print("Age requirement not met")
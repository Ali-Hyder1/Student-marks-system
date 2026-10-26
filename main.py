"""x = (int(input("Enter any number: ", ))+1)
for i in range(x):
    if (i%5==0):
        continue
    if (i==x):
        break
    if (i==0):
        continue
    print(i)
    """

"""y = "haider11"

for i in range(1, 6):
    x = input("Enter the password: ", )
    if (x==y):
        print("Access Granted!!".upper().center(10))
        break
    else:
        print("Wrong Password, try again".title().center(50))
        print("Attempt", i, "5")
else:
    print("Access Denied")"""

rage = int(input("Enter Number of students: ",))

for i in range(rage):
    x = input("Enter student name: ").title()
    y = int(input("Enter the student marks: ", ))
    if (y>100) or (y<0):
        print("Invalid Marks")
        continue

    print("===== Final Result =====".center(50))
    print("Student Name: ", x)
    print("Total marks : ", y)
    print("Persentage: ",y ,"%")
    if (y>=80):
        print("A1 Grade")
    elif (y>=70):
        print("A Grade")
    elif (y>=60):
        print("B Grade")
    elif (y>=50):
        print("C Grade")
    elif (y>=40):
        print("D Grade")
    elif (y>=33):
        print("E Grade")
    else:
        print("Fail!!!!")


    
    
        

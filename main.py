def get(subject):
    while True:
        
        x = input("Enter marks of " + subject + ": ")
        if x.strip() == "":
            return 0
        try:
            x = int(x)
        except ValueError:
            print("\tPlease Enter any number!!!!!!!!!!!!!!!")
            continue

        if (x > 100) or (x < 0):
            print("Invalid Marks!!!")
            continue

        return x
def calculate_grade(marks):
    if marks < 33:
        return "Fail"
    elif marks >= 80:
        return "A1"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "E"





while True:
    Name = int(input("Enter Total Number of Students:\t".title(), ))
    if (Name<1):
        print("Please enter at least 1 student!")
        continue

    break

highestmarks = -1
highestname = ""
lowestmarks = 501
lowestname = ""
fail = 0
pas = 0

for i in range(Name):
    
    stu = input("\n\nEnter Student Name:\t".title())
    eng = get("English")
    math = get("Mathematics")
    cs = get("Computer Science")
    urdu = get("Urdu")
    phy = get("Physics")
    total_marks = (eng + math + cs + urdu + phy)
    presentage = float((total_marks / 500 * 100))
    engmarks = calculate_grade(eng)
    mathmarks = calculate_grade(math)
    csmarks = calculate_grade(cs)
    urdumarks = calculate_grade(urdu)
    phymarks = calculate_grade(phy)
    if (eng < 33) or (math < 33) or (phy < 33) or (cs < 33) or (urdu < 33):
        fail = (fail + 1)
        pos = "Fail"
    else:
        pas = (pas + 1)
        pos = "Pass"

    if (presentage < 33) or (pos == "Fail"):
        grade = "Fail!!!"
    elif (presentage >= 80):
        grade = "A1"
    elif (presentage >= 70):
        grade = "A"
    elif (presentage >= 60):
        grade = "B"
    elif (presentage >= 50):
        grade = "C"
    elif (presentage >= 40):
        grade = "D"
    elif (presentage >= 33):
        grade = "E"

    if (total_marks > highestmarks):
        highestmarks = total_marks
        highestname = stu
    if (total_marks < lowestmarks):
        lowestmarks = total_marks
        lowestname = stu
    print("\n\n\n==================== "+ str(stu).upper()+" Marks ====================\n\n")
    print("Name:\t"+ str(stu).center(10).upper())
    print("English Marks:\t"+ str(eng).center(10)+ "\t", float(eng/100*100), "%", str(engmarks).center(10))
    print("Urdu Marks:\t"+ str(urdu).center(10)+ "\t", float(urdu/100*100), "%", str(urdumarks).center(10))
    print("Computer Marks:\t"+ str(cs).center(10)+ "\t", float(cs/100*100), "%", str(csmarks).center(10))
    print("Math Marks:\t"+ str(math).center(10)+ "\t", float(math/100*100), "%", str(mathmarks).center(10))
    print("Physics Marks:\t"+ str(phy).center(10)+ "\t", float(phy/100*100), "%", str(phymarks).center(10))
    print("Total marks:\t"+ str(total_marks).center(10))
    print("Percentage:\t"+ str(presentage)[0:5] + "%" + "\t\tGrade: " + str(grade))
    print("Position:\t"+ str(pos).center(10))


print("\n\n\n==================== Class Performance ====================\n\n")
print("\nNumber of Students Passed:  "+ str(pas).center(10) + "\tNumber of Student Failed:  "+ str(fail).center(10))
print("\nHighest marks taker:  "+ str(highestname).center(10) + "\tHighest Marks:  "+ str(highestmarks).center(10))
print("\nLowest marks taker:  "+ str(lowestname).center(10) + "\tLowest Marks:  "+ str(lowestmarks).center(10))

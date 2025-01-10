# Write a Python program that takes a student's marks in three subjects as input.
# •	If the average is greater than or equal to 90, print "Grade: A".
# •	If the average is between 80 and 89, print "Grade: B".
# •	If the average is between 70 and 79, print "Grade: C".
# •	Otherwise, print "Grade: Fail".

def calculate_grade():
    try:
        subject1 = int(input("Enter marks for subject 1: "))
        subject2 = int(input("Enter marks for subject 2: "))
        subject3 = int(input("Enter marks for subject 3: "))

        if 0 <= subject1 <= 100 and 0 <= subject2 <= 100 and 0 <= subject3 <= 100:
            average = (subject1 + subject2 + subject3) / 3

            if average >= 90:
                print("Grade: A")
            elif 80 <= average <= 89:
                print("Grade: B")
            elif 70 <= average <= 79:
                print("Grade: C")
            else:
                print("Grade: Fail")
        else:
            print("Invalid marks entered. Marks should be between 0 and 100.")

    except ValueError:
        print("Invalid input. Please enter numerical values for marks.")

calculate_grade()

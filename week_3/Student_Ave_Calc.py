choice = "y"

# Loop to repeat the program while the user enters 'y'
while choice == "y":

    # Input the marks for three quizzes as float numbers
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate and display the average of the three quizzes
    average = (quiz_1 + quiz_2 + quiz_3) / 3
    print("Average mark:", average)

    # Check if the average is 50 or above to determine Pass or Fail
    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    # Ask the user if they want to continue for another student
    choice = input("Continue? Select Y/N: ")

print("Program Ended")

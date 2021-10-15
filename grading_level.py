#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program converts Ontario's Grading to percentage


def convert_to_percentage(grade_level):
    # This function converts Ontario's Grading to percentage
    # process & output
    if grade_level == "4+":
        percentage = 97.0
    elif grade_level == "4":
        percentage = 90.5
    elif grade_level == "4-":
        percentage = 83.0
    elif grade_level == "3+":
        percentage = 78.0
    elif grade_level == "3":
        percentage = 74.5
    elif grade_level == "3-":
        percentage = 71.0
    elif grade_level == "2+":
        percentage = 68.0
    elif grade_level == "2":
        percentage = 64.5
    elif grade_level == "2-":
        percentage = 61.0
    elif grade_level == "1+":
        percentage = 58.0
    elif grade_level == "1":
        percentage = 54.5
    elif grade_level == "1-":
        percentage = 51.0
    elif grade_level == "R":
        percentage = 24.5
    else:
        percentage = -1.0

    return percentage


def main():
    # This function is the main function
    # input
    user_input = input("Enter a grade level (Ontario rubric): ")

    # call function
    grade = convert_to_percentage(user_input)
    
    if grade != -1:
        print("The percentage of {0} is {1}%.".format(user_input, grade))
    else:
        print("{0} is an invalid input.".format(user_input))


    print("\nDone.")


if __name__ == "__main__":
    main()

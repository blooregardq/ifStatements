"""Kathryn teaches a science class and her students are required to take three tests. She wants
to write a program that her students can use to calculate their average test score. She also
wants the program to congratulate the student enthusiastically if the average is greater
than 95. Here is the algorithm in pseudocode:
Get the first test score
Get the second test score
Get the third test score
Calculate the average
Display the average
If the average is greater than 95:
Congratulate the user"""

highscore = 95
grade1 = int(input('Enter score for test 1: '))
grade2 = int(input('Enter score for test 2: '))
grade3 = int(input('Enter score for test 3: '))

average = (grade1 + grade2 + grade3) / 3
print(average)

if average >= highscore:
    print('Congtratulations')


"""He has asked you to write a program that will allow a student to enter a test score and then 
display the grade for that score. Here is the algorithm that you will use:
1.  Ask the user to enter a test score.
2.  Determine the grade in the following manner:
If the score is greater than or equal to 90, then the grade is A.
Else, if the score is greater than or equal to 80, then the grade is B.
Else, if the score is greater than or equal to 70, then the grade is C.
Else, if the score is greater than or equal to 60, then the grade is D.
Else, the grade is F."""

gradeA = 90
gradeB = 80
gradeC = 70
gradeD = 60
score = int(input('Enter test score: '))
if score >= gradeA:
    print("Your grade is A")
else:
    if score >= gradeB:
        print("Your grade is B")
    else:
        if score >= gradeC:
            print("Your grade is C")
        else:
            if score >= gradeD:
                print('Your grade is D')
            else:
                if score < 60:
                    print('Your grade is F')

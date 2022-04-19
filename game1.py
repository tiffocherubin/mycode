#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""
score = int(input(" Enter a valid score inferior or equal to 100: "))

if score:
    if score <= 100:
        if score <= 100 and score >=90:
            print("\nyour grade: A")
        if score < 90 and score >=80:
            print("\nyour grade: B")
        if score < 80 and score >=70:
            print("\nyour grade: C")
        if score < 70 and score >=60:
            print("\nyour grade: D")
        if score < 60:
            print("\nyour grade: F")
    else:
        print("\nYour score is not valid")
else:
    print(" You didn't enter your score")
print("\nGrade table :\n  A (100 to 90)\n  B (89 to 80)\n  C (79 to 70)\n  D (69 to 60)\n  F (59 and below)")

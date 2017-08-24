"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        try:
            score = float(input("Invalid score"))
        except ValueError:
            score = float(input("Enter a number"))
    print(calculate_score(score))


def calculate_score(score):
    if score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")

main()

marks = int(input("enter your marks "))

print("entered marks", marks)


if marks >= 90:
    print("you have achieved A+ Grade")
elif marks >= 80:
    print("you have achieved A Grade")
elif marks >= 70:
    print("you have achieved B Grade")
elif marks >= 60:
    print("you have achieved C Grade")
elif marks >= 50:
    print("you have achieved D Grade")
elif marks >= 35:
    print("you have passed this examination")
else:
    print("you have failed this examination better luck next time!!!")

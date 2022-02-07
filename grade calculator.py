sub1=int(input("Enter marks of the first subject: "))

sub2=int(input("Enter marks of the second subject: "))

sub3=int(input("Enter marks of the third subject: "))

sub4=int(input("Enter marks of the fourth subject: "))

sub5=int(input("Enter marks of the fifth subject: "))

average=(sub1+sub2+sub3+sub4+sub4)/5

if average >= 90:
    print("Grade: A")
elif average >= 80 and average < 90:
    print("Grade: B")
elif average >= 70 and average < 80:
    print("Grade: C")
elif average >= 60 and average < 70:
    print("Grade: D")
else:
    print("Grade: E")

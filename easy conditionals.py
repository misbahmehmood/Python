maths_mark = int(input("maths mark: "))
chemistry_mark = int(input("chemistry mark: "))
physics_mark = int(input("physics mark: "))
overall_mark= maths_mark + chemistry_mark + physics_mark
percentage = (overall_mark/10)*100

if percentage < 40:
    print("Fail")
elif percentage >= 40:
    print("D")
elif percentage >= 50:
    print("C")
elif percentage >=60:
    print("B")
elif percentage >=70:
    print("A")

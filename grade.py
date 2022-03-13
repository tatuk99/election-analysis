user_input = int(input("What is the grade?"))
if user_input >= 90:
    print('A! Good job')
else:
    if user_input >=80:
        print('Your grade is a B')
    else:
        if user_input >= 70:
            print('Your grade is a C')
        else:
            if user_input >=60:
                print('Your grade is a D')
            else:
                print('Fail')
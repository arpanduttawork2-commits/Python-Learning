def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False




inp=input().strip(' ')
if(len(inp)==1):
    if (inp.isalpha()):
        print('Alphabet')
    elif inp.isdigit():
        print('Digit')
    else:
        print("Special Character")
else:
    if(inp.isalpha()):
        print("Word")
    elif is_number(inp):
        print("Number")
    elif inp.isalnum():
        print("Alphanumeric")
    else:
        print("Other(With special characters)")

#Checking for leap year
year=int(input())
if(year %100 ==0):
    if year%400==0:

        print(f"{year} is leap")
    else:
        print(f"{year} isn't leap")
else:
    if(year%4==0):
        print(f"{year} is leap")
    else:
        print(f"{year} is not leap")

    
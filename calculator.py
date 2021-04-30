choice=input("choose +,-,/,*: ")
if choice == "+":
    x=input("First num:  ")
    y=input("second num: ")
    sumresult=(int(x)+int(y))
    print(sumresult)

elif choice == "-":
    z=input("First num:  ")
    s=input("second num: ")
    diffrenceresult=(int(z)-int(s))
    print(diffrenceresult)

if choice == "/":
    a=input("First num:  ")
    w=input("second num: ")
    divideresult=(int(a)/int(w))
    print(divideresult)

elif choice == "*": 
    b=input("First num:  ")
    v=input("second num: ")
    multiplyresult=(int(b)*int(v))
    print(multiplyresult)   
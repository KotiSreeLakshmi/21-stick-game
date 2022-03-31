# program to perform 21 match stick game
m=21
user=0
comp=0
while m!=1:
    print("Number of match sticks:",m)
    user=int(input("please enter 1 or 2 or 3 or 4:"))
    print("my num is:",5-user)
    print("Match sticks left:",user+5-user)
    comp=5-user
    m=m-user-comp
   
if m==1:
    print("Computer Win!!!!!!!!!!!!!!!!!")

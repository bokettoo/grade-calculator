n1 = float(input("enter the first mark : "))
n2 = float(input("enter the second mark : "))
n3 = float(input("enter the third mark : "))

gpa = int((n1+n2+n3)/3)
if gpa>16 :
   print(f"{gpa} tres bien")
elif gpa<16  and gpa>14: 
   print(f"{gpa} bien")
elif gpa<14  and gpa>12: 
   print(f"{gpa} assez bien")
elif gpa<12  and gpa>10: 
   print(f"{gpa}passable")
elif gpa<10: 
   print(f"{gpa} insufissant")
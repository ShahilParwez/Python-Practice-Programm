print("\nWelcome to Grade Sorter App")

grades=[]

grade=int(input("\nWhat is your First Grade (0-100):"))
grades.append(grade)
grade=int(input("What is your Second Grade (0-100):"))
grades.append(grade)
grade=int(input("What is your Third Grade (0-100):"))
grades.append(grade)
grade=int(input("What is your Fourth Grade (0-100):"))
grades.append(grade)

print("\nyour Grades are:"+ str(grades))
grades.sort(reverse=True)
print("\nYour grades from highest to lower are:" +str(grades))

print("\nThe lowest two grades will now be dropped.")
removed_grade=grades.pop()
print("Removed grade :"+ str(removed_grade))
removed_grade=grades.pop()
print("Removed grade :"+ str(removed_grade))

print("\nYour remaining grades are :"+str(grades))
print("Nice Work! Your highest grade is "+str(grades[0])+".")

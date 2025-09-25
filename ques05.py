# Problem 5: Student Attendance Manager
# • Read a file attendance.txt containing roll numbers, one per line (who attended today).
# • Maintain a master list of all roll numbers in a Python list.
# • Compare and print:
# o “Present” students (roll numbers in file)
# o “Absent” students (roll numbers not in file)
# • Save the absent list to absent.txt.

list=[1,3,4,5,6]
set1=set(list)

# creating master list
f= open("17sep/attendence.txt")
b=f.read().strip()
c=b.split()
set2=set()

for i in c:
    set2.add(int(i))
# finding absent student
a=set2-set1
# print(set2)
print(a)

g=open("17sep/absent.txt","w")
h=g.write("")
g.close()


# updating to absent list
for i in a:
    g=open("17sep/absent.txt","a")
    h=g.write(f"{i} - Absent\n")
    g.close()

# printing output
l=open("17sep/absent.txt")
x=l.read()
print(x)

            

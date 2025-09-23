# Problem 4: Unique Numbers & Statistics
# • Ask the user to input numbers separated by spaces.
# • Store them in a set to remove duplicates.
# • Compute and print:
# o Total count of unique numbers
# o Sum
# o Average
# o Largest & smallest number

# Example:
# Enter numbers: 5 3 9 3 9 1
# Unique numbers: {1, 3, 5, 9}
# Count=4, Sum=18, Avg=4.5, Max=9, Min=1

nums=(input("enter your no. separated by space : ").strip())
num=set(nums.split(" "))
numm=[]
print(num)
print(f"total count of unique no. : {len(num)} ")
sum=0
for i in num:
    numm.append(int(i))
    sum+=int(i)
print("your total sum : ",sum)
print("your average : ",sum/len(num))
print(numm)
numm.sort()
print("your max no is : ",numm[-1])
print("your min no is :",numm[0])
# Problem 2: Word Frequency Filter
# Write a Python program that:
# • Reads a text file story.txt.
# • Counts how many times each word appears (ignore case, strip punctuation).
# • Prints only the words whose frequency is greater than a user-entered number n,
# sorted in descending order of frequency.
# Example output:
# Enter minimum frequency: 3
# Word frequencies ≥ 3:
# the → 12
# and → 5
# python → 4
n=int(input("enter your frequency :--"))
with open("17sep/story.txt","r") as f:
    a=f.read()
b=a.split()
c=[]
for i in b:
    if "," in i:
        continue
    else:
        c.append(i)
dict={}
for i in c:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
    
for i in dict:
    if dict[i]>=n:
        print(i,dict[i],"\n")

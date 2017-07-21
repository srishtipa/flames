print ("THE GAME IS FLAMES")
print ("enter 1st name")
name1=input()
print ("enter the 2nd name")
name2=input()
print ("the two names are")
print(name1) 
print(name2)
len1=len(name1)
len2=len(name2)
match=0
for i in range(len(name1)):
    for j in range(len(name2)):
        if name1[i]==name2[j]:
          list1=list(name1)
          list1[i]='#'
          name1=''.join(list1)
          list2=list(name2)
          list2[j]='#'
          name2=''.join(list2)
          match=match+2
          break
print(name1)
print(name2)
total_length=len1+len2 
unmatched=total_length-match
print(unmatched)

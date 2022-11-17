s=input()
z_count=0
o_count=0
# if s[-1]=="0" and s[-2]=="1":
#     z_count+=1
    
# elif s[-1]=="1" and s[-2]=="0":
#     o_count+=1
if s[-1]=="0":
    s+="1"
elif s[-1=="1"]:
    s+="0"

for i in range(len(s)-1):
    if s[i]=="0" and s[i]!=s[i+1]:
        o_count+=1
    elif s[i]=="1" and s[i]!=s[i+1]:
        z_count+=1
print(min(o_count,z_count))


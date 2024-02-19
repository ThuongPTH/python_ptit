# # Viết chương trình tìm các số vừa tìm được chia hết cho 5 và 7, số đó nằm trong 1500, 2700

# for i in range(1500, 2701, 5):
#     if i%7==0:
#         print(i)
            
# s= "asdgakjsdghkjasg 242412"
# num=0
# alpha=0
# for c in s:
#     if c.isdigit():
#         num+=1
#     elif c.isalpha():
#         alpha+=1
# print


# import re

# reg = "(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$])(?=.*\d)"
# passw = input()
# if re.match(reg, passw): print("True")
# else: print("False")

def giaithua(n):
    rs=1
    for i in range(1,n+1):
        rs*=i
    return rs

def dequy(n):
    if n==1 or n==0: return 1
    else: return n*dequy(n-1)

n = int(input())
print(giaithua(n))
print(dequy(n))
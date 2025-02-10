# 9. Palindrome Number

num=121
rev=0
for i in range(num):
    if num!=0:
        b=num%10
        num=num//10
        rev=rev*10+b
if num==1:
    print(rev,'is not a palindrome')
else:
    print(rev,'is a palindrome')

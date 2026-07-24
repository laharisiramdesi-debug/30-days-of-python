#return sum of two numbers
def sum(a,b):
    return a+b
print(sum(4,5))
#return largest number
def largest(a,b):
    if a>b:
        return a
    else:
        return b
print(largest(4,5))
#return reverse of a string
def reverse(s):
     return s[-1::-1]
s1=input("enter string:")
print(reverse(s1))
#return length of a list
def length(l):
    count=0
    for i in l:
        count+=1
    return count
a=input("enter list:").split()
print(length(a))
#return avg of numbers
def avg(a,b,c):
    return (a+b+c)/3
print(avg(4,5,6))
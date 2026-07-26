#with sort method
lists=list(map(int,input("enter list:").split()))
lists.sort()
print("ascending order:",lists)
lists.sort(reverse=True)
print("descending order:",lists)
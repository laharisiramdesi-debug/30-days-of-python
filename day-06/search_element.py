lists=list(input("enter list:").split())
element=(input("enter search element:"))
if element in lists:
    print("element found")
else:
    print("element not found")
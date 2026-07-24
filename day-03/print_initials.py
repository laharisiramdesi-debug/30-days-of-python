word=input("enter a word:")
splitting=word.split()
initials=""
for w in splitting:
    initials += w[0].upper()+"-"
print("initials:",initials)
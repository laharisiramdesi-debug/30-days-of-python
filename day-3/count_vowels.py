word=input("enter word:").lower()
vowels="aeiou"
print(f"no. of vowels:{sum(word.count(v) for v in vowels)}")
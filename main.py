from convertor import to_morse, to_english


e = input("Enter the string you want to convert to morse: ").lower()
m = input("Enter the string you want to convert to english: ").lower()
morse = to_morse(e)
english = to_english(m)

if not morse:
    print("please try again")
    english = input("Enter the string you want to convert to morse: ").lower()

print(morse)
print(english)

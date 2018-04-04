
def is_palindrom(text):
    forbiden = ('.', ',', '!', '?', '-', ';', ' ')
    new_text = text.lower()
    print(new_text)
    text2 = ""
    for letter in new_text:
        if letter not in forbiden:
            text2 += letter

    print(text2)
    return text2 == text2[::-1]

some = input('Enter text: ')
if (is_palindrom(some)):
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")

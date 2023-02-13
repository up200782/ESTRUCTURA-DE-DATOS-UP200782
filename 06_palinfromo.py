def is_palindrome(word):
    word = word.replace(" ", "")
    for i in range(len(word)//2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True

word = input("Give me a word: ")
if is_palindrome(word):
    print("Es palíndromo")
else:
    print("No es palíndromo")
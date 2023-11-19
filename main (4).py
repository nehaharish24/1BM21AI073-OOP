#get al palindromes in a string
def is_palindrome(s):
    return s == s[::-1]

def get_palindrome(text):
    palindromes = []
    words = text.split()

    for word in words:
        if is_palindrome(word):
            palindromes.append(word)

    return palindromes

print("enter the sentence")
input_string = input()
result = get_palindrome(input_string)

print("Palindromes in the string:")
print(result)
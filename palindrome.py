users_sentence = input("Enter your palindrome: ")

#Removing spaces, punctuation, and capitalization
users_sentence = users_sentence.replace(" ", "")
users_sentence = users_sentence.lower()
punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
new_string = ""
for i in users_sentence:
    if i not in punctuation:
        new_string = new_string + i

#Iterative method
i = 0
while i < int(len(new_string)/2):
    if new_string[i] == new_string[-1*(i + 1)]:
        i += 1 
    else:
        print("It is not a palindrome")
        break      
if i >= (int(len(new_string)/2)):
    print("It is a palindrome")

#Recursive method
# def check_string(palindrome):   
#     if len(palindrome) <= 1:
#         return "It is a palindrome"     
#     else:
#         if palindrome[0] == palindrome[-1]:
#             return check_string(palindrome[1:-1])   
#         else:
#             return "It is not a palindrome"

# print(check_string(new_string))

#Definitely the easiest way
# if new_string == new_string[::-1]:
#     print("Yup!")
# else:
#     print("Nope!")

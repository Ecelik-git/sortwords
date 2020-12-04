'''this program will print words in order
@codingwithec'''
#getting input from users
string=input("Enter a sentence or list of words: ")
#breaking down the string into words
string_sep = string.split()
#sorting words alphabetically 
string_sep.sort()
#printing each word
for i in string_sep:
    print(i, end="-")


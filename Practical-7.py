fh = open('prac-7.txt','w')
word=input("Enter a word to check for palindrome :")
if(word==word[::-1]): 
    fh.write("The letter is a palindrome") 
else: 
    fh.write("The word is not a palindrome")
fh.close()

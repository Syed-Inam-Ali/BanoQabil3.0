#Check if a String is Palindrome or Not:


phrase_word = str(input("Enter a word OR Phrase: "))
#for i in range(1,len(phrase_word)+1):
if phrase_word == phrase_word[::-1]:
     print("its a plain drom")
else:
        print("its not a plain drom")

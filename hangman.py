import random
import string
word = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
def get_valid_word(words):
    word= random.choice(words) #to randomly choose something
    while '-' in word or '' in word:
        word =random.choice(words)
    return word
def hangman():
    word =get_valid_word(words)
    word_letters =set(word) # to get letters in the words
    alphabet =(string.ascii_uppercase)
    used_letters = set() #what one has guessed

    #for getting input
    while len(word_letters) >0:
        #this shows the letters used
        #''.join(['a','b','cd'])-->'abcd'
        print('you have used these letters:',''.join(used_letters))
       #knowing the current word is (to-w n)  
    word_list =[letter if letter in used_letters else '-'for letter in words]
    print('Current word:',''.join(word_list))  

    user_letter =input('Guess a letter:').upper()
    if user_letter in alphabet- used_letters:
        used_letters.add (user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    elif user_letter in used_letters: 
        print('you have already used the character. try again.')      

    else:   
        print('invalid character. please try again.')
    print(user_input)     
hangman()

    


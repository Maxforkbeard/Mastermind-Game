from random import randint

secret1 = randint(1,9)
secret2 = randint(1,9)
secret3 = randint(1,9)
secret4 = randint(1,9)

secret1 = str(secret1)
secret2 = str(secret2)
secret3 = str(secret3)
secret4 = str(secret4)

secretmain = secret1 + secret2 + secret3 + secret4
secretmain = int(secretmain)

secret1 = int(secret1)
secret2 = int(secret2)
secret3 = int(secret3)
secret4 = int(secret4)


import sys
import time

#lopper for the BOOM
looper = 0

#fastprint
def fastprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./20)


#slowprint
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)
    

  # Clear
def clear():
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')
    
#slowprinting
def slowprinting(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./8)

#slowestprint
def slowestprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./1)

if __name__ == "__main__":
  slowprinting("Hello agent")
print("")
slowprint("You have been selected for a high class building job inside our glorious nation of Atricovich,")
print("")
slowprint("What is this mission you ask?")  
print("")
slowprint("It is called S.A.F.E.S.")
print("")
slowprint("S.A.F.E.S, is a code that means, Super Anialating Fenel, Easialy Sacriligious")
slowprinting("Are you up for the challange?")
slowprint("Please type 1 for yes, and 2 for no")
slowprint("Any other intiger will have you terminated!")

yesorno = input()
yesorno = int(yesorno)



if yesorno == 1:
 clear()
 slowprint("Welcome to S.A.F.E.S.")
 slowprint("You have to guess a number from 1 to 9 (0 means its wrong)")
 guess = int(input("Guess the first digit: "))
 guess2 = int(input("Guess the second digit: "))
 guess3 = int(input("Guess the third digit: "))
 guess4 = int(input("Guess the fourth digit: "))

 guess = str(guess)
 guess2 = str(guess2)
 guess3 = str(guess3)
 guess4 = str(guess4)

 guessmain = guess + guess2 + guess3 +guess4
 guessmain = int(guessmain)
 guess = int(guess)
 guess2 = int(guess2)
 guess3 = int(guess3)
 guess4 = int(guess4)

 if (guess == secret1) and (guess2 == secret2) and (guess3 == secret3) and (guess4 == secret4) :
   print("fluke")
 else:
  numguesses = 0
   

 while numguesses < 12: 
   print ("wrong numbers") 
   numguesses = numguesses + 1
   numguesses = int(numguesses)
   if guessmain != secretmain:
     wrong1 = 0
     wrong2 = 0
     wrong3 = 0
     wrong4 = 0
     wrongmain = 0
     wrongmain = str(wrongmain)

     if guess == secret1:
       wrong1 = secret1
       wrong1 = str(wrong1)
     else:
       wrong1 = str(wrong1)
       wrong1 = 0
       wrong1 = str(wrong1)
    
     if guess2 == secret2:
       wrong2 = str(wrong2)
       wrong2 = secret2 
       wrong2 = str(wrong2)
     else:
       wrong2 = 0
       wrong2 = str(wrong2)

     if guess3 == secret3:
       wrong3 = str(wrong3)
       wrong3 = secret3
       wrong3= str(wrong3)
     else:
       wrong3 = 0
       wrong3 = str(wrong3)

     if guess4 == secret4:
       wrong4 = secret4
       wrong4 = str(wrong4)
     else:
       wrong4 = str(wrong4)
       wrong4 = 0
       wrong4 = str(wrong4)
    

     wrongmain = wrong1 + wrong2 + wrong3 + wrong4
     wrongmain = str(wrongmain)
     print("But you did get ", wrongmain, "digit(s) right (0  menas no, sorry for the inconvineience")
     guess = int(input("Guess the first digit: "))
     guess2 = int(input("Guess the second digit: "))
     guess3 = int(input("Guess the third digit: "))
     guess4 = int(input("Guess the fourth digit: "))

     guess = str(guess)
     guess2 = str(guess2)
     guess3 = str(guess3)
     guess4 = str(guess4)

     guessmain = guess + guess2 + guess3 +guess4
     guessmain = int(guessmain) 
     print(guessmain) 

     guess = int(guess)
     guess2 = int(guess2)
     guess3 = int(guess3)
     guess4 = int(guess4)

     if guessmain == secretmain:
       numguesses == 100
  
 if guessmain == secretmain:
   clear()
   slowprint("Thats right, contgratulations, you are a S.A.F.E.S. craking genius!")
   slowprint ("Thankyou for playing, I hope you enjoyed it, pleases give me feed back, and I will continue to imporve on it. Goodbye")
   time.sleep(4)
   clear() 
   print("________   ________  ________    ___       ___  ")
   print("|      /   |      |  |      |    |  \     /   | ")
   print("|-----|    |      |  |      |    |   \   /    | ")
   print("|      \   |      |  |      |    |    ___     | ")
   print("________   ________  ________    |            | ")

 elif numguesses == 12:
   clear()
   slowprint("I'm sorry but you have run out of guesses")
   slowprint("I hope you will retry and get the right answers now, or else, this glorious nation will be doomed FOREVER.")
   time.sleep(4)
   clear()
   print("________   ________  ________    ___       ___  ")
   print("|      /   |      |  |      |    |  \     /   | ")
   print("|-----|    |      |  |      |    |   \   /    | ")
   print("|      \   |      |  |      |    |    ___     | ")
   print("________   ________  ________    |            | ")

 #Redundency 101
 else:
   slowprint("If you can access this there is something wrong with the earth and you, The Matrix is falling apart, get out while you still can")
   time.sleep(2)
   slowprint("And if you have extra time, try to wake everybody who is near and dear to you out, they are in danger if you get out")
   time.sleep(2)
   slowprint("Please help us")
   time.sleep(1)
   slowprint("Neo")



elif yesorno == 2:
  k = 0
  while k == 0:
   clear()
   slowprint("Are you sure?")
   slowprint("Please type 1 for yes, and 2 for no")
   slowprint("Anything other input will have you terminated!")
   UselessAnswer = input()
   UselessAnswer = int(UselessAnswer)

else:
  clear()
  slowprint("That is not a valid answer")
  slowprint("You will be TERMINATED in...")
  clear()
  slowestprint("...3")
  clear()
  slowestprint("...2")
  clear()
  slowestprint("...1")
  clear()
  slowprint("This may hurt your eyes")
  time.sleep(1)
  while looper == 0:
   clear()
   print("________   ________  ________    ___       ___  ")
   print("|      /   |      |  |      |    |  \     /   | ")
   print("|-----|    |      |  |      |    |   \   /    | ")
   print("|      \   |      |  |      |    |    ___     | ")
   print("________   ________  ________    |            | ")
  
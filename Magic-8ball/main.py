from getopt import gnu_getopt
import random
#name = "Brad"
name = input("What is your name? ")
#question = "Will I win the lottery"
question = input("What is your question? ")
answer = ""
random_number = random.randint(1,10)

if random_number == 1:
  answer = "Yes - definately."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Outlook not so good."
elif random_number == 10:
  answer = "No Fucking Way."
else:
  answer = "Error"


if name == "":
  print("Magic 8-Ball's answer: " + answer)
elif question == "":
  print("Without a question the very fabric of reality it at risk")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

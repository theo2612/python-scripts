from getopt import gnu_getopt
import random
#name = "Brad"
name = input("What is your name? ")
#question = "Will I win the lottery"
question = input("What is your question? ")

answers = [
  "Yes - definately.",
  "It is decidedly so.",
  "Without a doubt.",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you now.",
  "My sources say no.",
  "Outlook not so good.",
  "No Fucking Way."
]

answer = random.choice(answers)

if name == "":
  print(f"Magic 8-Ball's answer: {answer}")
elif question == "":
  print("Without a question the very fabric of reality it at risk")
else:
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer: {answer}")

#imports and addons
import time
import turtle
wn = turtle.Screen()
cafe ="starbucks background - Copy.gif"
wn.bgcolor("black")
wn.bgpic(cafe)
ohno = "worried clyde.gif"
yay = "blushing clyde.gif"
normal = "clydeeghost.gif"

#The text stuff
font = ( "Comic sans", 35, "bold")
Clyde = turtle.Turtle()
Clyde.up()
Clyde.goto(0,-300)
Clyde.down()
Clyde.ht()
for_else = "Please enter a valid responce"

#introduction
time.sleep(3)
wn.addshape(normal)
time.sleep(2)
player = input ("Oh hello! My name is Clyde. What's yours?")
Clyde.write("It's nice to meet you",player)
Clyde.clear()
#There will be a point system depending on your answer 
global baddate
baddate = 0

#Start of questions
time.sleep(3)
Clyde.write ("I've never done a blind date before. Especally one my friend Pinky sets up. I'm pretty excited and nervous to meet you.")
time.sleep(2)
start = input ("I'm sorry if I'm really fidgety. ('I'm nervous too' / 'You're the first of 5 dates I have today'", font = font)
if start == "I'm nervous too":
    Clyde.write("Oh thank god. I thought I would be the only one.")
elif start == "You're the first of 5 dates I have today":
    Clyde.write("Oh, well I guess you're not good with dates either?")
    baddate += 1
else:
    Clyde.write(for_else)

#question about breakfast
time.sleep(3)
Clyde.write ("Anyway, I thought I'd be a gentlemen and pay for some breakfast.")
time.sleep(2)
food = input("What do you wanna eat? 'Pancakes' / 'The souls of the innocent'", font = font)
if food == "Pancakes":
    Clyde.write("Oh I love pancakes! Think I'll get the same.")
elif food == "The souls of the innocent":
    Clyde.write("Oh fuuu- I mean...Haha funny, umm...I was just gonna get some fruit...I'll let you tell the waiter what you want.")
    baddate+=1
else:
    Clyde.write(for_else)

#Quick story
time.sleep(3)
Clyde.write("*A waiter comes to take your order*")

#College question
time.sleep(3)
Clyde.write("So, while we're waiting here, I was curious. You and Blinky are in classes together right?")
time.sleep(2)
classes = input("What are you going to college for? 'Computer Science' / 'How to get away with murder'", font = font)
if classes == "Computer Science":
    Clyde.write("Oh really! Me too! Maybe that's why Inky thought this was a good idea. I'm trying to make video games.")
elif classes == "How to get away with murder":
    Clyde.write("...So ah...you study crime? Like investigations? Tha-that's cool...as long as you like what you're um...studying.")
    baddate+=1
else:
    Clyde.write(for_else)

#player question
time.sleep(5)
Clyde.write("So I feel like I'm talking a lot.")
time.sleep(2)
question = input("Did you wanna ask me somthing? 'Do you believe in ghost?' / 'What's a hobby you have?'")
if question == "What's a hobby you have?":
    Clyde.write("Well I do a lot of exercise. Other than that, I usually just study for school. Though I'm kind of bad at school. My friends nicknamed me Stupid.")
elif question == "Do you believe in ghost?":
    Clyde.write("...Aaaaaahhhhhh...well um...I ah...I don't wanna talk about that.")
    baddate+=1
else:
    Clyde.write(for_else)

#More story
time.sleep(3)
Clyde.write("Umm, sorry. I think I made this a bit sad. Oh, look at that. The waiter's coming.")
time.sleep(2)
Clyde.write("*The waiter brings your food. You two end up chating about the restuarant you're in. It's a small, but nice cafe.*")

#Your opinion
time.sleep(5)
Clyde.write("So I was wondering...")
time.sleep(2)
opinion = input("What did you think of this date? 'I liked it' / 'Meet me in the dark ally'", font = font)
if opinion == "I liked it":
    Clyde.write("Well I'm glad you enjoyed it. I think it was an interesting date.")
elif opinion == "Meet me in the dark ally":
    Clyde.write("I ah... I don't like dark, and enclosed places. ... So cold...")
    baddate+=1
else:
    Clyde.write(for_else)

time.sleep(3)
if baddate < 3:
   Clyde.write("I really liked this date. Here, it's my number. Pinky told me you two have classes together, so maybe we can talk about a second date when you're done with class. Anyway, I'll let you go. See you soon!") 
else:
    Clyde.write("I have to be honest though. I didn't like this date. I'm just gonna go, I'm sorry if I disappointed you, but I don't want a second date.")


wn.mainloop()
from turtle import Turtle, Screen
import random 

WIDTH_FROM_CENTER = 250

colors  = ["red","orange", "pink", "green", "blue", "purple"]

def create_turtles():
    bots = []
    height = 60
    space = 30
    for color in colors:
        bot = Turtle()
        bot.shape("turtle")
        bot.color("red")
        bot.penup()
        bot.color(color)
        bot.goto(x = -WIDTH_FROM_CENTER, y = height)
        bots.append(bot)
        height -= space
    return bots

# game status
has_started= False
is_over = False
# Screen setup
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which bot will win the race? Enter the bot's color: ")

if(user_bet):
    has_started = True
    
# Initialize bot
bots = create_turtles()
while(has_started):
    random_dist = random.randint(0, 10)
    current_bot = bots[random.randint(0, len(colors)-1)]
    current_bot.forward(random_dist)
    if(current_bot.xcor() > WIDTH_FROM_CENTER - (current_bot.width()/2)):
        color = current_bot.pencolor()
        if( color == user_bet):
            print(f"You've won the bet! The {color} bot has win the race!")
        else:
            print(f"You've lost the bet! The {color} bot has win the race!")
        has_started = False
        #is_over = True

# screen will listen to any event when the program start
screen.listen()


# exit the gui when on
screen.exitonclick()
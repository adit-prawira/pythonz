import turtle as t
import colorgram
import random


print("1 - draw random motion\n2 - draw spirograph\n3 - hirst painting")
option = int(input("Enter computation option: "))
bot = t.Turtle()

bot.speed("fastest")
bot.hideturtle()
t.colormode(255)

#Directions:  E   N   W    S
directions = [0, 90, 180, 270,]

def generate_random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_path():
    bot.pensize(15)
    for _ in range(200):
        bot.color(generate_random_rgb())
        bot.forward(30)
        bot.setheading(random.choice(directions))

def draw_spirograph():
    n_gaps = int(input("Enter number number of gaps between circles: "))
    
    # draw spirograph in 1 revolution
    for _ in range(int(360/n_gaps)):
        bot.color(generate_random_rgb())
        bot.circle(100)
        bot.setheading(bot.heading() + n_gaps)
        
def hirst_painting():
    n_dots = 100
    rgb_colors = []
    colors = colorgram.extract("image.jpg", 30)
    bot.penup()
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    
    # initialize position of the bot
    bot.setheading(225)
    bot.forward(250)
    bot.setheading(0)
    
    for i in range(1, n_dots+1):
        bot.dot(20, random.choice(rgb_colors))
        bot.forward(50)
        if(i%10 == 0):
            bot.setheading(90)
            bot.forward(50)
            bot.setheading(180)
            bot.forward(500)
            bot.setheading(0)
if(option == 1):
    random_path()
elif(option ==2):
    draw_spirograph()
elif(option == 3):
    hirst_painting()
else:
    print("Invalid key\n")
    
screen = t.Screen()
screen.exitonclick()
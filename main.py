from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Who will win the race? Enter a color: ")
print(f"You placed your bet on {user_bet}.")
y_positions = [75, 45, 15, -15, -45, -75]
turtle_colors = ["purple", "blue", "green", "yellow", "orange", "red"]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[i])
    new_turtle.penup()
    new_turtle.setpos(-230, y_positions[i])
    all_turtles.append(new_turtle)

continue_race = True
winner = user_bet
while continue_race is True:
    for turtle in all_turtles:
        turtle.forward(random.randrange(10))
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            continue_race = False
            winner = turtle.pencolor()

if user_bet == winner:
    print(f"You win! The {winner} turtle is the winner!")
else:
    print(f"You lost! The {winner} turtle is the winner!")

screen.exitonclick()
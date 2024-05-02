from turtle import Turtle,Screen
import random
race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet..!",prompt="Which turtle will win? Choose a color..!")
print(user_bet)

colors = ["red","blue","green","yellow","orange","purple"]
tutle_y_position = [150,100,50,-50,-100,-150]
all_turtles = []

for turtle_index in range(0,6):
  tt = Turtle(shape="turtle")
  tt.color(colors[turtle_index])
  tt.penup()
  tt.goto(x=-230,y=tutle_y_position[turtle_index])
  all_turtles.append(tt)


if user_bet:
  race_on = True


while race_on:
  for turtle in all_turtles:
    if turtle.xcor()>=210:
      race_on = False
      winner = turtle.pencolor()
      if winner == user_bet:
        print(f"You win!,{winner} turtle is the winner.")
      else:
        print(f"You loose!,{winner} turtle is the winner.")
    random_pace = random.randint(0,10)
    turtle.forward(random_pace)






screen.exitonclick()
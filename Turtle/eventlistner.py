from turtle import Turtle,Screen

tt = Turtle()
screen = Screen()
def move_forward():
  tt.forward(20)

def move_backward():
  tt.backward(20)

def turn_left():
  new_heading = tt.heading()+10
  tt.setheading(new_heading)
def turn_right():
  new_heading = tt.heading()-10
  tt.setheading(new_heading)

def clear_drawing():
  tt.clear()
  tt.penup()
  tt.home()
  tt.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear_drawing,"c")
screen.exitonclick()
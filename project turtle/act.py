import turtle

screen = turtle.Screen()
screen.bgcolor("white")

board = turtle.Turtle()
board.shape("turtle")
board.color("blue")
board.speed(2)


for _ in range(4):
    board.forward(100) 
    board.left(90)    

turtle.done()


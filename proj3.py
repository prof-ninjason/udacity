import turtle

def open_window():
    window = turtle.Screen()
    window.bgcolor("blue")
    
#def create_brad():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(1)
    
#def move_brad(brad):
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)

# def draw_sq():
#     open_window()
#     brad = create_brad()
#     move_brad(brad)
    window.exitonclick()

open_window()
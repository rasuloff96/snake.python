import turtle
import time
import random

# Oynani sozlash

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("white")
window.setup(width=600, height=600)
window.tracer(0)



# Ilon boshini yaratish

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 1)
head.direction = "stop"



# Ovqat yaratish

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


segments = []



# Boshqarish funksiyalari

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
        
# Tugmalarni boglash
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")



# Oyin sikli

while True:
    window.update()
    
    # Devorga urilishni tekshirish
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Segmentlarni yashirish
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Segmentlar ro'yxatini tozalash
        segments.clear()
        
    # Ovqatga yeyishni tekshirish
    if head.distance(food) < 20:
        # Ovqatni yangi joyga qo'yish
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Segment qo'shish
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
    # Tanani ilon boshidan ketidan harakatlantirish
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    time.sleep(0.1)
import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dragon")
screen.tracer(0)

segments = []
positions = [(0, 0)] * 200
segment_count = 50

for i in range(segment_count):
    t = turtle.Turtle()
    t.shape("circle")
    if i == 0:
        t.color("red")
        t.shapesize(3)
    else:
        t.color("white")
        scale = max(0.2, 1 - i * 0.02)
        t.shapesize(scale)
    t.penup()
    t.speed(0)
    segments.append(t)

legs = []
leg_interval = 3
for i in range(1, segment_count, leg_interval):
    leg_pair = []
    for side in [-1, 1]:
        leg = turtle.Turtle()
        leg.shape("triangle")
        leg.color("gray")
        leg.shapesize(0.3, 1)
        leg.penup()
        leg.speed(0)
        leg_pair.append((leg, side))
    legs.append((i, leg_pair))

left_wing = turtle.Turtle()
left_wing.shape("triangle")
left_wing.color("darkred")
left_wing.shapesize(5, 8)
left_wing.penup()
left_wing.speed(0)

right_wing = turtle.Turtle()
right_wing.shape("triangle")
right_wing.color("darkred")
right_wing.shapesize(5, 8)
right_wing.penup()
right_wing.speed(0)

left_eye = turtle.Turtle()
left_eye.shape("circle")
left_eye.color("yellow")
left_eye.shapesize(0.3)
left_eye.penup()
left_eye.speed(0)

right_eye = turtle.Turtle()
right_eye.shape("circle")
right_eye.color("yellow")
right_eye.shapesize(0.3)
right_eye.penup()
right_eye.speed(0)

bonus_items = []

def create_bonus():
    for _ in range(10):
        b = turtle.Turtle()
        b.shape("circle")
        b.color("green")
        b.shapesize(0.5)
        b.penup()
        x = random.randint(-screen.window_width()//2 + 50, screen.window_width()//2 - 50)
        y = random.randint(-screen.window_height()//2 + 50, screen.window_height()//2 - 50)
        b.goto(x, y)
        bonus_items.append(b)

head = segments[0]
t = 0

def update():
    global t
    x = screen._root.winfo_pointerx() - screen._root.winfo_rootx() - screen.window_width() / 2
    y = screen.window_height() / 2 - (screen._root.winfo_pointery() - screen._root.winfo_rooty())

    hx, hy = head.pos()
    angle = math.degrees(math.atan2(y - hy, x - hx))
    head.setheading(angle)
    head.forward(7)

    positions.insert(0, head.pos())
    positions.pop()

    for i in range(1, len(segments)):
        idx = i * 5
        if idx < len(positions):
            segments[i].goto(positions[idx])

    for seg_idx, leg_pair in legs:
        if seg_idx < len(segments):
            seg = segments[seg_idx]
            sx, sy = seg.pos()
            angle = seg.heading()
            for leg, side in leg_pair:
                offset_angle = angle + side * 90
                offset_x = math.cos(math.radians(offset_angle)) * 10
                offset_y = math.sin(math.radians(offset_angle)) * 10
                leg_angle = math.sin(t * 0.3 + seg_idx) * 30
                leg.setheading(angle + leg_angle + side * 60)
                leg.goto(sx + offset_x, sy + offset_y)

    wx, wy = segments[4].pos()
    wing_angle = math.sin(t * 0.2) * 20
    left_wing.goto(wx, wy)
    left_wing.setheading(segments[4].heading() + 140 + wing_angle)
    right_wing.goto(wx, wy)
    right_wing.setheading(segments[4].heading() - 140 - wing_angle)

    hx, hy = head.pos()
    ha = head.heading()
    eye_offset_angle = 30
    dist = 10
    left_eye.goto(hx + math.cos(math.radians(ha + eye_offset_angle)) * dist,
                  hy + math.sin(math.radians(ha + eye_offset_angle)) * dist)
    right_eye.goto(hx + math.cos(math.radians(ha - eye_offset_angle)) * dist,
                   hy + math.sin(math.radians(ha - eye_offset_angle)) * dist)

    for b in bonus_items[:]:
        if head.distance(b) < 20:
            b.hideturtle()
            bonus_items.remove(b)
            for s in reversed(segments):
                if s.fillcolor() == "white":
                    s.color(random.choice(["blue", "orange", "purple", "cyan", "pink"]))
                    break

    screen.update()
    t += 1
    screen.ontimer(update, 30)

create_bonus()
update()
screen.mainloop()
from turtle import Turtle, Screen, colormode, color, begin_fill
import random
import colorgram
# colors = colorgram.extract('image.jpg',30)
# print(colors)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(color.rgb)
# print(rgb_colors)
# rgb_new = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_new.append(new_color)
# print(rgb_new)

color_list = [(181, 164, 134), (224, 232, 237), (241, 226, 230), (120, 95, 80), (69, 95, 111), (147, 163, 172),
              (123, 74, 86), (210, 201, 151), (178, 150, 157), (152, 167, 158), (33, 41, 56), (45, 36, 30),
              (78, 102, 87), (57, 34, 47), (100, 45, 61), (146, 139, 90), (32, 48, 40), (153, 112, 121),
              (157, 114, 106), (210, 181, 187), (49, 61, 84), (209, 184, 179), (90, 52, 47), (45, 75, 60),
              (182, 198, 190), (113, 137, 124), (39, 74, 83), (105, 136, 144)]
scr = Screen()
scr.bgcolor("AntiqueWhite")
tim = Turtle()
tim.shape("circle")
colormode(255)
tim.width(2)
tim.speed(0)
tim.penup()
tim.ht()
c_size = 100
d_size = 25
def circle():
    for b in range(10):
        for _ in range(10):
            tim.dot(d_size, random.choice(color_list))
            tim.circle(c_size, 36)
        tim.right(36)
        tim.forward(32)

for _ in range(3):
    circle()
    d_size = d_size/1.25
    c_size = c_size*1.25


screen = Screen()
screen.exitonclick()

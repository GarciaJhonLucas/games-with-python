#!/usr/bin/env python3

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 200
h = 0

for j in range(360):
	t.begin_fill()
	for i in range(2):
		h += 1/n
		t.left(20)
		t.forward(j-i)
	t.end_fill()
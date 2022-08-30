# one can of paint covers 5m^2 of wall, given a random height and width of wall
# calculate the minimum cans of paint to buy to fully cover the wall fully.
# define a function to take in inputs for width, height
# calculate the area of wall w*h, then calculate cans to buy rounded up to whole number
# output the number of cans

from math import ceil

def getPaintCans(w,h):
    print(f"You need at least {ceil((float(w)*float(h))/5)} cans of paint to fully cover the {w} by {h} wall.")

[width,height]=str.split(input("Input width and height of wall in metres, separated by a comma: \n"),",")
getPaintCans(width,height)
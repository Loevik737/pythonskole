#!/usr/bin/python3

from sys import stdin


def max_value(widths, heights, values, paper_width, paper_height):

    #om seddelen ikke passer på arket får den verdien 0
    for i in range(0,len(widths)):
        if (widths[i] > paper_width and widths[i] > paper_height) or (heights[i] > paper_width and heights[i] > paper_height):
            values[i] = 0



    

def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    main()
# treasure_map
[xCoord,yCoord]=str.split(input("X marks the spot! input a 2-d coordinate between 1-3 for each axis separated by a comma (x,y):\n"),",")
xAxis = [[" "]*3, [" "]*3, [" "]*3]
xAxis[int(yCoord)-1][int(xCoord)-1] = "X"
print(f"{xAxis[0]}\n{xAxis[1]}\n{xAxis[2]}")
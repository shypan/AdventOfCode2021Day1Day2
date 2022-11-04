input = open("day2_input.txt")

def locator_corrected(file_input):
    h_pos = 0
    depth = 0
    aim = 0
    with file_input as i:
        for line in i:
            pos_data = line.strip().split(" ")
            direction = pos_data[0]
            units = int(pos_data[1])

            if direction == "forward":
                h_pos += units
                depth += aim*units
            if direction == "down":
                aim += units
            if direction == "up":
                aim -= units
    return h_pos, depth


coords = locator_corrected(input)
# print(coords)
# print(coords[0]*coords[1])
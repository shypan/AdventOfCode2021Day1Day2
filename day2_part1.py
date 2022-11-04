input = open("day2_input.txt")


def locator(file_input):
    h_pos = 0
    depth = 0
    with file_input as i:
        for line in i:
            pos_data = line.strip().split(" ")
            direction = pos_data[0]
            units = int(pos_data[1])

            if direction == "forward":
                h_pos += units
            if direction == "down":
                depth += units
            if direction == "up":
                depth -= units
    return h_pos, depth


coords = locator(input)
# print(coords)
# print(coords[0]*coords[1])

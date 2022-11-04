
input = open("day1_input.txt")


def inc_count(file_input):
    count = 0
    inc_count = 0
    last = ""
    with file_input as i:
        for line in i:
            if count == 0:
                last = int(line)
                count += 1
                continue
            else:
                current = int(line)
                if current > last:
                    inc_count += 1
                    count += 1
                elif last > current:
                    count += 1
                else:
                    count += 1
                last = current
    return inc_count


# print(inc_count(input))

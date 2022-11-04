import string

from day1_part1 import inc_count

input = open("day1_input.txt")

def slide_window_sum3(file_input):
    data = []
    sum = 0
    sums = []
    max_len = len(data)
    count = 0

    with file_input as f:
        for line in f:
            data.append(int(line))

    # print(data)
    max_len = len(data)
    # print(max_len)
    count = 0

    for i in range(0, len(data)):
        count += 1
        sum = 0
        sum += data[i]
        # print(count)
        if count == max_len - 1:
            break
        sum += data[i + 1]
        sum += data[i + 2]
        sums.append(sum)

    return sums


output = slide_window_sum3(input)
output_file = open("output_day1part2.txt", "w+")

for num in output:
    output_file.write(str(num) + "\n")

output_file = open("output_day1part2.txt")

inc_count_slide = inc_count(output_file)

# print(inc_count_slide)
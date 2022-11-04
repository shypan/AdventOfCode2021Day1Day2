from day1_part1 import inc_count
from day1part2 import slide_window_sum3
from day2_part1 import locator
from day2_part2 import locator_corrected

if __name__ == "__main__":

    day1input = open("day1_input.txt")
    day2input = open("day2_input.txt")

    print("Day 1, Part 1 answer: ", inc_count(day1input))

    day1input = open("day1_input.txt")

    output = slide_window_sum3(day1input)
    output_file = open("output_day1part2.txt", "w+")

    for num in output:
        output_file.write(str(num) + "\n")

    output_file = open("output_day1part2.txt")

    inc_count_slide = inc_count(output_file)

    print("Day 1, Part 2 answer: ", inc_count_slide)

    day2part1_answer = locator(day2input)
    print("Day 2, Part 1 answer: ", day2part1_answer, day2part1_answer[0]*day2part1_answer[1])

    day2input = open("day2_input.txt")
    day2part2_answer = locator_corrected(day2input)
    print("Day 2, Part 2 answer: ", day2part2_answer, day2part2_answer[0] * day2part2_answer[1])



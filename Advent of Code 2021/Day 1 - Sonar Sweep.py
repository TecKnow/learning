sample_data = """
199
200
208
210
200
207
240
269
260
263
"""

sample_data_b = """
199
200
208
210
200
207
240
269
260
263
"""


def increasing_values(int_list: list[int]) -> int:
    input_int_zip = zip(int_list[:], int_list[1:])
    filtered_int_zip_list = [x for x in input_int_zip if x[1] > x[0]]
    return len(filtered_int_zip_list)


def sliding_windows(int_list: list[int], window_size: int = 3) -> int:
    print(int_list)
    count = 0
    list_a = int_list[:]
    list_b = int_list[1:]
    while len(list_b) >= window_size:
        window_a = list_a[:window_size]
        window_b = list_b[:window_size]
        print(window_a, window_b)
        if sum(window_b) > sum(window_a):
            count += 1
        list_a.pop(0)
        list_b.pop(0)
    return count


if __name__ == "__main__":
    with open("Day 1 Data.txt") as input_file:
        input_int_list = [int(line) for line in input_file if line.strip()]
        print(sliding_windows(input_int_list))

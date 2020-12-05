def decode_boarding_pass(boarding_pass: str) -> dict[str, int]:
    boarding_pass = boarding_pass.replace("F", "0")
    boarding_pass = boarding_pass.replace("B", "1")
    boarding_pass = boarding_pass.replace("L", "0")
    boarding_pass = boarding_pass.replace("R", "1")
    row = boarding_pass[:7]
    row = int(row, 2)
    seat = boarding_pass[7:]
    seat = int(seat, 2)
    seat_id = (row * 8) + seat
    return {
        "row": row,
        "seat": seat,
        "ID": seat_id
    }


def find_missing_seats(decoded_boarding_passes: dict[str, int]) -> set[int]:
    all_seats = set(range(1024))
    known_seats = set([boarding_pass["ID"] for boarding_pass in decoded_boarding_passes])
    missing_seats = all_seats.difference(known_seats)
    return missing_seats, known_seats


def find_potential_seats(missing_seats: set[int], known_seats: set[int]) -> set[int]:
    result_set = set()
    for missing_seat in missing_seats:
        if missing_seat + 1 in known_seats and missing_seat - 1 in known_seats:
            result_set.add(missing_seat)
    return result_set

if __name__ == "__main__":
    data = open("Day 5 Data.txt").readlines()
    decoded_data = [decode_boarding_pass(row) for row in data]
    max_id = max(x["ID"] for x in decoded_data)
    print(f"Maximum ID found: {max_id}")
    missing_seats, known_seats = find_missing_seats(decoded_data)
    potential_seats = find_potential_seats(missing_seats, known_seats)
    print(f"{potential_seats=}")

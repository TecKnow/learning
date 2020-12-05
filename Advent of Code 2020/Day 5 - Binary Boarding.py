from pprint import pprint


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


if __name__ == "__main__":
    data = open("Day 5 Data.txt").readlines()
    decoded_data = [decode_boarding_pass(row) for row in data]
    max_id = max(x["ID"] for x in decoded_data)
    print(f"Maximum ID found: {max_id}")

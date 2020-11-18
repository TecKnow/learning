if __name__ == "__main__":
    winning_combinations = set()
    total_combinations = set()
    losing_combinations = set()
for x in range(1,7):
    for y in range(1,7):
        for z in range(1,7):
            total_combinations.add((x,y,z))
            if x + y == 10:
                winning_combinations.add((x,y,z))
            elif x+y > 10 and x+z == 10:
                winning_combinations.add((x,y,z))
            elif x+y+z == 10:
                winning_combinations.add((x,y,z))
            else:
                losing_combinations.add((x,y,z))

print(f"winning combinations: {len(winning_combinations)}\n"
      f"losing combinations: {len(losing_combinations)}\n"
      f"total combinations: {len(total_combinations)}")
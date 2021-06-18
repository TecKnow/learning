import argparse
import csv

COLUMN_NAMES = "Name Price Street City State Comments"

parser = argparse.ArgumentParser("Track information about restaurants")
parser.add_argument("master.csv", help="The master list of restaurant data that will be updated")
parser.add_argument("update.csv", help="New information to be added to the master list.  This file will not be changed")
parser.add_argument("-u", "--update", action="store_true")
parser.add_argument("-s", "--sort", action="store_true")

if __name__ == "__main__":
    args = parser.parse_args()
    args = vars(args)
    with open(args["master.csv"], newline='') as master_file, open(args["update.csv"], newline="") as update_file:
        master_reader = csv.DictReader(master_file)
        update_reader = csv.DictReader(update_file)
        master_list = [*master_reader]
        update_list = [*update_reader]
        records = {(r["State"], r["City"], r["Name"], r["Street"]): r for r in master_list}
        rows_added = 0
        rows_updated = 0
        for row in update_list:
            if (row["State"], row["City"], row["Name"], row["Street"]) not in records:
                rows_added += 1
                records[(row["State"], row["City"], row["Name"], row["Street"])] = row
            elif args["update"]:
                if row["Comments"]:
                    records[(row["State"], row["City"], row["Name"], row["Street"])]["Comments"] = row["Comments"]
                    rows_updated += 1
    with open(args["master.csv"], 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=COLUMN_NAMES.split())
        writer.writeheader()
        if args["sort"]:
            writer.writerows(sorted(records.values(), key=lambda r: (r["State"], r["City"], r["Name"])))
        else:
            writer.writerows(records.values())
    print(f"Added {rows_added} row(s)")
    if args["update"]:
        print(f"Updated {rows_updated} row(s)")

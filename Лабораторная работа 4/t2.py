import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        json_data = json.dumps([row for row in csv_reader], indent=4)
        with open(OUTPUT_FILENAME, 'w') as json_file:
            json_file.write(json_data)


if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

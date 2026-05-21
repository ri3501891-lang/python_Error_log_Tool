import csv

INPUT_FILE = "input.csv"
OUTPUT_FILE = "error.log"


def extract_error_logs():
    total_lines = 0
    error_lines = []

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_lines += 1
            if row["status"] == "ERROR":
                error_lines.append(row)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for row in error_lines:
            file.write(f'id={row["id"]}, status={row["status"]}, message={row["message"]}\n')

    print(f"Total lines: {total_lines}")
    print(f"Error lines: {len(error_lines)}")
    print(f"Error lines saved to {OUTPUT_FILE}")


extract_error_logs()
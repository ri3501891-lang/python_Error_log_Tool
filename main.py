import csv

INPUT_FILE = "input.csv"
ERROR_FILE = "error.log"
WARNING_FILE = "warning.log"
SUMMARY_FILE = "summary.csv"


def analyze_logs():
    total_lines = 0
    error_lines = []
    warning_lines = []
    summary = {}

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_lines += 1

            date = row["date"]
            status = row["status"]

            if date not in summary:
                summary[date] = {
                    "error_count": 0,
                    "warning_count": 0
                }

            if status == "ERROR":
                error_lines.append(row)
                summary[date]["error_count"] += 1

            elif status == "WARNING":
                warning_lines.append(row)
                summary[date]["warning_count"] += 1

    with open(ERROR_FILE, "w", encoding="utf-8") as file:
        for row in error_lines:
            file.write(
                f'date={row["date"]}, id={row["id"]}, status={row["status"]}, message={row["message"]}\n'
            )

    with open(WARNING_FILE, "w", encoding="utf-8") as file:
        for row in warning_lines:
            file.write(
                f'date={row["date"]}, id={row["id"]}, status={row["status"]}, message={row["message"]}\n'
            )

    with open(SUMMARY_FILE, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["date", "error_count", "warning_count"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

       

        for date, counts in summary.items():
            writer.writerow({
                "date": date,
                "error_count": counts["error_count"],
                "warning_count": counts["warning_count"]
            })
            
            

    print(f"Total lines: {total_lines}")
    print(f"Error lines: {len(error_lines)}")
    print(f"Warning lines: {len(warning_lines)}")
    print(f"Error lines saved to {ERROR_FILE}")
    print(f"Warning lines saved to {WARNING_FILE}")
    print(f"Summary saved to {SUMMARY_FILE}")


analyze_logs()
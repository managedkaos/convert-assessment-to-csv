"""
Use this template to create a custom Python function
"""

import csv
import sys


def parse_input_data(input_data):
    """
    parse input data
    """
    lines = input_data.split("\n")
    data = []
    current_set = {}

    for line in lines:
        if line.startswith("Script Name:"):
            if current_set:
                data.append(current_set)
                current_set = {}
            current_set["Video Title (from TOC)"] = line.replace(
                "Script Name:", ""
            ).strip()
        elif line.startswith("Question:"):
            current_set["Question"] = line.replace("Question:", "").strip()
        elif line.startswith("Correct Answer:"):
            current_set["Correct"] = line.replace("Correct Answer:", "").strip()
        elif line.startswith("Incorrect 1:"):
            current_set["Incorrect 1"] = line.replace("Incorrect 1:", "").strip()
        elif line.startswith("Incorrect 2:"):
            current_set["Incorrect 2"] = line.replace("Incorrect 2:", "").strip()
        elif line.startswith("Incorrect 3:"):
            current_set["Incorrect 3"] = line.replace("Incorrect 3:", "").strip()
        elif line.startswith("Correct Explanation:"):
            current_set["Correct Explanation"] = line.replace(
                "Correct Explanation:", ""
            ).strip()
        elif line.startswith("Incorrect 1 Explanation:"):
            current_set["Incorrect 1 Explanation"] = line.replace(
                "Incorrect 1 Explanation:", ""
            ).strip()
        elif line.startswith("Incorrect 2 Explanation:"):
            current_set["Incorrect 2 Explanation"] = line.replace(
                "Incorrect 2 Explanation:", ""
            ).strip()
        elif line.startswith("Incorrect 3 Explanation:"):
            current_set["Incorrect 3 Explanation"] = line.replace(
                "Incorrect 3 Explanation:", ""
            ).strip()

    if current_set:
        data.append(current_set)

    return data


def write_to_csv(data, csv_filename):
    """
    write csv data to file
    """
    header = [
        "Video Title (from TOC)",
        "Video Filename",
        "Video ID",
        "Quiz",
        "Exam",
        "CEU",
        "Qustn Type",
        "Question",
        "Correct",
        "Incorrect 1",
        "Incorrect 2",
        "Incorrect 3",
        "Correct Explanation",
        "Incorrect 1 Explanation",
        "Incorrect 2 Explanation",
        "Incorrect 3 Explanation",
        "Subdomain",
        "Difficulty Level",
        "Is Practice Exam",
        "Good/Bug/Needs Improvement",
        "Actionable Feedback",
        "Matches Learning Objective",
    ]

    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    """
    the main function
    """
    if len(sys.argv) != 3:
        print("Usage: python convert_to_csv.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'ASSESSMENTS.txt'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'output.csv'

    with open(input_file, "r") as file:
        input_data = file.read()

    parsed_data = parse_input_data(input_data)
    write_to_csv(parsed_data, output_file)
    print(f"Data has been written to {output_file}")


if __name__ == "__main__":
    main()

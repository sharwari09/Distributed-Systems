import csv


def parse_csv(input_file):
    with open(input_file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            if i == 0:
                continue #Skip the header
            yield line


"""Enrollment analysis:  Summary report of majors enrolled in a class.
CS 210 project, Fall 2023.
Author:  Miguel Pimienta
Credits:
"""
import doctest
import csv


def read_csv_column(path: str, field: str) -> list[str]:
    """Read one column froma CSV file with headers inot a list of s

    >>> read_csv_column("data/test_roster.csv", "Major")
    ['DSCI', 'CIS', 'BADM', 'BIC', 'CIS', 'GSS']
    """
    with open(path, "r", newline="")as the_file:
        reader = csv.DictReader(the_file)
        list = []
        for row in reader:
            list.append(row[field])
    return list


def counts(column: list[str]) -> dict[str, int]:
    """ Returns a dict with counts of elemens in column.
    >>> counts(["dog", "cat", "cat", "rabbit", "dog"])
    {'dog': 2, 'cat': 2, 'rabbit': 1}
    """
    counts = {}
    for word in column:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts




def read_csv_dict(path: str, key_field: str, value_field: str) -> dict[str, dict]:
    """Read a CSV with column headers into a dict with selected
    key and value fields.

    >>> read_csv_dict("data/test_programs.csv", key_field="Code", value_field="Program Name")
    {'ABAO': 'Applied Behavior Analysis', 'ACTG': 'Accounting', 'ADBR': 'Advertising and Brand Responsibility'}
   """

    with open(path, "r", newline="") as the_file:
        reader = csv.DictReader(the_file)
        dict = {}
        for row in reader:
            sort_major = row[key_field]
            long_major = row[value_field]
            dict[sort_major] = long_major
    return dict

def items_v_k(counts_by_major: dict) ->list[tuple]:
    """Makes a list of tuples from the dict
    >>> items_v_k({'one': 1, 'two': 2})
    [(1, 'one'), (2, 'two')]
    """
    new_count = []
    for code, count in counts_by_major.items():
        double = (count, code)
        new_count.append(double)
    return new_count


def main():
    doctest.testmod()
    majors = read_csv_column("data/roster_selected.csv", "Major")
    counts_by_major = counts(majors)
    program_names = read_csv_dict("data/programs.csv", "Code", "Program Name")
    # --- Next line replaces several statements
    by_count = items_v_k(counts_by_major)
    # ---
    by_count.sort(reverse=True)  # From largest to smallest
    for count, code in by_count:
        program = program_names[code]
        print(count, program)


if __name__ == "__main__":
    main()


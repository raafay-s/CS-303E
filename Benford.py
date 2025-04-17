# File: Benford.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
#
# Date: 04/04/2025
# Description of Program: Analyze a dataset for compliance with Benford's Law using leading digits of death-related statistics from a file.

def main():
    filename = input("Enter the name of a file of census data: ")
    try:
        infile = open(filename, "r")
    except:
        print("File does not exist")
        return

    # Set for unique values
    unique_values = set()

    # Dictionary for digit counts (as strings)
    digit_counts = {}
    for i in range(10):
        digit_counts[str(i)] = 0

    line_count = 0

    for line in infile:
        if "#" in line:
            continue  # Skip comment lines
        fields = line.strip().split(",")

        if len(fields) < 7:
            continue  # Skip malformed lines

        number_of_deaths = fields[5].strip()
        death_rate = fields[6].strip()

        # Remove underscores
        number_of_deaths = number_of_deaths.replace("_", "")
        death_rate = death_rate.replace("_", "")

        # Add to unique value set
        unique_values.add(number_of_deaths)
        unique_values.add(death_rate)

        # Count leading digit for both values
        if number_of_deaths != "":
            digit = number_of_deaths[0]
            if digit in digit_counts:
                digit_counts[digit] += 1

        if death_rate != "":
            digit = death_rate[0]
            if digit in digit_counts:
                digit_counts[digit] += 1

        line_count += 1

    infile.close()

    # Write results to file
    outfile = open("benford.txt", "w")
    outfile.write("Processing file: " + filename + "\n\n")
    outfile.write("Total lines processed: " + str(line_count) + "\n")
    outfile.write("Unique numbers count: " + str(len(unique_values)) + "\n")
    outfile.write("First digit frequency distributions:\n")
    outfile.write("Digit".ljust(8) + "Count".ljust(12) + "Percentage\n")

    total_digits = sum(digit_counts.values())

    for i in range(10):
        digit = str(i)
        count = digit_counts[digit]
        if total_digits == 0:
            percentage = 0.0
        else:
            percentage = round((count * 100.0) / total_digits, 1)
        line = digit.ljust(8) + str(count).ljust(12) + str(percentage) + "\n"
        outfile.write(line)

    outfile.close()
    print("Output written to benford.txt")

main()
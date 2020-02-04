import csv
import itertools

with open('GOL_consolidado.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = itertools.izip(*[lines] * 3)
    with open('output.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(grouped)


from tablestats import read_rows, count_types, total_minutes, to_csv

filename = input()

with open(filename, encoding="utf-8") as table:
    rows = read_rows(table)

counts = count_types(rows)

print(len(rows))
print(len(counts))
print(total_minutes(rows, "ошибка"))

with open("lab05/summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))

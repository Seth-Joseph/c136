import csv

rows = []

with open('final.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        rows.append(i)

headers = rows[0]
star_data_rows = rows[1:]

final_dict = []

final_star_list = []
for star_data in star_data_rows:
  temp_dict = {
      "name":star_data[1],
      "distance":star_data[2],
      "mass":star_data[3],
      "radius":star_data[4],
      "gravity":star_data[5],
  }
  final_dict.append(temp_dict)

print(list(final_dict))

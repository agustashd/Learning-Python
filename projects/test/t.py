import csv

with open('data.csv', newline='') as f:
            data_table = csv.reader(f)
            for col in next(data_table):
                print(col)
            for row in data_table:
                for col in row:
                    print(col)

print("end")
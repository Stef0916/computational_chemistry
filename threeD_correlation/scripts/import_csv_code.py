import csv

# Define your data as a list of lists
data = data = [
    ["Theta", "Alpha", "J"],
    [95.2, 0, -159.27],
    [95.2, 10, -128.42],
    [95.2, 20, -65.7],
    [95.2, 30, 9.06],
    [95.2, 40, 76.49],
    [95.2, 50, 125.81],
    [95.2, 60, 155.47],
    [96.1, 0, -217.62],
    [96.1, 10, -184.67],
    [96.1, 20, -117.35],
    [96.1, 30, -35.55],
    [96.1, 40, 41.03],
    [96.1, 50, 100.61],
    [96.1, 60, 139.96],
    [97.09, 0, -284.7],
    [97.09, 10, -249.52],
    [97.09, 20, -177.35],
    [97.09, 30, -88.3],
    [97.09, 40, -2.37],
    [97.09, 50, 67.56],
    [97.09, 60, 116.72],
    [97.83, 0, -329.87],
    [97.83, 10, -293.37],
    [97.83, 20, -218.45],
    [97.83, 30, -125.35],
    [97.83, 40, -34.01],
    [97.83, 50, 42.1],
    [97.83, 60, 97.32],
    [98.91, 0, -380.87],
    [98.91, 10, -342.89],
    [98.91, 20, -264.82],
    [98.91, 30, -167.2],
    [98.91, 40, -69.98],
    [98.91, 50, 12.72],
    [98.91, 60, 74.37],
    [99.85, 0, -452.02],
    [99.85, 10, -411.99],
    [99.85, 20, -329.63],
    [99.85, 30, -226.05],
    [99.85, 40, -121.1],
    [99.85, 50, -29.77],
    [99.85, 60, 40.41],
    [100.75, 0, -507.23],
    [100.75, 10, -465.59],
    [100.75, 20, -379.84],
    [100.75, 30, -271.72],
    [100.75, 40, -160.97],
    [100.75, 50, -63.17],
    [100.75, 60, 13.49]
]

# Specify the CSV file path
csv_file_path = ""

# Open the CSV file in write mode and write the data
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

print(f"CSV file '{csv_file_path}' has been created.")

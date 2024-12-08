data_array_1 = []
data_array_2 = []

# Fill arrays with data from input file
with open('input_day_1', 'r') as input_file:
    for line in input_file:
        line_values = line.strip().split()
        if len(line_values) == 2:
            data_array_1.append(int(line_values[0]))
            data_array_2.append(int(line_values[1]))

# Sort data arrays
data_array_1.sort()
data_array_2.sort()

# Get total distance
total_distance = 0
for i in range(len(data_array_1)):
    if data_array_1[i] > data_array_2[i]:
        total_distance += data_array_1[i] - data_array_2[i]
    else:
        total_distance += data_array_2[i] - data_array_1[i]

print(total_distance)

import functions

data_array_1, data_array_2 = functions.read_data_from_input_1()

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

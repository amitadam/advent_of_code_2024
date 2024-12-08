import functions

data_array_1, data_array_2 = functions.read_data_from_input_1()

data_appearances_in_array_2 = {}

for value in data_array_2:
    if value in data_appearances_in_array_2:
        data_appearances_in_array_2[value] += 1
    else:
        data_appearances_in_array_2[value] = 1

similarity_score = 0
for value in data_array_1:
    if value in data_appearances_in_array_2:
        similarity_score += value * data_appearances_in_array_2[value]

print(similarity_score)

def read_data_from_input_1():
    array_1 = []
    array_2 = []
    with open('input_1', 'r') as input_file:
        for line in input_file:
            line_values = line.strip().split()
            if len(line_values) == 2:
                array_1.append(int(line_values[0]))
                array_2.append(int(line_values[1]))
    return array_1, array_2
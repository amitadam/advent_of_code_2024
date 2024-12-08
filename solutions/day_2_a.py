import functions

reports = functions.read_data_from_input_2()

number_of_safe_reports = 0

for report in reports:
    is_report_safe = True
    if len(report) > 1:
        if int(report[0]) > int(report[1]):
            is_ascending = False
        else:
            is_ascending = True
        for i in range(1, len(report)):
            if is_ascending is True and int(report[i]) < int(report[i - 1]):
                is_report_safe = False
                break
            elif is_ascending is False and int(report[i]) > int(report[i - 1]):
                is_report_safe = False
                break
            else:
                difference = abs(int(report[i]) - int(report[i - 1]))
                if difference < 1 or difference > 3:
                    is_report_safe = False
                    break
        if is_report_safe is True:
            number_of_safe_reports += 1

print(number_of_safe_reports)

customer_report = {}

try:
    with open("telebirr_log.txt", "r") as f:
        for line in f:
            cleaned_line = line.strip()
            parts = cleaned_line.split(",")

            if len(parts) == 2:
                name = parts[0].strip()
                amount = float(parts[1].strip())
                
                if name in customer_report:
                    customer_report[name] = customer_report[name] + amount
                else:
                    customer_report[name] = amount

    
    list_to_sort = []
    for name, total in customer_report.items():
        list_to_sort.append((total, name))
    list_to_sort.sort(reverse=True)


    with open("transaction report.txt", "w") as report_file:
        
        for total, name in list_to_sort:
            rounded_total = round(total, 2)
            report_line = name + ": " + str(rounded_total)
            
            print(report_line)
            report_file.write(report_line + "\n")

except FileNotFoundError:
    print("File doesnt exist")

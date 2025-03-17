import csv
def save_to_csv(data,filename="book.csv"):
    with open(filename,"w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title","Price"])
        writer.writerows(data)
        print(f"Data saved to {filename}")


    
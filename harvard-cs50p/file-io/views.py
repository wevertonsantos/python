import csv
from PIL import Image

def main():
    with open("views.csv","r",encoding="utf-8") as views, open("analysis.csv","w", encoding="utf-8") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis,fieldnames=reader.fieldnames + ["new"])
        writer.writeheader()
        new = "new_value"
        for row in reader:
            writer.writerow({
                "id" : row["id"],
                "english_title" : row["english_title"],
                "japanese_title" : row["japanese_title"],
                "new" : new
            })

main()
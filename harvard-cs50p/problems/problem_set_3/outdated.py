#https://cs50.harvard.edu/python/2022/psets/3/outdated/

def main():
    date = input("Date: ")
    formatter_date(date)

def formatter_date(date):
    #Verificar os dados que estão contido na data
    #Pegar o dia, mês e ano da data
    ...

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#main()

date = "September 8, 1636"
if '/' in date and len(date) == 8:
    month = month = int(date[0])
    year = int(date[4:])
    day = int(date[2])
    if month < 10:
        month = f"0{int(date[0])}"
    if day < 10:
        day = f"0{int(date[2])}"
    date = f"{year}-{month}-{day}"
    print(date)
else:
    for month in months:
        if month in date:
            ...
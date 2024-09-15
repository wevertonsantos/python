#https://cs50.harvard.edu/python/2022/psets/3/outdated/

def main():
    date = input("Date: ")
    formatter_date(date)

def formatter_date(date):
    ...

months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August:":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

#main()

#date = "December 80, 1980"
date = "9/8/1636"
if "/" in date and len(date) <= 10:
    date = date.strip().split("/")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    if day <= 31:
        if month < 10:
            month = f"0{month}"
        if day < 10:
            day = f"0{day}"
        date = f"{year}-{month}-{day}"
    print(date)
else:
    for month in months:
        if month in date:
            if date.startswith(month):
                if len(date) == 17:
                    month = int(months[month])
                    year = int(date[13:])
                    day = int(date[10])
                    if day <= 31:
                        if month < 10:
                            month = f"0{month}"
                        if day < 10:
                            day = f"0{day}"
                        date = f"{year}-{month}-{day}"
                    print(date)
                    #print(months[month])
                    #print(date[10])
                    #print(date[13:])
#https://cs50.harvard.edu/python/2022/psets/1/meal/

def main():
    time = input("What time is it? ")
    time = convert(time)
    print(meal(time))
    
def convert(time):
    time = time.replace(":",".")
    if time.__contains__("30"):
        time = time.replace("30","50")
    return float(time)

def meal(time):
    if time >= 7 and time <= 8:
        return "breakfast time"
    elif time >= 12 and time <= 13:
        return "lunch time"
    elif time >= 18 and time <= 19:
        return "dinner time"
    else:
        return None
        
if __name__ == "__main__":
    main()
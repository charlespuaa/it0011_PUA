dateInput = input("Enter date (MM/DD/YY): ")

def convertDateFormat(dateInput):
    month, day, year = dateInput.split("/")
    
    if month == "01":
        monthName = "January"
    elif month == "02":
        monthName = "February"
    elif month == "03":
        monthName = "March"
    elif month == "04":
        monthName = "April"
    elif month == "05":
        monthName = "May"
    elif month == "06":
        monthName = "June"
    elif month == "07":
        monthName = "July"
    elif month == "08":
        monthName = "August"
    elif month == "09":
        monthName = "September"
    elif month == "10":
        monthName = "October"
    elif month == "11":
        monthName = "November"
    elif month == "12":
        monthName = "December"
    else:
        print("Invalid month entered.")
        return
    
    year = "20" + year if len(year) == 2 else year
    
    print(f"Date Output: {monthName} {int(day)}, {year}")

convertDateFormat(dateInput)
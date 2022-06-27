def getDayFromDate(theDate):
	stringList = theDate.split(" ")
	number = stringList[1]
	number = number.replace(",", "")
	return int(number)

def getMonthFromDate(theDate):
	stringList = theDate.split(" ")
	Date = stringList[0]
	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	for i in range(12):
		if Date == months[i]:
			return months[i] 

def getMonthFromDateNum(theDate):
	stringList = theDate.split(" ")
	Date = stringList[0]
	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	for i in range(12):
		if Date == months[i]:
			return nums[i]

def getYearFromDate(theDate):
	stringList = theDate.split(" ")
	year = stringList[2]
	return year

def getLengthOfMonth (Month):
	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
	for i in range(12):
		if getMonthFromDate(Month) == months[i]:
			return days[i]
			break

def getLengthOfMonthCALC(theDate):
	if isLeapYear(getYearFromDate(theDate)):
		Feb = 29
	else:
		Feb = 28
	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	days = [31, Feb, 31, 30, 31, 30, 31, 31, 30, 31, 30]
	for i in range(12):
		if getMonthFromDate(theDate) == months[i]:
			return days[i]
			break

def isLeapYear(year):
	if int(year)%4 == 0 and int(year)%100 != 0 and int(year)%400 != 0:
			return True
		
	if int(year)%100 == 0 and int(year)%400 == 0:
		return True

	else:
		return False
		
def calculateDaysBetween(date1, date2):
	day1 = int(getDayFromDate(date1))
	day2 = int(getDayFromDate(date2))

	month1 = getMonthFromDateNum(date1)
	month2 = getMonthFromDateNum(date2)

	year1 = int(getYearFromDate(date1))
	year2 = int(getYearFromDate(date2))

	if year1 > year2:
		maxYear = year1 
		minYear = year2

		maxMonth = month1
		minMonth = month2

		maxDay = day1 
		minDay = day2 
	
	#If the years are the same 
	elif year1 == year2:

			
		if month1 > month2:
			maxYear = year1 
			minYear = year2

			maxMonth = month1
			minMonth = month2

			maxDay = day1 
			minDay = day2 

		else:
			maxYear = year2
			minYear = year1

			maxMonth = month2
			minMonth = month1

			maxDay = day2
			minDay = day1 
			

	else:
		maxYear = year2
		minYear = year1

		maxMonth = month2
		minMonth = month1

		maxDay = day2
		minDay = day1 

	diffYear = maxYear - minYear 
	diffMonth = int(maxMonth) - int(minMonth)
	diffDay = maxDay - minDay 

	



	if diffDay < 0:
		diffMonth -= 1
		diffDay = 31+diffDay

	if diffMonth < 0:
		diffYear -= 1
		diffMonth = 12+diffMonth
	
	



	
	
	TwoYearDaysMin = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	TwoYearDaysMax = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	if isLeapYear(minYear) == True:
		TwoYearDaysMin = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	


	if isLeapYear(maxYear) == True:
		TwoYearDaysMax = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	sumDay = -minDay + 1
	
	for i in range(minMonth, 13):
		sumDay += TwoYearDaysMin[i]
	

	for j in range(maxMonth-1, 0, -1):
		sumDay += TwoYearDaysMax[j]
	
	sumDay += maxDay 

	for l in range(minYear + 1, maxYear):
		sumDay += 365
		if isLeapYear(l) == True:
			sumDay += 1
	
	if maxYear == minYear:
		if maxMonth == minMonth:
			return f'The number of days between {date1}, and {date2}, is {diffDay}'
			
		sumDay = 0
		for p in range(minMonth, maxMonth ):
			sumDay += TwoYearDaysMax[p]
		
		sumDay += diffDay + 1

	return f'The number of days between {date1}, and {date2}, is {sumDay-1}'

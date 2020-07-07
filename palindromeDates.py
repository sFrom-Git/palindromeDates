def checkPalindrome(word):
  for i in range(len(word) // 2):
  	if word[i] == word[-i - 1]:
  		pass
  	else:
  		return False
  return True



    #Code starts executing from here
counter = 0

print("DD/MM/YYYY")
startYear = int(input("start year: "))

print("DD/MM/YYYY")
endYear = int(input("end year: "))

#print("{:02d}/{:02d}/{:04d}".format(i, j, k))



for year in range(startYear, endYear):
	for month in range(1, 13):
		for day in range(1, 32):
			dateStr = "{:02d}".format(day) + "{:02d}".format(month) + "{:04d}".format(year)

			if checkPalindrome(dateStr):
				print("{:02d}/{:02d}/{:04d}".format(day, month, year))
				counter += 1

print(counter)


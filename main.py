import ftcapi
import datetime
import calendar
import time
import lcddriver

lcd = lcddriver.lcd()

#set up variables to start
currentprice = ftcapi.toFTC(1)
sundayreset=0 
highprice = currentprice
lowprice = currentprice

#main loop
while True:	
	now = datetime.datetime.now()
	check = calendar.weekday(now.year, now.month, now.day)

	#high and low values resets at the start of Sunday each week
	#based on local time
	if check is 7:
		if sundayreset == 0:
			highprice = currentprice
			lowprice = currentprice
			sundayreset=1

	if check is 0:
		if sundayreset == 1:
			sundayreset = 0
	
	#gets current value of ftc
	currentprice = ftcapi.toFTC(1)
	
	#only updated all of display if API responded
	if currentprice > 0:	
		if currentprice > highprice:
			highprice = currentprice
		if currentprice < lowprice:
			lowprice = currentprice

		#display price and date and time
		#call lcd module to display on lcd
		lcd.lcd_display_string("FTC Price in AUD", 1)
		#need to convert float value to string to print and format it to always 4 decimal places
		lcd.lcd_display_string("Low "+ str("{:.4f}".format(lowprice)) + " HI " + str("{:.4f}".format(highprice)), 2)
		lcd.lcd_display_string("Current Price "+ str("{:.4f}".format(currentprice)), 3)
		lcd.lcd_display_string(time.strftime("%d/%m/%Y")+" "+ time.strftime("%H:%M:%S"), 4)
	else:
		lcd.lcd_display_string("Current Price OffLne", 3)
		lcd.lcd_display_string(time.strftime("%d/%m/%Y")+" "+ time.strftime("%H:%M:%S"), 4)
	
	time.sleep(30) #waits 30 seconds before repeating

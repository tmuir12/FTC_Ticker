FTC_Ticker
==========

Python code to create a Raspbery Pi based 20 x 4 LCD feathercoin price ticker
You need a i2C enabled 20 x 4 LCD
If it is 5 volts dont forget a 3.3V to 5V logic converter as the raspberry Pi is 3.3V
Code is set for Australian dollars but can be easily changed to any currency supported by the feathercoin API

ftcapi is based on code provided by Uncle Muddy on the Featehrcoin forum
i2c_lib.py and lcddriver.py I found on the web, but tracking back they appear to of come from CaptainStouf and can be found here
https://github.com/CaptainStouf/raspberry_lcd4x20_I2C

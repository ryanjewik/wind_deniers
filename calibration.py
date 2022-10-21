#SCI calibration manual inputs

#heatRate and coolRate must always have one of them at zero
coolRate = 0 #will take a range of integers, essentially will act as "low-high"
heatRate = 0 #will work similarly to heat rate

#leave and return times will be an int range between either 1-24 or 1-48
humidity = 0 #will be a value between 1-100 in percentage humidity
snow = False #if true the heatRate will increase by 2 & start earlier
rain = False #if true the heateRate will increase by 1 & start earlier
heatWarning = False #if true the coolRate will increase by 1 & start earlier

outerTemp = 80 #outside temperature in F
print("What would you like the inside temperature to be?")
innerTemp = int(input()) #inside temperature in F

print("Around when will you leave the house? (1-24)")
leaveTime = int(input()) #time people will leave the house
print("Around when will you return to the house? (1-24)")
returnTime = int(input()) #time people will return to the house
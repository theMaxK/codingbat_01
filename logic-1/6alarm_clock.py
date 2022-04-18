def alarm_clock(day, vacation): 
    alarm_weekdays = '7:00'
    alarm_weekend = '10:00'
    alarm_weekdays_holidays = '10:00'
    alarm_weekends_holidays = 'off'

    if day >= 1 and day <=5:  
        if vacation == False: 
            return alarm_weekdays
        elif vacation == True: 
            return alarm_weekdays_holidays
    elif day == 0 or day == 6: 
        if vacation == False: 
            return alarm_weekend
        elif vacation == True: 
            return alarm_weekends_holidays

     

print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))
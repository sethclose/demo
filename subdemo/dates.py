def datetimes():
    """
    Function for Date Times
    """

    import datetime
    from zoneinfo import ZoneInfo

    print("datetime.datetime.now() = " + str(datetime.datetime.now()))
    print("datetime.datetime(2023,12,3) = " + str(datetime.datetime(2023,12,3)))
    print("datetime.datetime(2023,12,3,1,2,3,4) = " + str(datetime.datetime(2023,12,3,1,2,3,4)))
    print("   datetime.datetime.now().strftime('%A') = " + str(datetime.datetime.now().strftime("%A")))    
    print("   datetime.datetime.now().strftime('%B') = " + str(datetime.datetime.now().strftime("%B")))
    print("   datetime.datetime.now().strftime('%d') = " + str(datetime.datetime.now().strftime("%d")))
    print("   datetime.datetime.now().strftime('%Y') = " + str(datetime.datetime.now().strftime("%Y")))
    print("   datetime.datetime.now().strftime('%I') = " + str(datetime.datetime.now().strftime("%I")))
    print("   datetime.datetime.now().strftime('%M') = " + str(datetime.datetime.now().strftime("%M")))
    print("   datetime.datetime.now().strftime('%Z') = " + str(datetime.datetime.now().strftime("%Z")))
    print("=> " +
            str(datetime.datetime.now().strftime("%A")) + ", " + 
            str(datetime.datetime.now().strftime("%B")) + " "  +
            str(datetime.datetime.now().strftime("%d")) + ", " + 
            str(datetime.datetime.now().strftime("%Y")) + " "  +
            str(datetime.datetime.now().strftime("%I")) + ":"  +
            str(datetime.datetime.now().strftime("%M")) + " "  +
            str(datetime.datetime.now().strftime("%Z"))) 
    # %a	Weekday, short version	Wed	
    # %A	Weekday, full version	Wednesday	
    # %w	Weekday as a number 0-6, 0 is Sunday	3	
    # %d	Day of month 01-31	31	
    # %b	Month name, short version	Dec	
    # %B	Month name, full version	December	
    # %m	Month as a number 01-12	12	
    # %y	Year, short version, without century	18	
    # %Y	Year, full version	2018	
    # %H	Hour 00-23	17	
    # %I	Hour 00-12	05	
    # %p	AM/PM	PM	
    # %M	Minute 00-59	41	
    # %S	Second 00-59	08	
    # %f	Microsecond 000000-999999	548513	
    # %z	UTC offset	+0100	
    # %Z	Timezone	CST	
    # %j	Day number of year 001-366	365	
    # %U	Week number of year, Sunday as the first day of week, 00-53	52	
    # %W	Week number of year, Monday as the first day of week, 00-53	52	
    # %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
    # %C	Century	20	
    # %x	Local version of date	12/31/18	
    # %X	Local version of time	17:41:00	
    # %%	A % character	%	
    # %G	ISO 8601 year	2018	
    # %u	ISO 8601 weekday (1-7)	1	
    # %V	ISO 8601 weeknumber (01-53)	01	
    
    return

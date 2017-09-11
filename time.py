def durationTransformation(string):
    string=string.replace(' ','')
    string=string.replace('~','')
    string=string.replace('>','')
    string=string.replace('<','')
    string=string.replace('+','')
    string=string.replace('-currently','')
    string=string.replace('r-','r')
    string=string.replace('mins','minutes')
    string=string.replace('-minutes','minutes')
    string=string.replace('Nightly-','')
    string =string.replace('-s','s')
    string =string.replace('?','')
    string= string.replace('minutes/-','minutes')
    string=string.replace('-h','h')
    string=string.replace('-current','')
    string=string.replace('-NA','minutes')

    day=0
    hour=0
    minute=0
    second=0

    if string =='Not Sure'or string =='Nan'  or string=='-' or string=='' or string=='on-going' or string=='1-month'or string=='Unknown-afewhours' or string=='NorthI-77' or string=='Fewminutes(maybe2-3':
        return hour,minute,second
    if string =='4-5':
        string='5minutes'
    if string =='7-8':
        string='8minutes'
    if string =='1-2':
        string='2minutes'
    if string =='2-3':
        string='2minutes'
    if string=='3-4':
        string='4minutes'
    if string=='7:55pm-8:34pm':
        string='40minutes'
    if string =='5-10':
        string='7minutes'
    if string=='9pm-7am':
        string='8hours'
    if string=='10:00pm-10:40pm':
        string='40minutes'
    if string=='2-3:00':
        string='1hours'
    if string=='5-6':
        print 'lol'
        string='1hours'
    if string=='10minutes-3hours':
        string='1hours'
    if string=='1second/-0.5Sec':
        string='1second'

    if 'days' in string:
        hour=24
        return hour,minute,second

    if ':' in string:
        indexDot=string.index(":")
        minute=string[: indexDot]
        second=string[indexDot+1:]

    if '-' in string:
        indexBar=string.index('-')
        numberDigitBefore=0
        numberDigitAfter=0

        if string[indexBar-1].isdigit():
            if string[indexBar-2].isdigit():
                numberDigitBefore= 2

            else:
                numberDigitBefore = 1

        if string[indexBar+1].isdigit():
            if string[indexBar+2].isdigit():
                numberDigitAfter= 2
            else:
                numberDigitAfter = 1


        approx=str((int(string[indexBar-numberDigitBefore: indexBar])+int(string[indexBar+1: indexBar+numberDigitAfter+1]))/2)
        string= approx+string[indexBar+1+numberDigitAfter:]




    if 'hour' in string:
        hour=string.index('hour')
        if string[hour-1].isdigit():
            if string[hour-2].isdigit():
                hour= string[hour-2:hour]
            else:
                hour= string[hour-1]



    if 'minute' in string:
        minute=string.index('minute')
        if string[minute-1].isdigit():
            if string[minute-2].isdigit():
                minute=string[minute-2:minute]
            else:
                minute=string[minute-1]


    if 'second' in string:
        second=string.index('second')
        if string[second-1].isdigit():
            if string[second-2].isdigit():
                second= string[second-2:second]
            else:

                second= string[second-1]


    second=''.join(i for i in str(second) if i.isdigit())
    minute=''.join(i for i in str(minute) if i.isdigit())
    hour =''.join(i for i in str(hour) if i.isdigit())
    if len(second)<1:
        second=0
    if len(minute)<1:
        minute=0
    if len(hour)<1:
        hour=0
    if len(str(second))>2:
        second=str(second)[0:2]
    if len(str(hour))>2:
        hour=str(hour)[0:2]
    if len(str(minute))>2:
        minute=str(minute)[0:2]

    hour=int(hour)
    minute=int(minute)
    second=int(second)
    if second>=60:
        remainder=second-60
        minute+=1
        second=remainder

    if minute>=60:
        remainder=minute-60
        hour+=1
        minute=remainder

    if hour>=23:
        hour=23


    print hour,minute,second
    return time(hour,minute,second)


    return time(hour,minute,second)

sick_days = [10, 4, -5, 19]
total = sum(sick_days)

if sick_days[0] > 0 and sick_days[1] > 0 and sick_days[2] > 0 and sick_days[3]> 0: 
    print('Frank was sick for', total, 'days')
else:
    print('Frank can’t be sick for -1 days')
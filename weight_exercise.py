w = input('Weight: ')
m = input('(K)g or (L)bs: ')
if m.upper() == 'K':
    print('Weight in Lbs: ' + str(float(w) / 0.45359237))
elif m.upper() == 'L':
    print('Weight in Kg: ' + str(float(w) * 0.45359237))
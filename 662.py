def shkala():
    b = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'F': []
        }
    a = [int(x) for x in input().split()]
    for i in a:
        if 90<=i<100:
            b['A'].append(i)
        elif 80<=i<90:
            b['B'].append(i)
        elif 70<=i<80:
            b['C'].append(i)
        elif 60<=i<70:
            b['D'].append(i)
        elif i<60:
            b['F'].append(i)
    print(b)

shkala()

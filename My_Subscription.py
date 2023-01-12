Newspapers={
    'TOI':{'MON':3 , 'TUE':3 , 'WED':3 , 'THUS':3 , 'FRI':3 , 'SAT':5 , 'SUN':6},
    'HINDU':{'MON':2.5 , 'TUE':2.5 , 'WED':2.5 , 'THUS':2.5 , 'FRI':2.5 , 'SAT':4 , 'SUN':4},
    'ET':{'MON':4 , 'TUE':4 , 'WED':4 , 'THUS':4 , 'FRI':4 , 'SAT':4 , 'SUN':10},
    'BM':{'MON':1.5 , 'TUE':1.5 , 'WED':1.5 , 'THUS':1.5 , 'FRI':1.5 , 'SAT':1.5 , 'SUN':1.5},
    'HT':{'MON':2 , 'TUE':2 , 'WED':2 , 'THUS':2 , 'FRI':2 , 'SAT':4 , 'SUN':4}
}
T=sum(Newspapers['TOI'].values())
H=sum(Newspapers['HINDU'].values())
E=sum(Newspapers['ET'].values())
B=sum(Newspapers['BM'].values())
Ht=sum(Newspapers['HT'].values())
budget=float(input())
if budget>=B+Ht:
    print("{'BM','HT'}")
if budget>=B+E:
    print("{'BM','ET'}")
if budget>=B+H:
    print("{'BM','HINDU'}")
if budget>=B+T:
    print("{'BM','TOI'}")
if budget>=T+H:
    print("{'TOI','HINDU'}")
if budget>=T+E:
    print("{'TOI','ET'}")
if budget>=T+Ht:
    print("{'TOI','HT'}")
if budget>=H+E:
    print("{'HINDU','ET'}")
if budget>=H+Ht:
    print("{'HINDU','HT'}")
if budget>=E+Ht:
    print("{'ET','HT'}")




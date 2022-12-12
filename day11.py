sample = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

realIn = '''Monkey 0:
  Starting items: 59, 65, 86, 56, 74, 57, 56
  Operation: new = old * 17
  Test: divisible by 3
    If true: throw to monkey 3
    If false: throw to monkey 6

Monkey 1:
  Starting items: 63, 83, 50, 63, 56
  Operation: new = old + 2
  Test: divisible by 13
    If true: throw to monkey 3
    If false: throw to monkey 0

Monkey 2:
  Starting items: 93, 79, 74, 55
  Operation: new = old + 1
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 1

Monkey 3:
  Starting items: 86, 61, 67, 88, 94, 69, 56, 91
  Operation: new = old + 7
  Test: divisible by 11
    If true: throw to monkey 6
    If false: throw to monkey 7

Monkey 4:
  Starting items: 76, 50, 51
  Operation: new = old * old
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 5

Monkey 5:
  Starting items: 77, 76
  Operation: new = old + 8
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 6:
  Starting items: 74
  Operation: new = old * 2
  Test: divisible by 5
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 7:
  Starting items: 86, 85, 52, 86, 91, 95
  Operation: new = old + 6
  Test: divisible by 7
    If true: throw to monkey 4
    If false: throw to monkey 5'''
def operation(inString, old):
    l = inString.split(' = ')
    l = l[-1].split()
    n1 = old
    op = l[1]
    n2 = l[-1]
    if n2=='old':
        n2 = n1
    else:
        n2 = int(n2)
    if op=='+':
        new = n1 + n2
    else:
        new = n1 * n2
    return new

def mb(sample):
    s = sample.split('\n')
    md = dict()
    for p in s:
        if 'Monkey' in p:
            l = p.split()
            m = int(l[1][0:-1])
            di = []
        elif 'Starting' in p:
            l = p.split(':')
            wl = l[1].strip().split(', ')
            wl = [int(x) for x in wl]
            di.append(wl)
        elif 'Operation' in p:
            di.append(p)
        elif 'Test' in p:
            l = p.split()
            db = int(l[-1])
            di.append(db)
        elif 'true' in p:
            l = p.split()
            nm = int(l[-1])
            di.append(nm)    
        elif 'false' in p:
            l = p.split()
            nm = int(l[-1])
            di.append(nm)   
        md[m] = di  

    r = 1
    mc = dict()
    for m in md.keys():
        mc[m] = 0
    while r<21:
        for m in md.keys():
            wl = md[m][0].copy()
            op = md[m][1]
            db = md[m][2]
            tnm = md[m][3]
            fnm = md[m][4]
            for i in wl:
                mc[m] = mc[m] + 1
                nwl = operation(op, i)
                nwl = int(nwl/3)
                if nwl % db==0:
                    nmd = md[tnm][0]
                    nmd.append(nwl)
                    md[tnm][0] = nmd.copy()
                else:
                    nmd = md[fnm][0]
                    nmd.append(nwl)
                    md[fnm][0] = nmd.copy()
                md[m][0].pop(0)
                
        r += 1
    mcl = []
    for m in mc.keys():
        mcl.append(int(mc[m]))
    mcl.sort()
    mc1 = mcl[-1]
    mc2 = mcl[-2]    
    mb = mc1 * mc2
                    


    return mb
print(mb(sample))
print(mb(realIn))

def mb2(sample):
    s = sample.split('\n')
    md = dict()
    allds = []
    for p in s:
        if 'Monkey' in p:
            l = p.split()
            m = int(l[1][0:-1])
            di = []
        elif 'Starting' in p:
            l = p.split(':')
            wl = l[1].strip().split(', ')
            wl = [int(x) for x in wl]
            di.append(wl)
        elif 'Operation' in p:
            di.append(p)
        elif 'Test' in p:
            l = p.split()
            db = int(l[-1])
            di.append(db)
            allds.append(db)
        elif 'true' in p:
            l = p.split()
            nm = int(l[-1])
            di.append(nm)    
        elif 'false' in p:
            l = p.split()
            nm = int(l[-1])
            di.append(nm)   
        md[m] = di  
    ds = 1
    for i in allds:
        ds = ds * i
    r = 1
    mc = dict()
    for m in md.keys():
        mc[m] = 0
    while r<10001:
        for m in md.keys():
            wl = md[m][0].copy()
            op = md[m][1]
            db = md[m][2]
            tnm = md[m][3]
            fnm = md[m][4]
            for i in wl:
                mc[m] = mc[m] + 1
                nwl = operation(op, i)
                #nwl = int(nwl/3)
                nwl = nwl % ds
                if nwl % db==0:
                    nmd = md[tnm][0]
                    nmd.append(nwl)
                    md[tnm][0] = nmd.copy()
                else:
                    nmd = md[fnm][0]
                    nmd.append(nwl)
                    md[fnm][0] = nmd.copy()
                md[m][0].pop(0)
                
        r += 1
    mcl = []
    for m in mc.keys():
        mcl.append(int(mc[m]))
    mcl.sort()
    mc1 = mcl[-1]
    mc2 = mcl[-2]    
    mb = mc1 * mc2
                    


    return mb
#print(mb2(sample))
print(mb2(realIn))
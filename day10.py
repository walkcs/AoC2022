sample = '''noop
addx 3
addx -5'''

s2 = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

realIn = '''noop
noop
noop
addx 6
noop
addx 30
addx -26
noop
addx 5
noop
noop
noop
noop
addx 5
addx -5
addx 6
addx 5
addx -1
addx 5
noop
noop
addx -14
addx -18
addx 39
addx -39
addx 25
addx -22
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 2
noop
addx 3
noop
addx 3
addx 2
addx 5
addx 4
addx -18
addx 17
addx -38
addx 5
addx 2
addx -5
addx 27
addx -19
noop
addx 3
addx 4
noop
noop
addx 5
addx -1
noop
noop
addx 4
addx 5
addx 2
addx -4
addx 5
noop
addx -11
addx 16
addx -36
noop
addx 5
noop
addx 28
addx -23
noop
noop
noop
addx 21
addx -18
noop
addx 3
addx 2
addx 2
addx 5
addx 1
noop
noop
addx 4
noop
noop
noop
noop
noop
addx 8
addx -40
noop
addx 7
noop
addx -2
addx 5
addx 2
addx 25
addx -31
addx 9
addx 5
addx 2
addx 2
addx 3
addx -2
noop
addx 3
addx 2
noop
addx 7
addx -2
addx 5
addx -40
addx 20
addx -12
noop
noop
noop
addx -5
addx 7
addx 7
noop
addx -1
addx 1
addx 5
addx 3
addx -2
addx 2
noop
addx 3
addx 2
noop
noop
noop
noop
addx 7
noop
noop
noop
noop'''

def compProg(sample):
    x = 1
    s = sample.split('\n')
    c = 1
    cycles = [20,60,100,140,180,220]
    sigStrL = []
    for i in s:
        ins = i.split()
        w = ins[0]
        if w=='noop':
            c += 1
        else:
            n = int(ins[1])
            c += 1
            sigStr = c * x
            if c in cycles:
                sigStrL.append(sigStr)
            c += 1
            x += n
        sigStr = c * x
        if c in cycles:
            sigStrL.append(sigStr)
    return sum(sigStrL)
print(compProg(s2))
print(compProg(realIn))

def compProg2(sample):
    x = 1
    sp = [0,1,2]
    s = sample.split('\n')
    c = 0
    crt = []
    p = [39,79,119,159,199,239]
    scrt = ''
    t = 0
    for i in s:
        ins = i.split()
        w = ins[0]
        if c==0:
            scrt = scrt + '#'
        if w=='noop':
            c += 1
            if c-t*40 in sp:
                scrt = scrt + '#'
            else:
                scrt = scrt + '.'
            if c in p:
                crt.append(scrt)
                scrt = ''
                sp = [sp[0]-40, sp[1]-40, sp[2]-40]
                t += 1
        else:
            c += 1
            if c-t*40 in sp:
                scrt = scrt + '#'
            else:
                scrt = scrt + '.'
            if c in p:
                crt.append(scrt)
                scrt = ''
                sp = [sp[0]-40, sp[1]-40, sp[2]-40]
                t += 1
            n = int(ins[1])
            c += 1
            x += n
            sp = [x-1, x, x+1]

            if c-t*40 in sp:
                scrt = scrt + '#'
            else:
                scrt = scrt + '.'
            if c in p:
                crt.append(scrt)
                scrt = ''
                sp = [sp[0]-40, sp[1]-40, sp[2]-40]
                t += 1

    scrt = ''
    for r in crt:
        for p in r:
            scrt = scrt + p
        print(scrt)
        scrt = ''
    #return crt
print(compProg2(s2))
print(compProg2(realIn))
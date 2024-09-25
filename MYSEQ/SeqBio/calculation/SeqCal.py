
# SeqCal module
def countBase(seq, base):
    return seq.count(base.upper())

def countBasesDict(seq):
    basesM = {}
    seq = seq.upper()
    for base in seq:
        if base in basesM:
            basesM[base] += 1
        else:
            basesM[base] = 1
    return basesM

def gcContent(seq):
    # G+C/(A+T+G+C)
    seq = seq.upper()
    return (countBase(seq, 'G') + countBase(seq, 'C'))/len(seq)

def atContent(seq):
    # A+T/(A+T+G+C)
    seq = seq.upper()
    return (countBase(seq, 'A') + countBase(seq, 'T'))/len(seq)



# Test
if __name__ == '__main__':
    print("Base Count:")
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    print(seq)
    print(countBase(seq,'T'))

if __name__ == '__main__':
    print("GC Content:")
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    
    print(gcContent(seq))

if __name__ == '__main__':
    print("AT Content:")
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    
    print(atContent(seq))

if __name__ == '__main__':
    print("Base count by dict:")
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    print(seq)
    print(countBasesDict(seq))



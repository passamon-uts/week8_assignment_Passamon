import re

def cpgSearch(seq):
    cpgs = []
    for m in re.finditer(r'CG', seq, re.I):
        cpgs.append((m.group(), m.start(), m.end()))
    return cpgs

def enzTargetsScan(seq, enz):
    resEnzyme = dict(EcoRI='GAATTC', BamHI='GGATCC', 
                 HindIII='AAGCTT',AccB2I='[AG]GCGC[CT]',
                 AasI='GAC[ATCG][ATCG][ATCG][ATCG][ATCG][ATCG]GTC',
                 AceI='GC[AT]GC')
    out = []
    if enz in resEnzyme:
        for m in re.finditer(resEnzyme['EcoRI'],seq):
            out.append((m.group(), m.start(), m.end()))
            
    return out

# Test
# if __name__ == '__main__':
#     print("enzTargetsScan:",__name__)
#     seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
#     enz = 'EcoRI'
#     print(seq)
#     print(enzTargetsScan(seq, enz))
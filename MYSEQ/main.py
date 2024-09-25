from SeqBio.calculation.SeqCal import *
from SeqBio.pattern.SeqPattern import *
from SeqBio.seqMan.dnaconvert import *

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action="store_true",
                           help="Convert DNA to reverse-complementary")
    
    
    Transcriptionsearch_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    Transcriptionsearch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    Transcriptionsearch_command.add_argument("-r", "--revcomp", action="store_true",
                           help="Convert DNA to reverse-complementary")
    
    TranslationSearch_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    TranslationSearch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    TranslationSearch_command.add_argument("-r", "--revcomp", action="store_true",
                           help="Convert DNA to reverse-complementary")
    
    
    enzserch_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzserch_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Provide sequence")
    enzserch_command.add_argument("-r", "--revcomp", action="store_true",
                           help="Enzyme name")
    

    return parser 
    

def main():
    parser = argparserLocal()
    args = parser.parse_args()

    if args.seq:
        seq = args.seq.upper()  # Convert sequence to uppercase

        if args.command == 'gcContent':
            print("Input:", args.seq, "\nGC content =", gcContent(seq))

        elif args.command == 'countBases':
            if args.revcomp:
                seq = reverseComplementSeq(seq)

            print("Input:", args.seq, "\nCount of bases =", countBasesDict(seq))

        elif args.command == 'enzTargetsScan':
            if args.revcomp:
                seq = reverseComplementSeq(seq)

            print("Input:", args.seq, "\n", args.enz, "sites =", enzTargetsScan(seq, args.enz))

        elif args.command == 'transcription':
            if args.revcomp:
                seq = reverseComplementSeq(seq)

            rna_seq = dna2rna(seq)
            print("Input:", args.seq, "\nTranscription =", rna_seq)

        elif args.command == 'translation':
            if args.revcomp:
                seq = reverseComplementSeq(seq)

            protein_seq = dna2protein(seq)
            print("Input:", args.seq, "\nTranslation =", protein_seq)

    else:
        print("Error: Sequence not provided.")

if __name__ == "__main__":
    main()

# Input
# seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
# seq = seq.upper()
# print("Transcription: ", dna2rna(seq))
# print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
# print("Translation: ", dna2protein(seq))
# print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
# print("GC Content:", gcContent(seq))
# print("Count Bases: ", countBasesDict(seq))
# print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
# print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
# print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))
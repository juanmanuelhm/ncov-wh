"""
Identify matching haplotypes
"""
import argparse
from Bio import AlignIO, SeqIO
from Bio.Align import MultipleSeqAlignment

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Identify matching haplotypes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('--alignment', type=str, metavar="FASTA", required=True, help="input FASTA alignment")
    args = parser.parse_args()

    aln = AlignIO.read(args.alignment, "fasta")
    ref = [a for a in aln if a.id=='Wuhan/Hu-1/2019'][0]

    ref_expected = ['C', 'C']
    positions = [20402, 28821]
    wt_expected = ['T', 'A']

    for i in range(0, len(positions)):
        assert(ref[positions[i]-1]==ref_expected[i])

    newwave_records = []
    for seq in aln:
        include = True
        for i in range(0, len(positions)):
            if seq[positions[i]-1]!=wt_expected[i]:
                include = False
        if include:
            newwave_records.append(seq)
            print(seq.name)

    print(len(newwave_records), "total matches")

def reverse_base(base):
    """compute reverse complement of sequence."""
    base = base.lower()
    rev_seq = seq[-1::-1]:
        seq.replace('a', 'T')
        seq.replace('t', 'A')
        seq.replace('c', 'G')
        seq.replace('g', 'C')
    return rev_seq

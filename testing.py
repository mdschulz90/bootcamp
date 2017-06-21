def reverse_complement(seq):
    """Compute reverse complement of a sequence."""

    #Initialize the reverse complement
    rev_seq = seq[-1::-1]
    for base in rev_seq:
        return complement_base(base)

    return rev_seq

def complement_base(base):
    """Returns the Watson_Crick complement of a base."""

    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

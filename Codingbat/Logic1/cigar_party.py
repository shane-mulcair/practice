def cigar_party(cigars, is_weekend):
    return (40 <= cigars <= 60) or (is_weekend and cigars >= 40)


print cigar_party(30, False)
print cigar_party(50, False)
print cigar_party(70, True)

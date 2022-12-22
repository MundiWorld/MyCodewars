def bool_to_word(boolean):
    #It is True?
        if boolean == True:
            return("Yes")
    #For this specific case work an else here,because we know if isn't true is false.
        else:
            return("No")
#2th thymine to Uracil

def dna_to_rna(dna):
    for i in dna:
        if i == "T":
            dna = dna.replace("T","U")
    return(dna)



#did at 20-12-2022
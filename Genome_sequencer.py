# INTRODUCTION TO GENOME SEQUENCER/ASSEMBLER
print("\t\t\t\t\t☺☺☺ WELCOME TO THIS GENOME ASSEMBLER/SEQUENCER ☺☺☺")

'''LET'S TELL YOU ABOUT BASES OF A DNA SEQUENCES
A = ADENINE
C = CYTOSINE
G = GUANINE
T = THYMINE
A IS COMPLEMENT TO T AND C IS COMPLEMENT TO G AND VICE VERSA'''

print("\t\t\t\t\tYOU CAN PERFORM FOLLOWING OPERATIONS ON A GIVEN DNA SEQUENCE STRING: -")
print("\t\t\t\t\t(1.)CHEKING IF GIVEN DNA IS VALID OR NOT")
print("\t\t\t\t\t(2.)CHECKING THE EQUALITY OF STRINGS FROM GIVEN DNA SEQUENCE")
print("\t\t\t\t\t(3.)TO GET COMPLEMENT AND REVERSE COMPLEMENT OF A STRINGFROM GIVEN DNA SEQUENCE")
print("\t\t\t\t\t(4.)CHECKING THE LENGTH OF A DNA STRING")
print("\t\t\t\t\t(5.)FIND THE INDIVIDUAL NUMBER OF BASES PRESENT IN A DNA SEQUENCE")
print("\t\t\t\t\t(6.)TO REPLACE UNWANTED PART OF A STRING FROM GIVEN DNA SEQUENCE")
print("\t\t\t\t\t(7.)TO ADD TWO DIFFERENT STRINGS FROM SAME OR DIFFERENT DNA SEQUENCES")

while True:
    print("\t\t\t\t\tENTER THE CHOICE FROM ABOVE GIVEN LIST TO PERFORM DESIRED OPERATIONS")
    your_choice = int(input())
# CHECKING FOR VALIDITY OF DNA SEQUENCE
    if your_choice == 1:
        print("WELCOME 😊 !! WE ARE GOING TO CHECK IF GIVEN DNA SEQUENCE IS VALID OR NOT\nPROVIDE STRING FROM DNA SEQUENCE")
        str1 = input().upper()
        base1 = ''
        j = 0
        for base in str1:
            x = 0
            y = 0
            z = 0
            i = 0
            if base == 'A':
                x = x + 1
            elif base == 'C':
                y = y + 1
            elif base == 'G':
                z = z + 1
            elif base == "T":
                i = i + 1
            else:
                j = j + 1
            base1 = base
            pos = str1.find(base1)
        if j != 0:
            print("INVALID DNA SEUQNCE")
            print(base1)
            print("INVALID AT", pos)
        else:
            print("VALID DNA SEQUENCE")
# CHECKING THE EQUALITY OF STRINGS FROM GIVEN DNA SEQUENCE
    elif your_choice == 2:
        print("WELCOME 😊 !! WE ARE GOING TO CHECK EQUALITY OF STRINGS FROM DNA SEQUENCES GIVEN BY YOU\nPROVIDE STRING FROM DNA SEQUENCE 1: -")
        string1 = input().upper()  # STRING FROM DNA SEQUENCE 1
        print("PROVIDE STRING FROM DNA SEQUENCE 2")
        string2 = input().upper()  # STRING FROM DNA SEQUENCE 2
        if string1 == string2:
            print("STRINGS FROM DNA SEQUENCE 1 AND 2 GOT MATCHED")
        else:
            print("SORRY!! BOTH STRINGS FROM DNA SEQUENCES ARE DIFFERENT")
# GETTING THE COMPLEMENT AND REVERSE COMPLEMENT FOR A STRING OF OF GIVEN DNASEQUENCE
    elif your_choice == 3:
        print("WELCOME 😊 !! WE ARE GOING TO TELL YOU COMPLEMENT AND REVERSE COMPLEMENT OF A STRING FROM DNA SEQUENCE GIVEN BY YOU\nPROVIDE THE ORIGINAL DNA SEQUENCE:-")
        origin = input().upper()
        complement = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
        t = ''
        s = ''
# COMPLEMENT OF A SEQUENCE
        for bases in origin:
            t = t + complement[bases]
        print("COMPLEMENT OF STRING FROM GIVEN ORIGINAL DNA SEQUENCE IS: \t{",t,"}")
# REVERSE COMPLEMENT OF A SEQUENCE
        for bases in origin:
            s = complement[bases] + s
        print("REVERSE COMPLEMENT OF STRING FROM GIVEN ORIGINAL DNA SEQUENCE IS: \t{",s,"}")
# GETTING THE LENGTH OF A DNA SEQUENCE
    elif your_choice == 4:
        print("WELCOME 😊 !! WE ARE GOING TO FIND OUT LENGTH OF A STRING OF DNA SEQUENCE GIVEN BY YOU\nPROVIDE THE DNA SEQUENCE: -")
        dna_seq = input().upper()
        length = 0
        for bases in dna_seq:
            length = length + 1
        print("LENGTH OF GIVEN DNA SEQUENCE IS:\t{", length, "}")
# NUMBER OF BASES PRESENT IN A DNA SEQUENCE
    elif your_choice == 5:
        print("WELCOME 😊 !! WE ARE GOING TO TELL NUMBER OF BASES PRESENT IN A DNA SEQUENCE\nPROVIDE THE DNA SEQUENCE: -")
        DNA_seq = input().upper()
        x = 0
        y = 0
        i = 0
        j = 0
        for bases in DNA_seq:
            if bases == 'A':
                x = x + 1
            elif bases == 'C':
                y = y + 1
            elif bases == 'G':
                i = i + 1
            else:
                j = j + 1
        print("THERE ARE", x, "ADENIINES IN GIVEN SEQUENCE")
        print("THERE ARE", y, "CYTOSINES IN GIVEN SEQUENCE")
        print("THERE ARE", i, "GUANINES IN GIVEN SEQUENCE")
        print("THERE ARE", j, "THYMINES IN GIVEN SEQUENCE")
# REPLACEMENT OF UNWANTED PART OR UNWANTED BASE FROM ASEQUENCE
    elif your_choice == 6:
        print("WELCOME 😊 !! WE ARE GOING TO REMOVE THE UNWANTED OR THE WRONG BASE FROM A GIVEN DNA SEQUENCE\nPROVIDE THE DNA SEQUENCE: -")
        DNA_SEQ = input().upper()
        print("PROVIDE THE UNWANTED PART")
        unwant_seq = input().upper()
        print("PROVIDE THE REQUIRED PART")
        req_base = input().upper()
        NEW_SEQ = DNA_SEQ.replace(unwant_seq, req_base)
        print("NEW REPLACED SEQUENCE IS GIVEN BY\t\t\t{", NEW_SEQ, "}")
# ADDING DIFFERENT DNA SEQUNCES
    elif your_choice == 7:
        print("WELCOME 😊 !! WE ARE GOING TO ADD TWO DNA SEQUENCES TO GIVE A NEW SEQUENCE\nPROVIDE THE CONSTITUENT SEUENCES: -")
        SEQ1 = input().upper()
        SEQ2 = input().upper()
        RESULT = SEQ1 + SEQ2
        print("RESULTANT SEQUENCE IS GIVEN BY\t\t\t{", RESULT, "}")
    else:
        print("CHOICE CAN NOT BE PROCESSED")
        break
    print("\t\t\t\t\t\t\t\t\t\t\t\t\tTHANK YOU")

print("\t\t\t\t\t\t\t\t\t\t😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊")

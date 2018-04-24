grades=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F+','F','F-','P','IP']
with open("UnofficialTranscript.txt") as openfile:
    bbool=False
    termnumber=1
    for line in openfile:
        line1 = str.split(line)
        if "----------" in line and ('20' in line or '19' in line):
            print "\n"+line
            if termnumber<=3:
                stermnumber="I"*termnumber
            elif termnumber==4:
                stermnumber="IV"
            elif termnumber<9:
                stermnumber="V"+"I"*(termnumber-5)
            elif termnumber==9:
                stermnumber="IX"
            else:
                stermnumber="X"+"I"*(termnumber-5)
            print "TERM "+str(stermnumber)+ "\n"
            termnumber+=1
        if bbool:
            print prevline+line1[-3]
            bbool=False
        if "CAL" in line1 or "CH" in line1 or "E" in line1 or "MA" in line1 or "MGT" in line1 or "PEP" in line1 or "EE" in line1 or "CPE" in line1 or "HSS" in line1 or "PRV" in line1 or "TG" in line1 or "BT" in line1 or "IDE" in line1 or "HMU" in line1 or "HAR" in line1 or "HHS" in line1 or "LSP" in line1 or "HLI" in line1 or "HMU" in line1 or "HPL" in line1 or "COMM" in line1 or "HST" in line1 or "HTH" in line1:
            line2 = ("Class: " + line1[0] + line1[1] + " " + "Grade: " + line1[-3])
            if line1[-3] not in grades:
                if line1[-2] in grades:
                    line2 = ("Class: " + line1[0] + line1[1] + " " + "Grade: " + line1[-2])
                    print line2
                else:
                    bbool=True
                    prevline=("Class: " + line1[0] + line1[1] + " " + "Grade: ")
            else:
                print line2
        if "PE" in line1:
            line2 = ("Class: " + line1[0] + line1[1] + " " + "Grade: " + line1[-2])
            print line2


       

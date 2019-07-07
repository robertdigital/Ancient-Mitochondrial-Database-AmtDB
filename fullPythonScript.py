import pandas as pd
# import openpyxl
import sys
import os

#uncomment this piece of code if this error prints out in terminal (filename = sys.argv[1] IndexError: list index out of range); otherwise ignore
# if len(sys.argv)<2:
#     print "Fatal: You forgot to include the directory name on the command line."
#     print "Usage:  python %s <directoryname>" % sys.argv[0]
#     sys.exit(1)

cwd = os.getcwd()
all_files = os.listdir(cwd)
fa_files = []
for file in all_files:
    if file.endswith(".fa"):
        fa_files.append(file)

del all_files
super_final = []

for filename in fa_files:

	# filename = sys.argv[1]

	fileout=open(filename)
	data=fileout.read().strip("\n")
	totalentries=data.count(">")
	data=data.lstrip(">")
	datalist=data.split(">")

	# global final
	final=[]
	#global wb
	#global ws
	#wb = Workbook(raw_input("Enter name of output file (use .xlsx extension:"))
	#ws = wb.add_worksheet("New Sheet")

	for item in datalist:
	    item=item.strip("\n")
	    item=item.strip(">")
	    separator=item.find("\n")
	    item=item.replace("\n"," ")
	    info=item[:separator]                                    #info about the entry i.e the first line
	    global seq
	    seq=item[separator:]                                     # sequence in the entry
	    global seq_length                                        #total dinucleotide
	    for j in seq:
	        if j=="A" or j=="C" or j=="T" or j=="G":
	            continue
	        else:
	            seq=seq.replace(j,"")
	    seq_length=len(seq)

	    if seq!="Sequence unavailable":
	        GC=float(seq.count("GC"))
	        CG=float(seq.count("CG"))
	        AT=float(seq.count("AT"))
	        TA=float(seq.count("TA"))
	        AC=float(seq.count("AC"))
	        CA=float(seq.count("CA"))
	        AG=float(seq.count("AG"))
	        GA=float(seq.count("GA"))
	        CT=float(seq.count("CT"))
	        TC=float(seq.count("TC"))
	        GT=float(seq.count("GT"))
	        TG=float(seq.count("TG"))

	    AA=CC=TT=GG=float(0)
	    for i in range(0,len(seq)-1):
	        if seq[i]=="A" and seq[i+1]=="A":
	            AA+=1
	        if seq[i]=="C" and seq[i+1]=="C":
	            CC+=1
	        if seq[i]=="T" and seq[i+1]=="T":
	            TT+=1
	        if seq[i]=="G" and seq[i+1]=="G":
	            GG+=1

	    A=G=C=T=float(0)
	    for i in seq:
	        if i=="A":
	            A+=1
	        if i=="G":
	            G+=1
	        if i=="C":
	            C+=1
	        if i=="T":
	            T+=1


	    if C!=0 and G!=0:
	        pGC=(GC*seq_length)/(G*C)
	        pCG=(CG*seq_length)/(C*G)
	    else:
	        pGC=0
	        pCG=0
	    if A!=0 and T!=0:            
	        pAT=(AT*seq_length)/(A*T)
	        pTA=(TA*seq_length)/(T*A)
	    else:
	        pAT=0
	        pTA=0
	    if A!=0 and C!=0:
	        pAC=(AC*seq_length)/(A*C)
	        pCA=(CA*seq_length)/(C*A)
	    else:
	        pAC=0
	        pCA=0
	    if A!=0 and G!=0:
	        pAG=(AG*seq_length)/(A*G)
	        pGA=(GA*seq_length)/(G*A)
	    else:
	        pAG=0
	        pGA=0
	    if C!=0 and T!=0:
	        pCT=(CT*seq_length)/(C*T)
	        pTC=(TC*seq_length)/(T*C)
	    else:
	        pCT=0
	        pTC=0
	    if G!=0 and T!=0:
	        pGT=(GT*seq_length)/(G*T)
	        pTG=(TG*seq_length)/(T*G)
	    else:
	        pGT=0
	        pTG=0
	    if A!=0:
	        pAA=(AA*seq_length)/(A*A)
	    else:
	        pAA=0
	    if C!=0:
	        pCC=(CC*seq_length)/(C*C)
	    else:
	        pCC=0
	    if T!=0:
	        pTT=(TT*seq_length)/(T*T)
	    else:
	        pTT=0
	    if G!=0:
	        pGG=(GG*seq_length)/(G*G)
	    else:
	        pGG=0

	    # removing trailing \n or \r  
	    info = info.rstrip()

	    final.append((str(info),str(seq_length),str(A),str(C),str(T),str(G),str(GC),str(CG),str(AT),str(TA),str(AC), str(CA),str(AG), str(GA),str(CT),str(TC),str(GT),str(TG),str(AA),str(CC),str(TT),str(GG), str( pGC ),str( pCG  ),str( pAT ),str( pTA ),str( pAC ),str( pCA ),str( pAG ),str( pGA ),str( pCT ),str( pTC ), str( pGT ), str( pTG), str( pAA ), str( pCC ), str( pTT ), str( pGG )))
	    super_final.append(final[0])
#pd.DataFrame(final).to_excel("output.xlsx",header=False,index=False)
    # print (str(info) + "," + str(seq_length) + "," + str(A) + "," + str(C) + "," + str(T) + "," + str(G) + "," + str(GC) +  "," + str( CG ) + "," + str( AT ) + "," + str( TA ) + "," + str( AC ) + "," + str( CA ) + "," + str( AG ) + "," + str( GA ) + "," + str( CT ) + "," + str( TC ) + "," + str( GT ) + "," + str( TG ) + "," + str( AA ) + "," + str( CC ) + "," + str( TT ) + "," + str( GG ) +  "," + str( pGC ) + "," + str( pCG  ) + "," + str(  pAT ) + "," + str( pTA ) + "," + str( pAC ) + "," + str( pCA ) + "," + str( pAG ) + "," + str( pGA ) + "," + str( pCT ) + "," + str( pTC ) + "," + str( pGT ) + "," + str( pTG) + "," + str( pAA ) + "," + str( pCC ) + "," + str( pTT ) + "," + str( pGG ))


df = pd.DataFrame(super_final, columns=["info","seq_length","A","C","T","G","GC","CG","AT","TA","AC", "CA","AG", "GA","CT","TC","GT","TG","AA","CC","TT","GG","pGC","pCG","pAT","pTA","pAC","pCA","pAG","pGA","pCT","pTC", "pGT","pTG","pAA","pCC","pTT","pGG"])
df.to_csv("super_final"+".csv", sep='\t', encoding='utf-8')
#for row, item in enumerate(final):
 #   ws.write_row(row, 0, item)
#wb.close()
fileout.close()

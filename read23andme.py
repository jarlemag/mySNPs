#read23andme.py

import string
filename = 'Snippet.txt'

referencesequence = 'CRCh36'


#Open dataset

def createlist(filename): #Extract SNP data from a 23andme file.

    with open(filename) as dataset:
        listoflines = dataset.readlines()

    SNPlist = []

    for line in listoflines:
        if line[0] != '#': #Unless the line has been commented out.
            linesplit = string.split(line)
            currentSNP = {'rsID':linesplit[0],'Chromosome':linesplit[1],
                      'Position':linesplit[2],'Genotype':linesplit[3],'Reference':referencesequence}
            SNPlist.append(currentSNP)
    return SNPlist

def printfile():
    with open(filename) as f:
        for line in f.readlines():
            print line

mylist = createlist(filename)

        
#printfile()

#print SNPlist


def returnSNP(rsID,SNPlist):
    if type(rsID) == int:
        rsID = str(rsID)
    snpfound = False
    for SNP in SNPlist:
        if SNP['rsID'] == rsID:
            snpfound = True
            return SNP
    if snpfound == False:
        print 'Could not find entry for rsID %s' % rsID

def showinfo(SNP):
    print 'Selected SNP:'
    print 'rsID:',SNP['rsID']
    print 'Chromosome:',SNP['Chromosome']
    print 'Position:',SNP['Position']
    print 'Genotype:',SNP['Genotype']
    print 'Reference sequence:',SNP['Reference']

anSNP = returnSNP('rs3934834',mylist)

returnSNP('kake',mylist)


#def comparetwo(file1,file2):
    #Compare two genotypefiles

#def find_union(list1,list2):
    #Find SNPs which are in both of two lists
 #   repeatedSNPs = []
  #  for element in zip(list1,list2)

showinfo(anSNP)

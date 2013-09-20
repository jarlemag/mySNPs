#read23andme.py


#Imports

import string

#Hardcodd values:

filename = 'Snippet.txt'

referencesequence = 'CRCh36'


#Class definitions:



#Functions:

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

def readpartialfile(filename,percentage): #Extract SNP data from part of a file.
    with open(filename) as dataset:
        listoflines = dataset.readlines()
        SNPlist = []
        numberoflines = len(listoflines)
        getlines = int(numberoflines*percentage/100)
        for i in range(getlines):
            if listoflines[i][0] != '#':
                linesplit = string.split(listoflines[i])
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

def filterlist(key,value,SNPlist):
    matches = []
    for SNP in SNPlist:
        if SNP[filteron] == value:
            matches.append(SNP)
    return matches

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

def listrs(SNPlist):
    rslist = [entry['rsID'] for entry in SNPlist]
    return rslist

small_list = mylist[0:5]

tiny_list = mylist[0:3]

def find_union(SNPlist1,SNPlist2):
    #Find SNPs which are in both of two lists
    rslist1 = listrs(SNPlist1)
    rslist2 = listrs(SNPlist2)
    list1set = set(rslist1)
    unionset = list1set.intersection(rslist2)
    return unionset

def comparefiles(file1,file2):
    #Compare two genotypefiles. Return SNPs which are in both files.
    list1 = createlist(file1)
    list2 = createlist(file2)
    inboth = find_union(list1,list2)
    return inboth

showinfo(anSNP)

print 'Comparing files:'
print comparefiles('snippet.txt','snippet2.txt')

theunion = find_union(mylist,small_list)
print 'Union:',theunion

def getdiploids(SNPlist):
    diploids = []
    for SNP in SNPlist:
        if len(SNP['Genotype']) == 2:
            diploids.append(SNP)
    return diploids

def gethaploids(SNPlist):
    haploids = []
    for SNP in SNPlist:
        if len(SNP['Genotype']) ==1:
            haploids.append(SNP)
    return haploids

def findhomozygotesIDs(SNPlist):
    #Find all homozygous loci
    homozygotes = []
    filteredlist = getdiploids(SNPlist)
    for element in filteredlist:
        if element['Genotype'][0] == element['Genotype'][1]:
            homozygotes.append(element['rsID'])
    return homozygotes

homozygotes = findhomozygotesIDs(small_list)

print 'Homozygotes:',homozygotes

def getposinlist(rsID,SNPlist): #Get the position, in an SNP list, of a dictionary entry with a given rsID
    for i in range(len(SNPlist)):
        if SNPlist[i]['rsID']== rsID:
            index = i
    return index

print 'tinylist:',tiny_list

position = getposinlist('rs3094315',tiny_list)
print 'position:',position
print 'rs:','rs3094315'

def findheterozygotesIDs(SNPlist):
    #Find all heterozygous loci
    heterozygotes = []
    filteredlist = getdiploids(SNPlist)
    for element in filteredlist:
        if element['Genotype'][0] != element['Genotype'][1]:
            heterozygotes.append(element['rsID'])
    return heterozygotes

def sanitycheck(SNPlist):
    #Run a sanity check on a list of SNP genotypes
    sane = True
    N = len(SNPlist)
    if (len(findhomozygotesIDs(SNPlist)) + len(findheterozygotesIDs(SNPlist)) ) != N:
        sane = False
    return sane

print 'Sanitycheck:',sanitycheck(mylist)

def findnoncalled(SNPlist):
    #Find all loci with at least one uncalled base
    noncalled = []
    for SNP in SNPlist:
        if ('N' in SNP['Genotype']) or ('n' in SNP['Genotype']):
            noncalled.append(SNP['rsID'])
    return noncalled

noncalled = findnoncalled(mylist)
print 'noncalled:',noncalled
            

def findgenotype(genotype,SNPlist):
    matching = []
    for SNP in SNPlist:
        if SNP['Genotype'] == genotype:
            matching.append(SNP['rsID'])
    return matching

print findgenotype('GG',tiny_list)

def getchromosome(chromosomenumber,SNPlist):
    return filterlist('Chromosome',chromosomenumber,SNPlist)
    

def getbyposition(position,SNPlist):
    #Fetch one or more SNPs by their position in the reference sequence.
    snps = []
    for SNP in SNPlist:
        if SNP['Position'] == position:
            snps.append(SNP)
    return snps
    
def getbyrefseq(reference,SNPlist):
    return filterlist('Reference',reference,SNPlist)
    
    
import matplotlib.pylab as pl

def zygosityplot(SNPlist):
    counts = []
    counts.append(('heterozygotescount',len(findheterozygotesIDs(SNPlist))))
    counts.append(('homozygotescount',len(findhomozygotesIDs(SNPlist))))
    counts.append(('haploidcount',len(gethaploids(SNPlist))))
    totalcount = sum([i[1] for i in counts])
    left = [i for i in range(len(counts))]
    fig = pl.figure()
    ax = fig.add_subplot(1,1,1)
    ax.bar(left,[i[1] for i in counts],align = 'center') #Create a barplot
    ax.set_xticks(left)
    ax.set_xticklabels([i[0] for i in counts])
    ax.set_ylim([0,totalcount])
    fig.autofmt_xdate() #Autorotates the tick labels
    pl.show()
    return counts,left




def timewarning(elapsedtime,completedfraction,tolerance):
    '''A function to estimate time needed to complete an operation, and give a warning and option to abort
    if the estimated time is too high.
    '''
    timeestimate = elapsedtime/completedfraction
    if timeestimate > tolerance:
        response = input('Estimated time remaining for this operation is %.1f minutes. Continue? (y/n)'
                         % (timeestimate/60))
        if response == 'y' or response == 'Y':
            return True #Signal to continue the operation.
        else:
            return False #Signal to abort the operation.

mydata = readpartialfile('Snippet.txt',80)

zygosityplot(mydata)

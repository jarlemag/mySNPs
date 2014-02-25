#read23andme.py


#Imports

import string

#Hardcoded values:

filename = 'Snippet.txt'

referencesequence = 'CRCh36'

mito = 'genome_Jarle_Pahr_Mito_20130920050521.txt'

bases = 'ATGC'

#Class definitions:

class SingleNucleotidePolymorphism:
    def __init__(self,rsID,organism = 'Human',chromosome=None,
                  position=None,reference=None,genotype=None):
        self.rsID = rsID
        self.organism = organism
        self.chromosome = chromosome
        self.position = position
        self.reference = reference
        self.genotype = genotype
    def displayID(self):
        print 'rsID:',self.rsID
    def displaychromosome(self):
        print 'Chromosome:',self.chromosome
    def displayposition(self):
        print 'Position:',self.position
    def displayref(self):
        print 'Reference sequence:',self.reference
    def displaygenotype(self):
        print 'Genotype:',self.genotype

class Person:
    def __init__(self,ident,first_name,last_name):
        self.ident = ident
        self.first_name = first_name
        self.last_name = last_name

class SnpList:
    pass




#Functions:

#Open dataset

def createdictlist(filename): #Extract SNP data from a 23andme file and store as a list of dicts.

    with open(filename) as dataset:
        listoflines = dataset.readlines()

    SNPlist = []

    for line in listoflines:
        if line[0] != '#': #Unless the line has been commented out.
            linesplit = string.split(line) #Splits strings by whitespace
            currentSNP = {'rsID':linesplit[0],'Chromosome':linesplit[1],
                      'Position':linesplit[2],'Genotype':linesplit[3],'Reference':referencesequence}
            SNPlist.append(currentSNP)
    return SNPlist


'''
Extract SNP data from a 23andme file and store as a list of objects of the SingleNucleotidePolymorphism class.
'''
def createobjectlist(filename):
    with open(filename) as dataset:
        listoflines = dataset.readlines()

    SNPlist = []
    for line in listoflines:
        if line[0] != "#":
            linesplit = string.split(line) #Splits strings by whitespace#Splits string by whitespace
            currentSNP = SingleNucleotidePolymorphism(linesplit[0],chromosome = linesplit[1],position = linesplit[2], genotype = linesplit[3],reference = referencesequence)
            SNPlist.append(currentSNP)
    return SNPlist



def randomsnp(SNPlist):
    '''
    Fetch a random SNP from a SNP list.
    '''
    return

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


def rsIDs(filename): #Extract rsIDs from a file
    with open(filename) as data:
        return data.readlines()
         

def printfile():
    with open(filename) as f:
        for line in f.readlines():
            print line

def filterlist(key,value,SNPlist):
    matches = []
    for SNP in SNPlist:
        if SNP[filteron] == value:
            matches.append(SNP)
    return matches

def returnSNP(rsID,SNPlist): #Fetch an 
    if type(rsID) == int:
        rsID = str(rsID)
    snpfound = False
    for SNP in SNPlist:
        if isinstance(SNP,SingleNucleotidePolymorphism) == True:
            subjectid = SNP.rsID
        else:
            subjectid = SNP['rsID']
        if  subjectid == rsID:
            snpfound = True
            return SNP
    if snpfound == False:
        print 'Could not find entry for rsID %s' % rsID

def showinfo(SNP): #Prints infor for a selected SNP.
    if isinstance(SNP,SingleNucleotidePolymorphism) == True:
        print 'Selected SNP:'
        print 'rsID:',SNP.rsID
        print 'Chromosome:',SNP.chromosome
        print 'Position:',SNP.position
        print 'Genotype:',SNP.genotype
        print 'Reference sequence:',SNP.reference
    else:
        print 'Selected SNP:'
        print 'rsID:',SNP['rsID']
        print 'Chromosome:',SNP['Chromosome']
        print 'Position:',SNP['Position']
        print 'Genotype:',SNP['Genotype']
        print 'Reference sequence:',SNP['Reference']

def listrs(SNPlist): #Retrieve the rsIDs of all the SNPs in a list, and store them in a new list.
    rslist = [entry['rsID'] for entry in SNPlist] #Use this function if SNPs are stored as dicts in SNPlist.
    return rslist

def listrs2(SNPlist):
    rslist = [entry.rsID for entry in SNPlist] #Use this function if SNPs are stored as SingleNucleotidePolymorphism class instances in SNPlist.
    return rslist

def find_union(SNPlist1,SNPlist2):
    #Find SNPs which are in both of two lists
    rslist1 = listrs(SNPlist1)
    rslist2 = listrs(SNPlist2)
    list1set = set(rslist1)
    unionset = list1set.intersection(rslist2)
    return unionset

def comparefiles(file1,file2):
    #Compare two genotypefiles. Return SNPs which are in both files.
    list1 = createdictlist(file1)
    list2 = createdictlist(file2)
    inboth = find_union(list1,list2)
    return inboth

def getdiploids(SNPlist):
    diploids = []
    for SNP in SNPlist:
        if any(x in SNP['Genotype'] for x in bases) & (len(SNP['Genotype']) == 2):
            diploids.append(SNP)
    return diploids

def gethaploids(SNPlist):
    haploids = []
    for SNP in SNPlist:
        if (any(x in SNP['Genotype'] for x in bases)) & (len(SNP['Genotype']) ==1):
            haploids.append(SNP)
    return haploids

def findhomozygotesIDs(SNPlist):
    #Find all homozygous loci
    homozygotes = []
    filteredlist = getdiploids(SNPlist)
    for element in filteredlist:
        if (any(x in element['Genotype'] for x in bases)) & (element['Genotype'][0] == element['Genotype'][1]):
            homozygotes.append(element['rsID'])
    return homozygotes

def getposinlist(rsID,SNPlist): #Get the position, in an SNP list, of a dictionary entry with a given rsID
    for i in range(len(SNPlist)):
        if SNPlist[i]['rsID']== rsID:
            index = i
    return index

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

def find_noncalled(SNPlist):
    #Find all loci with at least one uncalled base
    noncalled = []
    for SNP in SNPlist:
        if ('N' in SNP['Genotype']) or ('n' in SNP['Genotype']):
            noncalled.append(SNP['rsID'])
    return noncalled

def find_called(SNPlist):
    #Find all loci with at least one called base
    called = []
    for SNP in SNPlist:
        if any(x in SNP['Genotype']):
            called.append(SNP['rsID'])
    return called

def find_differing(SNPlist1,SNPlist2):
    #Find SNPs for which the genotype differs between two lists.
    #Pseudocode-ish. Have to fix it up.
    union = find_union(SNPlist1,SNPlist2):
    differing = []
    for SNP in union:
        if SNPlist1[SNP] != SNPlist2[SNP] :
            differing.append(SNP)
    return differing


def find_notinboth(SNPlist1,SNPlist2):
    #Find SNPS which are only in list 1, not in list 2.

    return

def find_genotype(genotype,SNPlist):
    matching = []
    for SNP in SNPlist:
        if SNP['Genotype'] == genotype:
            matching.append(SNP['rsID'])
    return matching

def get_chromosome(chromosomenumber,SNPlist):
    return filterlist('Chromosome',chromosomenumber,SNPlist)
    

def get_byposition(position,SNPlist):
    #Fetch one or more SNPs by their position in the reference sequence.
    snps = []
    for SNP in SNPlist:
        if SNP['Position'] == position:
            snps.append(SNP)
    return snps
    
def get_byrefseq(reference,SNPlist):
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
    #ax.set_title('Figure title')
    fig.autofmt_xdate() #Autorotates the tick labels
    pl.show()
    return counts,left

'''
def chromosomeplot(SNPlist):
    counts = []
'''

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

#mydata = createdictlist('genome_Jarle_Pahr_Full_20110901082829.txt')


#zygosityplot(mydata)


def savelist(rsIDlist,filename): #Write a list of rsIDs to disk.
    out = "\n".join(rsIDlist)
    
    writeout = open(filename, "w+")
    writeout.write(str(out))
    writeout.close()


#Tests:

mylist = createdictlist(filename)

small_list = mylist[0:5]

tiny_list = mylist[0:3]

print 'tinylist:',tiny_list

position = getposinlist('rs3094315',tiny_list)
print 'position:',position
print 'rs:','rs3094315'

smalldata = createobjectlist('Snippet.txt')

exampleSNP = returnSNP('rs3934834',mylist) #Check if the SNP 'rs3934834' is in the list "mylist".
showinfo(exampleSNP)

print findgenotype('GG',tiny_list)

homozygotes = findhomozygotesIDs(small_list)

print 'Homozygotes:',homozygotes

print 'Comparing files:'
print comparefiles('snippet.txt','snippet2.txt')

theunion = find_union(mylist,small_list)
print 'Union:',theunion

print 'Sanitycheck:',sanitycheck(mylist)

noncalled = findnoncalled(mylist)
print 'noncalled:',noncalled

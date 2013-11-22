##############################################################################
#
# Program Name:
#
# buildSNPdict
#
# This program builds up a dictionary of SNPs, where the key is the affy 6.0
# SNP naming format (e.g SNP_A-1234567) and the value is the equivalent
# refSNP cluster ID number (e.g. rs123456).  This dictionary is then pickled
# so it can be used in the affy2RS program, which converts PLINK bim files
# from Affy 6.0 snps ro refSNPs.
#
# Author:
#
# Daniel Williams (Department of Psychiatry, University of Melbourne)
#                 daniel.williams@unimelb.edu.au
#
# Date Created:
#
# 21 November 2013
#
##############################################################################

from cPickle import dump
from csv import reader

#### CONSTANTS ####

# path to the databse that stores the rs and affy 6.0 names
DATA_FILE = "data/GenomeWideSNP_6.na29.annot.csv"

# path to the pickle file that will be created
PICKLE_FILE = "data/affy2rsIndex.pickle"

# character in DATA_FILE that indicates it is a header line / comment
HEADER_TAG = '#'

#### FUNCTIONS ####

def make_index(datafile,picklefile):
    """ create the pickle file storing the affy to rs data """

    # access data and initialise 
    data = open(datafile)
    csvdata = reader(data)
    out = open(picklefile, "wb")
    index = {}

    # skip over header lines
    skipHeaders(csvdata)

    # build index
    for line in csvdata:
        index[line[0]] = line[1]

    # pickle index
    dump(index, out)
    out.close()
    
def skipHeaders(reader):
    """ skip over the header lines in the csv documents so we can access
    the data """

    # skip 'comment' section at header of DATA_FILE
    currentLine = reader.next()
    while (currentLine[0][0] == HEADER_TAG):
        currentLine = reader.next()

def main():
    """ run the program."""
    make_index(DATA_FILE, PICKLE_FILE)

main()

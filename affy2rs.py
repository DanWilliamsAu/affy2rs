##############################################################################
#
# Program Name:
#
# affy2rs
#
# This program takes a PLINK bim file which is encoded with affy 6.0 SNP
# naming format (e.g SNP_A-1234567) and creates a new PLINK bim file with the
# equivalent refSNP cluster ID numbers (e.g. rs123456).  Makes use of a
# pickle file which contains the mapping information.  Pickle file was
# created with the associated program builSNPdict.
# DOES NOT alter the original bim file - it creates a new one
#
# Usage:
#
# $ python affy2rs <bimfilename>
#
# This will create a new bim file with refSNP numbers, with the filename
# as per the OUTFILE_NAME constant below.  This new file should be renamed as
# required.
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

from cPickle import load
from csv import writer
import sys

### CONSTANTS ###


# path to the pickled aff6 6.0 -> rs mapping dictionary index
PKL_FILE = "data/affy2rsIndex.pickle"

# placeholder name for recoded file
OUTFILE_NAME = "RENAMETHISrecodedBimFile"


## FUNCTIONS ###


def open_index(pkl_file):
    """ unpickles the aff6 6.0 -> rs mapping dictionary and retunrs it. """
    return load(open(pkl_file, "rb"))


def get_filename():
    """ checks command line arguments and returns name of
    PLINK bim file which is to be converted
    if supplied or defualt file if not """

    if len(sys.argv) != 2:
        print "please provide a bim file name. Usage:"
        print "python affy2rs.py <filename>"
        sys.exit()
    else:
        return sys.argv[1]


def open_bim(bimFileName):
    """ open and return a file object for the bim file"""
    return open(bimFileName)


def build_RS_bim(bimfile, outWriter, index):
    """ loop through each line of the bimfile in Affy 6.0 format, and output
    the refSNP format to the new output bimfile"""

    for line in bimfile:
        line = line.split()
        line[1] = index[line[1]]
        outWriter.writerow(line)


def main():
    """ run the program."""
    bimfileName = get_filename()
    bimfile = open_bim(bimfileName)
    index = open_index(PKL_FILE)
    out = open(OUTFILE_NAME, "w")
    outWriter = writer(out, delimiter=" ")
    build_RS_bim(bimfile, outWriter, index)


main()

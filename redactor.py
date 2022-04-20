# -*- coding: utf-8 -*-
# Example main.py
import argparse
from project1 import main

def mains(args):
    i=0
    stats ={}
    # Getting the input data
    if args.input:
        print(args.input)
        input_data=main.Read_file(args.input)

    if args.names:
    # Reading names
        input_data, count=main.Redact_names(input_data)
        stats['Redactd Names']=count

    if args.dates:
    # Reading dates
        input_data, count=main.Redact_dates(input_data)
        stats['Redacted Dates']=count

    if args.phones:
    # Reading phone numbers
        input_data, count=main.Redact_phones(input_data)
        stats['Redacted Phone Numbers']=count

    if args.genders:
    # Reading genders
        input_data,count=main.Redact_gender(input_data)
        stats['Redacted Genders']=count

    if args.address:
    # Reading address
        input_data,count=main.Redact_address(input_data)
        stats['Redacted Addresses']=count
    
    if args.concept:
    # Reading concepts
        concount=0
        for i in args.concept:
            input_data,count=main.Redact_concept(input_data, i)
            concount+=count
        stats['Redacted Concepts']=concount

    if args.output:
    # Writing data into a File
        main.write_output(input_data)

    if args.stats:
    # Writing stats into a File
        if args.stats!='stderr' and args.stats!='stdout':
            f = open(args.stats[0],'w')
            print("---Summary of Redaction-----\n",stats, file=f)
        elif args.stats =='stderr':
            print("---Summary of Redaction-----\n",stats, file=sys.stdout)
        elif args.stats =='stdout':
            print("---Summary of Redaction-----\n",stats,  file=sys.stdout)
        

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', action='append', help="Input Files", nargs='*', required=True)
    parser.add_argument('--names', action='store_true', help='Redact_names', required=False) 
    parser.add_argument('--dates', action='store_true', help='Redact_dates', required=False)
    parser.add_argument('--phones', action='store_true', help='Redact_phones', required=False )
    parser.add_argument('--genders', action='store_true', help='Redact_gender', required=False)
    parser.add_argument('--address', action='store_true', help='Redact_address', required=False)
    parser.add_argument('--concept', action='append',  help='Redact_concept', required=True)
    parser.add_argument('--output', help='write_output', required=False)
    parser.add_argument('--stats', action='append', help='write_status', required=True)
    args=parser.parse_args()

    mains(args)

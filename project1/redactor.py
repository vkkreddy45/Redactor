# -*- coding: utf-8 -*-
# Example main.py
import argparse
import project1

def main(args):
    i=0
    # Getting the input data
    if args.input:
        print(args.input)
        input_data=project1.Read_file(args.input)
    
    #print("<---Summary of the Redaction process--->")
    if args.names:
    # Reading names
        input_data, count=project1.Redact_names(input_data)
        #t=sum(count)
        #print("Total Redacted Names: "+str(t))

    if args.dates:
    # Reading dates
        input_data, count=project1.Redact_dates(input_data)
        #t=sum(count)
        #print("Total Redacted Dates: "+str(t))

    if args.phones:
    # Reading phone numbers
        input_data, count=project1.Redact_phones(input_data)
        #t=sum(count)
        #print("Total Redacted Phones: "+str(t))

    if args.genders:
    # Reading genders
        input_data,count=project1.Redact_gender(input_data)
        #t=sum(count)
        #print("Total Redacted Genders: "+str(t))

    if args.address:
    # Reading address
        input_data,count=project1.Redact_address(input_data)
        #t=sum(count)
        #print("Total Redacted Address: "+str(t))

    while(i<10):
        if args.concept:
        # Reading concepts
            input_data,count=project1.Redact_concept(input_data, args.concept)
            #t=sum(count)
        i=i+1
    #print("Total Redacted Concepts: "+str(t))

    if args.output:
    # Writing data into a File
        project1.write_output(input_data)

    if args.stats:
    # Writing stats into a File
        project1.write_stats(input_data,args.stats)
        


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', action='append', help="Input Files", nargs='*', required=True)
    parser.add_argument('--names', action='store_true', help='Redact_names', required=False) 
    parser.add_argument('--dates', action='store_true', help='Redact_dates', required=False)
    parser.add_argument('--phones', action='store_true', help='Redact_phones', required=False )
    parser.add_argument('--genders', action='store_true', help='Redact_gender', required=False)
    parser.add_argument('--address', action='store_true', help='Redact_address', required=False)
    parser.add_argument('--concept', help='Redact_concept', required=True)
    parser.add_argument('--output', help='write_output', required=False)
    parser.add_argument('--stats', action='append', help='write_status', required=True)
    args=parser.parse_args()

    main(args)

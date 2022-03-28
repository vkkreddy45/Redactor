# -*- coding: utf-8 -*-
# Example main.py
import argparse

import project1

def main(args):
    # Getting the Input
    if args.input:
        input_data = project1.Read_file(args.input)

    if args.names:
    # Reading names
        project1.Redact_names(input_data)
    
    if args.dates:
    # 
        project1.Redact_dates(input_data)
    
    if args.phones:
    #
        project1.Redact_phones(input_data)
    
    if args.gender:
    # 
        project1.Redact_gender(input_data)

    if args.address:
    #
        project1.Redact_address(input_data)

    if args.concept:
    #
        project1.Redact_concept(input_data, args.concept)

    if args.output:
    #
        project1.write_output(input_data)

    # if args.stats:
    # #
    #     project1.write_stats(input_data)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help="Input Files", nargs='*')
    parser.add_argument('--names', required=False, help='Redact_names') 
    parser.add_argument('--dates', required=False, help='Redact_dates')
    parser.add_argument('--phones', required=False, help='Redact_phones')
    parser.add_argument('--genders', required=False, help='Redact_gender')
    parser.add_argument('--address', required=False, help='Redact_address')
    parser.add_argument('--concept', required=True, help='Redact_concept')
    parser.add_argument('--output', required=True, help='write_output')
    #parser.add_argument('--stats', required=True, help='write_status')
    args = parser.parse_args()

    main(args)

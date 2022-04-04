# -*- coding: utf-8 -*-
# Example main.py
import argparse

import project1

def main(args):
    # Getting the Input
    if args.input:
        print(args.input)
        input_data = project1.Read_file(args.input)

    if args.names:
    # Reading names
        input_data, count=project1.Redact_names(input_data)
    
    if args.dates:
    # 
        input_data, count=project1.Redact_dates(input_data)
    
    if args.phones:
    #
        input_data, count=project1.Redact_phones(input_data)
    
    if args.genders:
    # 
        input_data,count=project1.Redact_gender(input_data)

    if args.address:
    #
        input_data,count=project1.Redact_address(input_data)

    if args.concept:
    #
        input_data,count=project1.Redact_concept(input_data, args.concept)

    if args.output:
    #
        project1.write_output(input_data)

    if args.stats:
    # #
        project1.write_stats(input_data)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help="Input Files", nargs='*', action='append')
    parser.add_argument('--names', required=False, help='Redact_names', action='store_true') 
    parser.add_argument('--dates', required=False, help='Redact_dates', action='store_true')
    parser.add_argument('--phones', required=False, help='Redact_phones', action='store_true')
    parser.add_argument('--genders', required=False, help='Redact_gender', action='store_true')
    parser.add_argument('--address', required=False, help='Redact_address', action='store_true')
    parser.add_argument('--concept', help='Redact_concept')
    parser.add_argument('--output', help='write_output')
    parser.add_argument('--stats', required=False, help='write_status')
    args = parser.parse_args()

    main(args)

# Changes 
* Wrong redaction character or amount --- I changed the redaction characters to the Unicode block '\u2588' instead of a other unicodes.
* Gender Function --- I corrected the code to get the count of genders.
* Date Function --- I have corrected the code to get the count of Dates.
* Redact_concept() --- I have changed the function from lambda to a for loop to count the concepts.
* write_output() --- I changed the .redacted.txt to .redacted extension. I have also changed the hard coded directory name where it takes the output flag passed directory name and stores the redacted files in the passed directory.
* args.stats --- I have modified the three cases for name of a file or special files (stderr, stdout).
* Files Structure --- I have modified the file structure.

# cs5293sp22-project1

### Text Analytics Project 1
### Author: Vudumula Kranthi Kumar Reddy

# About

In this Project the main goal is to read the inputed text files and Pass the file for the Redaction Process. Generally, we hide the important information that is present in the text file with any unicode characters. Concepts that I have used for this project are text analytics and Knowledge of python. 


### Table of Contents

**[Required Packages](#required-packages)**<br>
**[Function Description](#function-description)**<br>
**[How to run the project](#how-to-run-the-project)**<br>
**[How to run the test cases](#how-to-run-the-test-cases)**<br>
**[Bugs](#bugs)**<br>


# Required Packages

The below mentioned are the packages used for this Project:
* glob
* itertools
* nltk
* os
* regex
* spacy


# Function Description

1. project1.py: 

     This file contains all the functions that will be used for the redaction process and writing the summary of the redaction process.
     

2. redactor.py:

     This is the main function were the argument parsing is done. 

    a. Read_file(path): 

        In this Function, we read the text files that are being passed with '*.txt' extension.

    b. Redact_names(idata):

        In this Function, we redact the names that are present in the passes text file.

    c. Redact_gender(idata):

        In this Function, we redact the genders that reveals the gender of an entity like he, she, him, father, .... etc.

    d. Redact_dates(idata):

        In this Function, we redact all the dates that are present in the text file written in the form of 2/4/1990, January 10th, .... etc.

    e. Redact_phone(idata):

        In this Function, we redact all the phone numbers present in the text file written in the form of +14055413246, 04055647329, 405-234-3455, .... etc.

    f. Redact_address(idata):

        In this Function, we redact all the addresses that are present in the file like any physical address.

    g. Redact_concept(idata):

        In this Function, we redact all the values or strings that refer to the concept gets redacted. Here, we redacting all the different synonyms that refer to the passed concept. To get the synonyms I have used some of the concepts like synsets, lemmas, hypernyms, hyponyms, .... etc.

    h. write_output(idata):

        In this Function, we initially create a directory. Then we create a file with "*.redacted.txt" and write the redacted data into the newly created text file.

    i. write_stats(idata):

        In this Function, we intially create a directory. Then we create a file and write the summary of the redaction process by displaying the number of redactions done for each of the redactions funtions mentioned above.
        
   
3. test_data.py:

     This file contains all the test cases for the above mentioned functions, to check whether the redaction process is running correctly or not.
    
    a. test_readfile():
     
        In this Function, I am trying to check whether the inputed file is being passed or None.
     
    b. test_redactname():
  
        In this Function, I am trying to check whether the inputed count of name is not None and count is equal to 2.
    
    c. test_redactgender():
  
        In this Function, I am trying to check whether the inputed count of genders is not None and and the count is greater than 4.
     
    d. test_redactdates():
  
        In this Function, I am trying to check whether the inputed count of dates is not None and the count is equal to 1.
     
    e. test_redactphones():
  
        In this Function, I am trying to check whether the inputed count of phones is not None and the count is equal to 1.
     
    f. test_redactaddress():
  
        In this Function, I am trying to check whether the inputed count of address is not None.
     
    g. test_redactconcept():
  
        In this Function, I am trying to check whether the inputed count of concept is not equal to 0.
        
        
* test1.txt & test2.txt:

      These are the text files where the content to be redacted is stored.
    
* test1.redacted.txt & test2.redacted.txt:

      These are the text files where the redacted text is present.
    
* stderr.txt & stdout.txt:

      These are the text files where the Summary of the redacted text is stored.
      
* pytest.ini:

      Aditionally, I have created a **pytest.ini** file and added some code to eliminate some of the warnings that are being displayed while running the test cases.


# How to run the project

```
pipenv run python project1/redactor.py --input '*.txt' --names --dates --phones --genders --address --concept 'person' --output 'files/' --stats stderr
```
or

```
pipenv run python project1/redactor.py --input '*.txt' --names --dates --phones --genders --address --concept 'person' --output 'files/' --stats stdout
```
or

```
pipenv run python project1/redactor.py --input '*.txt' --names --dates --phones --genders --address --concept 'person' --concepts'kids' --output 'files/' --stats stderr
```


# How to run the test cases

```
pipenv run python -m pytest
```


# Bugs

* One might face problem, For the address function as it only works for few expressions but not for all the address expressions.

# cs5293sp22-project1

### Text Analytics Project 1
### Author: Vudumula Kranthi Kumar Reddy

# About

In this Project the main goal is to read the inputed text files and Pass the file for the Redaction Process. Generally, we hide the important information that is present in the text file with any unicode characters. Concepts that I have used for this project are text analytics and Knowledge of python. 

# Required Packages

The below mentioned are the packages used for this Project:
* glob
* itertools
* nltk
* os
* regex
* spacy

# Function Description

1. Read_file(path): 

In this Function, we read the text files that are being passed with '*.txt' extension.

2. Redact_names(idata):

In this Function, we redact the names that are present in the passes text file.

3. Redact_gender(idata):

In this Function, we redact the genders that reveals the gender of an entity like he, she, him, father, .... etc.

4. Redact_dates(idata):

In this Function, we redact all the dates that are present in the text file written in the form of 2/4/1990, January 10th, .... etc.

5. Redact_phone(idata):

In this Function, we redact all the phone numbers present in the text file written in the form of +14055413246, 04055647329, 405-234-3455, .... etc.

6. Redact_address(idata):

In this Function, we redact all the addresses that are present in the file like any physical address.

7. Redact_concept(idata):

In this Function, we redact all the values or strings that refer to the concept gets redacted. Here, we redacting all the different synonyms that refer to the passed concept. To get the synonyms I have used some of the concepts like synsets, lemmas, hypernyms, hyponyms, .... etc.

8. write_output(idata):

In this Function, we initially create a directory. Then we create a file with "*.redacted.txt" and write the redacted data into the newly created text file.

9. write_stats(idata):

In this Function, we intially create a directory. Then we create a file and write the summary of the redaction process by displaying the number of redactions done for each of the redactions funtions mentioned above.

# How to run the project

```
pipenv run python project1/main.py --input '*.txt' --names --dates --phones --genders --address --concept 'person' --output 'files/' --stats stderr
```

# How to run the test cases

```
pipenv run python -m pytest
```

# Bugs

* One might face problem, For the address function as it only works for few expressions but not for all the address expressions.

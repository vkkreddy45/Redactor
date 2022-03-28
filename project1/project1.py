import spacy 
import nltk
#nltk.download("wordnet")
#nltk.download("omw-1.4")
import glob
from itertools import chain
import regex as re
from nltk.corpus import wordnet
import os

nlp = spacy.load("en_core_web_sm")
input_files=[]

# Function for Getting the input data from Glob

def Read_file(path):
    idata = []
    files = list(chain.from_iterable(path))

    for i in range(len(files)):
        finput = glob.glob(files[i])
        for j in range(len(finput)):
            dat = open(finput[j]).read()
            idata.append(dat)
            input_files.append(finput[j])
    return idata

def redact_names_with(token):
    if token.ent_iob != 0 and token.ent_type_ == 'PERSON':
        return '\u2588 '
    return str(token)

def redact_names(nlp_doc):
    # for ent in nlp_doc:
    #     print(ent, ent.ent_type_)
    tokens = map(redact_names_with, nlp_doc)
    return ' '.join(tokens)

# Function for Reading Names

def Redact_names(idata):
    tdata=[]
    for text in idata:
        doc = nlp(text)
        tdata.append(redact_names(doc))
    #print(tdata)
    return tdata

# Fuction for Genders
def Redact_gender(idata):
    tdata=[]
    # Pronous for genders
    gender=['he','she','him','her','his','hers','male','female','man','woman','men','women','He','She','Him','Her','His','Hers','Male','Female','Man','Woman','Men','Women','HE','SHE','HIM','HER','HIS','HERS','MALE','FEMALE','MAN','WOMAN','MEN','WOMEN']
    for i in idata:
        doc = nlp(i)
        temp = []
        for x in doc:
            test = lambda x : '\u2588' if str(x) in gender else x
            temp.append(test(x))
        tdata.append(" ".join([str(x) for x in temp]))
    #print(tdata)
    return tdata

# Function for Reading dates

def Redact_dates(idata):
    tdata=[]
    for i in idata:
        doc = nlp(i)
        dlist = []
        for x in doc:
            if x.ent_type_=='DATE' or x.ent_type_=='CARDINAL':
                dlist.append(x)
        dlist = set(dlist)
        temp = []
        for t in doc:
            test = lambda z : '\u2588' if z in dlist else z
            temp.append(test(t))
        tdata.append(" ".join([str(x) for x in temp]))
    #print(tdata)
    return tdata
# Function for Reading Phones

def Redact_phones(idata):
    #print(idata)
    tdata = []
    for i,text in enumerate(idata):
        ri = r'\d{3}\s*[ - \.\s]\s*\d{3}\s*[ - \.\s]\s*\d{4}|\(\d{3}\)\s*\d{3}\s*[ - \.\s]\d{4}|\d{3}[ - \.\s]\d{4}'
        result = re.findall(ri,text)
        ph = re.compile('''((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-])))''')
        tr = ph.findall(text)
        #print(tr)
        ts = ""
        for g in tr:
            for k in g:
                ts = ts + k
        #print(ts)
        result = result + list(ts)
        #print(result)
        for k in result:
            text = text.replace(k,'\u2588')
        idata[i] = text
        tdata.append(text)
    #print(tdata)
    return tdata

def Replace(char):
    if char =='\n':
        char = ""
    return char

# Function for Reading address

def Redact_address(idata):
    #print(idata)
    #idata = list(filter(Replace,idata))
    tdata=[]
    #nlp1=spacy.load("C:/Users/Admin/Desktop/address-parser-main/address-parser-main/output/models/model-best")
    for i,text in enumerate(idata):
        text = re.sub(r'\n', '', text)
        addr = re.compile('\d{1,4} [\w\s]{1,20}(?:main|street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|parkwood|pkwy|circle|cir|boulevard|blvd|Blvd)\W?(?=\s|$) | \b\d{5}(?:[-\s]\d{4})?\b', re.IGNORECASE)
        temp_addr = addr.findall(text)
        print(temp_addr)
        for k in temp_addr:
            text = text.replace(k,'\u2588')
        idata[i] = text
        tdata.append(text)
    #print(tdata)
    return tdata

# Function for Reading concept

def Redact_concept(idata, concept):
    tdata = []
    syn = wordnet.synsets(concept)
    synonyms = []
    #print(syn)
    for i in syn:
        for l in i.lemmas():
            synonyms.append(l.name())
        for hyper in i.hypernyms():
            synonyms.append(hyper.name())
        for hypo in i.hyponyms():
            synonyms.append(hypo.name())
    #print(synonyms)
    for i in idata:
        doc = nlp(i)
        temp = []
        for t in doc:
            test = lambda z : '\u2588' if str(t) in synonyms else z
            temp.append(test(t))
        tdata.append(" ".join([str(x) for x in temp]))
    return tdata

def write_output(idata):
    outputfiles=[]
    for i in input_files:
        newname = os.path.splitext(i)[0]
        newname = newname +'.redacted.txt'
        outputfiles.append(newname)
    print(outputfiles)

    # Parent Directory path
    parent_dir = str(os.getcwd())
    # Path
    path = os.path.join(parent_dir, "files")
    try:
        os.mkdir(path)
    except:
        print("Directory Exists")

    for i in range(len(outputfiles)):
        despath = str(os.getcwd())+"/files/"+outputfiles[i]
        with open(despath, 'w+' , encoding='utf-8') as file:
            file.write(idata[i])
            file.close()

def write_status():
    pass

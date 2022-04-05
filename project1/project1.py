import glob 
from itertools import chain
import nltk
from nltk.corpus import wordnet
#nltk.download("wordnet")
#nltk.download("omw-1.4")
import os
import regex as re
import spacy

nlp=spacy.load("en_core_web_sm")
input_files=[]

# Function for getting data from glob

def Read_file(path):
    idata=[]
    files=list(chain.from_iterable(path))

    for i in range(len(files)):
        finput=glob.glob(files[i])
        for j in range(len(finput)):
            dat=open(finput[j]).read()
            idata.append(dat)
            #print(idata)
            input_files.append(finput[j])
    return idata

def redact_names_with(token):
    if token.ent_iob!=0 and token.ent_type_=='PERSON':
        return '\u2588'
    return str(token)

def redact_names(nlp_doc):
    tokens=map(redact_names_with, nlp_doc)
    return ' '.join(tokens)

# Function for Reading Names

def Redact_names(idata):
    tdata=[]
    for text in idata:
        doc=nlp(text)
        tdata.append(redact_names(doc))
    #print(tdata)
    ncount=tdata[0].count('\u2588')
    #print(tdata,ncount)
    return tdata,ncount

# Fuction for Reading Genders

def Redact_gender(idata):
    tdata=[]
    # Pronous for genders
    gender=['female','man','woman','men','he','she','him','her','his','hers','male','women','He','She','Him','Her','His','Hers','Male','Female','Man','Woman','Men','Women','HE','SHE','HIM','HER','HIS','HERS','MALE','FEMALE','MAN','WOMAN','MEN','WOMEN']
    for i in idata:
        doc=nlp(i)
        temp=[]
        for x in doc:
            test=lambda x:'\u2589' if str(x) in gender else x
            temp.append(test(x))
        tdata.append(" ".join([str(x) for x in temp]))
    gcount=tdata[0].count('\u2589')
    #print(tdata,gcount)
    return tdata,gcount

# Function for Reading dates

def Redact_dates(idata):
    tdata=[]
    for i in idata:
        doc=nlp(i)
        dlist=[]
        for x in doc:
            if x.ent_type_=='DATE' or x.ent_type_=='CARDINAL':
                dlist.append(x)
        dlist=set(dlist)
        temp=[]
        for t in doc:
            test=lambda z:'\u2587' if z in dlist else z
            temp.append(test(t))
        tdata.append(" ".join([str(x) for x in temp]))
    dcount=tdata[0].count('\u2587')
    #print(tdata,dcount)
    return tdata,dcount

# Function for Reading Phones numbers

def Redact_phones(idata):
    tdata=[]
    for i,text in enumerate(idata):
        ri=r'\d{3}\s*[ - \.\s]\s*\d{3}\s*[ - \.\s]\s*\d{4}|\(\d{3}\)\s*\d{3}\s*[ - \.\s]\d{4}|\d{3}[ - \.\s]\d{4}'
        result=re.findall(ri,text)
        ph=re.compile('''((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-])))''')
        tr=ph.findall(text)
        #print(tr)
        ts = ""
        for g in tr:
            for k in g:
                ts=ts + k
        #print(ts)
        result=result + list(ts)
        #print(result)
        for k in result:
            text=text.replace(k,'\u2586')
        idata[i]=text
        tdata.append(text)
    #print(tdata)
    pcount=tdata[0].count('\u2586')
    #print(tdata,pcount)
    return tdata,pcount

def Replace(char):
    if char=='\n':
        char=""
    return char

# Function for Reading address

def Redact_address(idata):
    #print(idata)
    tdata=[]
    for i,text in enumerate(idata):
        text=re.sub(r'\n', '', text)
        addr=re.compile('\d{1,4} [\w\s]{1,20}(?:main|street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|parkwood|pkwy|circle|cir|boulevard|blvd|Blvd)\W?(?=\s|$) | \b\d{5}(?:[-\s]\d{4})?\b', re.IGNORECASE)
        temp_addr=addr.findall(text)
        #print(temp_addr)
        for k in temp_addr:
            text=text.replace(k,'\u2585')
        idata[i]=text
        tdata.append(text)
    #print(tdata)
    acount=tdata[0].count('\u2585')
    #print(tdata,acount)
    return tdata,acount

# Function for Reading concept

def Redact_concept(idata, concept):
    tdata=[]
    syn=wordnet.synsets(concept)
    synonyms=[]
    for i in syn:
        for l in i.lemmas():
            synonyms.append(l.name())
        for hyper in i.hypernyms():
            synonyms.append(hyper.name())
        for hypo in i.hyponyms():
            synonyms.append(hypo.name())
    for i in idata:
        doc=nlp(i)
        temp=[]
        for t in doc:
            test=lambda z:'\u2584' if str(t) in synonyms else z
            temp.append(test(t))
        tdata.append(" ".join([str(x) for x in temp]))
    ccount=tdata[0].count('\u2584')
    #print(tdata,ccount)
    return tdata,ccount

# Function for Writing Output to the Files

def write_output(idata):
    outputfiles=[]
    for i in input_files:
        newname=os.path.splitext(i)[0]
        newname=newname +'.redacted.txt'
        outputfiles.append(newname)
    #print(outputfiles)

    # Parent Directory path
    parent_dir=str(os.getcwd())
    # Path
    path=os.path.join(parent_dir,"files")
    try:
        os.mkdir(path)
    except:
        print("Directory Exists")

    for i in range(len(outputfiles)):
        despath=str(os.getcwd())+"/files/"+outputfiles[i]
        with open(despath, 'w+' , encoding='utf-8') as file:
            file.write(idata[i])
            file.close()

# Function writing the stats into File

def write_stats(idata,fname):    
    cnt_names, cnt_gender, cnt_dates, cnt_address, cnt_phones, cnt_concept=[], [], [], [], [], []
    #print(fname)
    fname=fname[0]
    for t in idata:
        cnt_names.append(t.count('\u2588'))
        cnt_gender.append(t.count('\u2589'))
        cnt_dates.append(t.count('\u2587'))
        cnt_address.append(t.count('\u2585'))
        cnt_phones.append(t.count('\u2586'))
        cnt_concept.append(t.count('\u2584'))
    #print(cnt_names,cnt_gender,cnt_dates,cnt_phones,cnt_address,cnt_concept)

    # Parent Directory path
    parent_dir=str(os.getcwd())
    # Path
    path=os.path.join(parent_dir, fname)
    try:
        os.mkdir(path)
    except:
        print("Directory Exists")
    
    despath=str(os.getcwd())+"/"+fname+"/"+fname+".txt"
    with open(despath, 'w+' , encoding='utf-8') as file:
        file.write("***Summary of the Redaction Process***"+"\n")
        file.write("Names: "+str(sum(cnt_names))+"\n")
        file.write("Dates: "+str(sum(cnt_dates))+"\n")
        file.write("Phones Numbers: "+str(sum(cnt_phones))+"\n")
        file.write("Genders: "+str(sum(cnt_gender))+"\n")
        file.write("Address: "+str(sum(cnt_address))+"\n")
        file.write("Concepts: "+str(sum(cnt_concept)))
        file.close()

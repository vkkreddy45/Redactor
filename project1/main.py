import glob 
from itertools import chain
import nltk
from nltk.corpus import wordnet
#nltk.download("wordnet")
#nltk.download("omw-1.4")
import os
import regex as re
import spacy
import sys

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
    print('namecount: ', ncount)
    return tdata,ncount

# Fuction for Reading Genders

def Redact_gender(idata):
    tdata=[]
    gcount=0
    # Pronous for genders
    gender=['female','man','woman','men','he','she','him','her','his','hers','male','women','He','She','Him','Her','His','Hers','Male','Female','Man','Woman','Men','Women','HE','SHE','HIM','HER','HIS','HERS','MALE','FEMALE','MAN','WOMAN','MEN','WOMEN']
    for i in idata:
        doc=nlp(i)
        temp=[]
        for x in doc:
            if str(x) in gender:
                x='\u2588'
                gcount+=1
            #test=lambda x:'\u2587' if str(x) in gender else x
            #gcount = gcount+sum(map(lambda x: x=='\u2587', str(x)))
            #test=lambda x:'\u2588' if str(x)=='\u2587' else x
            temp.append(x)
        tdata.append(" ".join([str(x) for x in temp]))
    print('gendercount:', gcount)
    #gcount=tdata[0].count('\u2589')
    #print(tdata,gcount)
    return tdata,gcount

# Function for Reading dates

def Redact_dates(idata):
    tdata=[]
    dcount=0
    for i in idata:
        doc=nlp(i)
        dlist=[]
        for x in doc:
            if x.ent_type_=='DATE' or x.ent_type_=='CARDINAL':
                dlist.append(x)
        dlist=set(dlist)
        temp=[]
        for t in doc:
            if t in dlist:
                t='\u2588'
                dcount+=1
            #test=lambda z:'\u2586' if z in dlist else z
            #dcount = dcount+sum(map(lambda x: x=='\u2586', str(x)))
            #test=lambda x:'\u2588' if str(x)=='\u2586' else x
            temp.append(t)
        tdata.append(" ".join([str(x) for x in temp]))
    print('date count: ',dcount)
    #dcount=tdata[0].count('\u2587')
    #print(tdata,dcount)
    return tdata,dcount

# Function for Reading Phones numbers

def Redact_phones(idata):
    tdata=[]
    pcount=0
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
            pcount+=1
            text=text.replace(k,'\u2588')
        idata[i]=text
        tdata.append(text)
    #print(tdata)
    #pcount=tdata[0].count('\u2588')
    print('phone count: ',pcount)
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
    acount=0
    for i,text in enumerate(idata):
        text=re.sub(r'\n', '', text)
        addr=re.compile('\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Norman|norman|oklahoma|classen|Street|Ave|Dr|Rd|Blvd|blvd|Ln|St|)\.?', re.IGNORECASE)
        temp_addr=addr.findall(text)
        #print(temp_addr)
        for k in temp_addr:
            acount+=1
            text=text.replace(k,'\u2588')
        idata[i]=text
        tdata.append(text)
    #print(tdata)
    #acount=tdata[0].count('\u2588')
    print('address count: ',acount)
    #print(tdata,acount)
    return tdata,acount

# Function for Reading concept

def Redact_concept(idata, concept):
    tdata=[]
    syn=wordnet.synsets(concept)
    ccount=0
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
            if str(t) in synonyms:
                t='\u2588'
                ccount+=1
            #test=lambda z:'\u2582' if str(t) in synonyms else z
            #ccount = ccount+sum(map(lambda t: t=='\u2582', str(t)))
            #test=lambda x:'\u2588' if str(x)=='\u2582' else x
            temp.append(t)
        tdata.append(" ".join([str(x) for x in temp]))
    #ccount=tdata[0].count('\u2588')
    print('Concept Count: ', ccount)
    #print('concept count: ',ccount)
    #print(tdata,ccount)
    return tdata,ccount

# Function for Writing Output to the Files

def write_output(idata,directory):
    outputfiles=[]
    for i in input_files:
        newname=i
        newname=newname +'.redacted'
        outputfiles.append(newname)
    #print(outputfiles)

    # Parent Directory path
    parent_dir=str(os.getcwd())
    # Path
    path=os.path.join(parent_dir,directory)
    try:
        os.mkdir(path)
    except:
        print("Directory Exists")

    for i in range(len(outputfiles)):
        despath=str(os.getcwd())+"/"+directory+"/"+outputfiles[i]
        with open(despath, 'w+' , encoding='utf-8') as file:
            file.write(idata[i])
            file.close()

from project1 import project1
import pytest

filename = ["*.txt"]

def test_readfile():
    result = project1.Read_file([filename]) 
    assert result is not None

def test_redactname():
    result,count = project1.Redact_names(["Vijay Kumar"])
    assert len(result) is not None and count==2

def test_redactgender():
    result,count = project1.Redact_gender(["he,she,him,her,his,hers,male,female"])
    assert len(result) is not None and count>=4

def test_redactdates():
    result,count = project1.Redact_dates(["11/17/00"])
    assert len(result) is not None and count==1

def test_redactphones():
    result,count = project1.Redact_phones(["09824066305"])
    assert len(result) is not None and count==len(result[0])

def test_redactaddress():
    result,count = project1.Redact_address(["2657 Classen blvd"])
    assert len(result) is not None

def test_redactconcept():
    result,count = project1.Redact_concept(["kids,child,small"],"kids")
    assert len(result)!=0

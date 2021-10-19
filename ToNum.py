# Python3 code to demonstrate
# getting numbers from string 
# using re.findall()
import re
  
def To_Num(text):
    # using re.findall()
    # getting numbers from string 
    temp = re.findall(r'\d+\.?\d*', text)
    res = list(map(float, temp))
    
    # print result
    return res[0]

def To_Storage(text):
        # using re.findall()
    # getting numbers from string 
    temp = text.split(' ')
    
    # print result
    return temp[0]



def To_Date(text):

    regex = re.compile(
        '(?=((?:(?:[0][1-9]|[1-2][0-9]|3[0-1]|[1-9])[/\-,.]?(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[/\-,.]?(?:19|20)?\d{2}(?!\:)|'
        '(?:19|20)?\d{2}[/\-,.]?(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[/\-,.]?(?:[0][1-9]|[1-2][0-9]|3[0-1]|[1-9])|'
        '(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[/\-,.]?(?:[0][1-9]|[1-2][0-9]|3[0-1]|[1-9])[/\-,.]?(?:19|20)\d{2}(?!\:)|'
        '(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[/\-,.]?(?:[0][1-9]|[1-2][0-9]|3[0-1]|[1-9])[/\-,.]?\d{2})))'
    )

    return(sum([regex.findall(x) for x in text],[]))
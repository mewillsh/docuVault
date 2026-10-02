import pymupdf 
import re
def pdf_extractor(file:bytes)->str:
    doc  = pymupdf.open(stream=file,filetype="pdf")
    text = ""
    for page in doc:
        curr = re.sub(r'\s+', ' ',page.get_text()).strip()
        text += curr
    return text

def text_extractor(file:bytes)->str:
    return file.decode("utf-8")
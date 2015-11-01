from config import currentPacket
from PyPDF2 import PdfFileReader

def questionParser():
    inputFile = PdfFileReader(open(currentPacket, "rb"))
    return str(inputFile.getPage(1).extractText())

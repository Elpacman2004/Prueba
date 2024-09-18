import comtypes.client
import pythoncom
import os

def convert_word_to_pdf(doc_path, pdf_path):
    print(f"Converting Word file {doc_path} to PDF file {pdf_path}")

    wdFormatPDF = 17

    try:
        pythoncom.CoInitialize()
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(doc_path)
        doc.SaveAs(pdf_path, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
    except Exception as e:
        print(f"Error converting Word to PDF: {e}")
    finally:
        pythoncom.CoUninitialize()
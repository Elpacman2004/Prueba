import win32com.client

def convert_word_to_pdf(doc_path, pdf_path):
    try:
        word = win32com.client.Dispatch('Word.Application')
        doc = word.Documents.Open(doc_path)
        doc.SaveAs(pdf_path, FileFormat=17)  # 17 represents the PDF format in Word
        doc.Close()
        word.Quit()
    except Exception as e:
        print(f"Error converting Word to PDF: {e}")
        return False

import PyPDF2

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

def extract_resume_data(filename):
    data = {}
    
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text = page.extract_text()
            
            # Extract the necessary fields from the text and populate the data dictionary
            
    return data

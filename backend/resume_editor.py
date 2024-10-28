from resume_parser import ResumeParser
from resume_builder import Resume, ResumeSection, ResumeSubheading, resumeInfo
from baml_client import b
from constants import DUMMY_RESUME_DICT_1

def edit_resume():
    parser = ResumeParser()
    pdf_path = "/Users/ronald/Documents/GitHub/resume-builder/backend/output/input1.pdf"
    text = parser.extract_text_from_pdf(pdf_path)
    # testing the resume
    # resume = Resume(DUMMY_RESUME_DICT_1)
    # resume.generate_pdf("yay1")
    
    # print("extracted resume")
    extracted = b.ExtractResume(text)
    print(extracted)
    print("we managed to get the extracted resume as follows")
    resume = Resume(extracted)
    resume.generate_pdf("yay1")

edit_resume()


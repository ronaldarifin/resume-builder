import sys
import os
import app
from resume_builder.resume_parser import ResumeParser
from resume_builder.resume_builder import Resume, ResumeSection, ResumeSubheading, resumeInfo
from baml_client import b
from constants.constants import DUMMY_RESUME_1

def edit_resume():
    parser = ResumeParser()
    pdf_path = "/Users/ronald/Documents/GitHub/resume-builder/backend/output/input1.pdf"
    text = parser.extract_text_from_pdf(pdf_path)
    extracted = b.ExtractResume(text)
    resume = Resume(extracted)
    print(resume)
    print("going to print yay but cannot")
    resume.generate_pdf("yay1")


if __name__ == "__main__":
    edit_resume()


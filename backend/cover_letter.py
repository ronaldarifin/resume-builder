import app
from resume_parser import ResumeParser
from baml_client import b
from perplexity import PerplexityAPI
from constants import DUMMY_RESUME_DICT_1

# Takes in Resume Object and 
# class Cover_Letter():


def get_extracted_resume(pdf_path, simple):
    parser = ResumeParser()
    text = parser.extract_text_from_pdf(pdf_path)
    if simple:
        extracted = b.ExtractResumeSimple(text)
    else:
        extracted = b.ExtractResume(text)
    return extracted



pdf_path = "/Users/ronald/Documents/GitHub/resume-builder/backend/output/input1.pdf"
resume = get_extracted_resume(pdf_path, True)
company_name = "Doordash"
values = ["Real-World Impact", "Strong CS Fundamentals", "Agile"]
culture = PerplexityAPI().simple_completion(f"What is the mission and values of {company_name}")
cover_letter = b.GenerateCoverLetter(resume, culture, company_name, ",".join(values))
print(cover_letter)

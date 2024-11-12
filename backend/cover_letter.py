import app
from resume_parser import ResumeParser
from baml_client import b
from datetime import date
from perplexity import PerplexityAPI
from constants import DUMMY_RESUME_DICT_1
import os

class CoverLetter:
    def __init__(self, pdf_path=None):
        self.pdf_path = pdf_path
        self.parser = ResumeParser()
        
    def get_extracted_resume(self, simple=True):
        """Extract and parse resume from PDF"""
        text = self.parser.extract_text_from_pdf(self.pdf_path)
        if simple:
            extracted = b.ExtractResumeSimple(text)
        else:
            extracted = b.ExtractResume(text)
        return extracted
    
    def get_company_culture(self, company_name):
        """Get company mission and values using Perplexity API"""
        return PerplexityAPI().simple_completion(f"What is the mission and values of {company_name}. Also include the address, city, state, and zip of the {company_name}")
    
    def generate(self, company_name, values, user_info, simple=True):
        """Generate cover letter based on resume and company info"""
        resume = self.get_extracted_resume(simple)
        culture = self.get_company_culture(company_name)
        return b.GenerateCoverLetter(resume, culture, company_name, ",".join(values), user_info)

class CoverLetterPDFGenerator:
    def __init__(self, result):
        self.user_info = result.user_info
        self.letter = result.letter
    
    def generate_pdf(self, path_direction):
        """Generate PDF from cover letter content and user info"""
        from fpdf import FPDF
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(path_direction), exist_ok=True)
        
        # Add .pdf extension if not present
        if not path_direction.endswith('.pdf'):
            path_direction += '.pdf'
        
        # Create PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        # Use Arial
        pdf.set_font('Arial', size=12)
        
        # Clean the text by replacing problematic characters
        clean_letter = (self.letter
            .replace('—', '-')  # Replace em dash
            .replace('"', '"')  # Replace smart quotes
            .replace('"', '"')  # Replace smart quotes
            .encode('latin-1', 'replace').decode('latin-1'))  # Handle other special chars
        
        # Add user info header
        pdf.cell(0, 5, self.user_info.name, ln=True)
        pdf.cell(0, 5, self.user_info.address, ln=True)
        pdf.cell(0, 5, f"{self.user_info.city}, {self.user_info.state} {self.user_info.zip}", ln=True)
        pdf.cell(0, 5, self.user_info.phone, ln=True)
        pdf.cell(0, 5, self.user_info.date, ln=True)
        
        # Add spacing
        pdf.cell(0, 5, "", ln=True)
        
        # Add letter content using the cleaned text
        for paragraph in clean_letter.split('\n'):
            pdf.multi_cell(0, 5, paragraph)
            pdf.cell(0, 5, "", ln=True)  # Add spacing between paragraphs
            
        # Save PDF
        pdf.output(path_direction)


# Example usage:
if __name__ == "__main__":
    # pdf_path = "/Users/ronald/Documents/GitHub/resume-builder/backend/output/input1.pdf"
    # cover_letter = CoverLetter(pdf_path)
    # company_name = "Amazon"
    # values = ["Real-World Impact", "Strong CS Fundamentals", "Start Up Experience"]
    # user_info = f"Ronald Arifin stays at 1988 Martin Luther King Jr. Way, Berkeley, California, 94704, +15104786156, {datetime.now().date()}"
    # result = cover_letter.generate(company_name, values, user_info)
    
    # create dummy class here:
    letter_string = """Dear Amazon Hiring Manager,

I am writing to express my strong interest in a Software Engineering role at Amazon, motivated by the company's mission to innovate and deliver unmatched customer experiences. My academic and professional background aligns with Amazon's core principles—particularly Customer Obsession, Invent and Simplify, and Delivering Results—which are paramount to fulfilling the company's mission.

Firstly, my experiences as a Software Engineer Intern at HrHouz and as a Software Engineer at Skygeni reflect a keen ability to impact real-world applications positively. At HrHouz, I led the development of an applicant ranking service that enhanced resume matching accuracy, showcasing my capacity to obsess over customer needs and ensuring their expectations are exceeded through innovation and high-quality service.

Secondly, my strong computer science fundamentals are well established through my studies at UC Berkeley, where I have immersed myself in database systems, computer security, and algorithm courses. Coupled with practical experiences such as improving warehouse systems at Sayurbox using TypeScript and React, I have maintained a bias for action, consistently leveraging my technical skills to create efficient, user-friendly software solutions.

Lastly, my startup experience has honed my ability to think big and operate efficiently in dynamic environments. As a Head Teaching Assistant for CS61A, I have not only demonstrated leadership but also a commitment to learning and curiosity by managing and delivering a robust educational platform to over 1,000 students. This experience underscores my readiness to bring an entrepreneurial spirit to Amazon, ensuring my contributions fuel the company's innovative culture.

Thank you for considering my application. I look forward to the opportunity to discuss how I can further add value to Amazon.

Sincerely,

Ronald Arifin"""

    class UserObj:
        def __init__(self):
            self.name = "Ronald Arifin"
            self.address = "1988 Martin Luther King Jr. Way"
            self.city = "California" 
            self.state = "CA"
            self.zip = "94704"
            self.phone = "+15104786156"
            self.date = "October 3, 2023"
    class CoverLetterObj:
        def __init__(self, letter_string, user_info):
            self.user_info = user_info
            self.letter = letter_string
    user_obj = UserObj()
    results = CoverLetterObj(letter_string, user_obj)
    pdf_generator = CoverLetterPDFGenerator(results)
    pdf_generator.generate_pdf('output/cover_letter')

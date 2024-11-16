from typing import List, Optional
from models.user_info import UserInfo
from services.pdf_generator import PDFGenerator
from resume_parser import ResumeParser
from baml_client import b
from perplexity import PerplexityAPI

class CoverLetterGenerator:
    def __init__(self, pdf_path: Optional[str] = None):
        self.pdf_path = pdf_path
        self.parser = ResumeParser()
        self.pdf_generator = PDFGenerator()
        
    def _extract_resume(self, simple: bool = True) -> dict:
        """Extract and parse resume from PDF"""
        if not self.pdf_path:
            raise ValueError("PDF path not provided")
            
        text = self.parser.extract_text_from_pdf(self.pdf_path)
        return b.ExtractResumeSimple(text) if simple else b.ExtractResume(text)
    
    def _get_company_info(self, company_name: str) -> str:
        """Get company mission and values using Perplexity API"""
        query = (
            f"What is the mission and values of {company_name}. "
            f"What does the company do?"
        )
        return PerplexityAPI().simple_completion(query)
    
    def generate(self, 
                company_name: str, 
                # values: List[str], 
                user_info: UserInfo, 
                output_path: str,
                simple: bool = True) -> str:
        """
        Generate cover letter and save as PDF
        Returns: Path to generated PDF
        """
        resume = self._extract_resume(simple)
        company_culture = self._get_company_info(company_name)
        
        letter_content = b.GenerateCoverLetter(
            resume=resume,
            culture=company_culture,
            company_name=company_name,
            # values=",".join(values),
            user_info=str(user_info)
        )
        
        return self.pdf_generator.generate(
            user_info=user_info,
            content=letter_content.letter,
            output_path=output_path
        )

# Example usage:
if __name__ == "__main__":
    user = UserInfo(
        name="Ronald Arifin",
        address="1988 Martin Luther King Jr. Way",
        city="Berkeley",
        state="California",
        zip_code="94704",
        phone="+15104786156"
    )
    generator = CoverLetterGenerator("/Users/ronald/Documents/GitHub/resume-builder/backend/output/input1.pdf")
    generator.generate(
        company_name="Genius Sports",
        # values=["Real-World Impact", "Strong CS Fundamentals", "Start Up Experience"],
        user_info=user,
        output_path='output/cover_letter'
    )

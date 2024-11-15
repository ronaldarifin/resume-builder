from fpdf import FPDF
from models.user_info import UserInfo
import os
from typing import List

class PDFGenerator:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.set_font('Arial', size=12)

    def _clean_text(self, text: str) -> str:
        replacements = {
            '—': '-', '"': '"', '"': '"', ''': "'", ''': "'", '´': "'"
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text.encode('latin-1', 'replace').decode('latin-1')

    def _add_header(self, user_info: UserInfo) -> None:
        headers = [
            user_info.name,
            user_info.address,
            user_info.get_formatted_address(),
            user_info.phone,
            str(user_info.date)
        ]
        for header in headers:
            self.pdf.cell(0, 5, header, ln=True)

    def generate(self, user_info: UserInfo, content: str, output_path: str) -> str:
        """Generate PDF with given content and return the path"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        output_path = f"{output_path}.pdf" if not output_path.endswith('.pdf') else output_path
        
        self.pdf.add_page()
        self._add_header(user_info)
        self.pdf.cell(0, 5, "", ln=True)  # Spacing
        
        clean_content = self._clean_text(content)
        for paragraph in clean_content.split('\n'):
            self.pdf.multi_cell(0, 5, paragraph)
            self.pdf.cell(0, 5, "", ln=True)
            
        self.pdf.output(output_path)
        return output_path 
import PyPDF2
from typing import Dict
import os
from baml_client import b
from baml_client.types import Resume
import app  # This will load the environment variables


# def main():
#     resume_text = """Ronald Arifin
# 5104786156 |ronaldarifin@berkeley.edu |github.com/ronaldarifin |linkedin.com/in/ronaldarifin |www.ronaldarifin.com
# Education
# University of California, Berkeley Expected Graduation: December 2024
# Electrical Engineering and Computer Science, B.S. California
# –Relevant Coursework: Introduction to Database Systems, Introduction to the Internet: Protocol and Architecture,
# Computer Security, Operating Systems, Algorithms and Data Structures
# –Campus Organizations: Computer Science Mentors [Senior Mentor], Cloud Computing at Cal [Lead Engineer],
# Google Developers at DVC [President]
# Experience
# HRHouz June 2023 - Present
# Software Engineer Intern Remote
# –Developed and maintained a full-stack web application using React, Node.js, and PostgreSQL to streamline HR
# processes
# –Implemented RESTful APIs to handle data communication between front-end and back-end systems
# –Collaborated with cross-functional teams to gather requirements and deliver features that improved user experience
# –Utilized Git for version control and participated in code reviews to ensure high code quality
# University of California, Berkeley January 2023 - May 2023
# Teaching Assistant for CS61A: Structure and Interpretation of Computer Programs Berkeley, CA
# –Led weekly discussion sections and lab sessions for 30+ students, reinforcing concepts in Python, Scheme, and SQL
# –Held office hours to provide one-on-one support, improving student understanding and performance
# –Collaborated with course staff to develop and grade assignments, projects, and exams
# SkyGeni June 2022 - August 2022
# Software Engineer Intern Remote
# –Developed and maintained microservices using Node.js and Express.js, improving system modularity and scalability
# –Implemented data processing pipelines using Apache Kafka for real-time event streaming
# –Contributed to the design and implementation of RESTful APIs, enhancing communication between services
# –Participated in Agile development processes, including daily stand-ups and sprint planning
# Sayurbox June 2021 - August 2021
# Software Engineer Intern Jakarta, Indonesia
# –Assisted in the development of an e-commerce platform using React and Redux, improving user experience
# –Implemented responsive design principles, ensuring compatibility across various devices and screen sizes
# –Collaborated with the backend team to integrate APIs and optimize data retrieval processes
# –Participated in code reviews and contributed to the improvement of coding standards and best practices
# Projects
# Study Suite September 2022 - December 2022
# –Developed a comprehensive study management platform using React, Node.js, and MongoDB
# –Implemented features such as task scheduling, progress tracking, and collaborative study sessions
# –Utilized Redux for state management and Socket.io for real-time updates
# –Deployed the application on AWS, ensuring scalability and high availability
# Database Management System January 2023 - May 2023
# –Designed and implemented a relational database management system from scratch using C++
# –Developed key components including query parser, execution engine, and storage manager
# –Implemented B+ tree indexing for efficient data retrieval and query optimization
# –Achieved significant performance improvements over naive implementations in benchmark tests
# Honors and Certifications
# AWS Cloud Practitioner – Foundational
# Technical Skills
# Languages Technologies : Python, SQL (Postgres), NoSQL (MongoDB), Java
# Frameworks Libraries : React, Axios, Flask, Pytest, Parse
# Developer Tools : Git, Docker, Github Actions, VS Code, Postman, Make, AWS, Warp, Raycast, Vim"""
#     # Use the sync version instead of await
#     resume = b.ExtractResume(resume_text)
#     print(resume)


# if __name__ == "__main__":
#     # No need for asyncio.run() anymore
#     main()


class ResumeParser:
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from a PDF file"""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    # def convert_to_structured_data():


# if __name__ == "__main__":
#     # Create the parser
#     parser = ResumeParser()
    
#     # Specify the correct path to your PDF file
#     pdf_path = "/Users/ronald/Documents/GitHub/resume-builder/backend/output/resume.pdf"
    
#     # Call the method with the path
    # text = parser.extract_text_from_pdf(pdf_path)

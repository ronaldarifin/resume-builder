import os
import subprocess
from pylatex import Document, Package, NewPage, Command, Center, SmallText, MediumText, LargeText, LineBreak
from pylatex.base_classes import Command as NewCommand
from pylatex.utils import bold, italic, NoEscape

class ResumeSubheading:
    def __init__(self, title, date, subtitle, location, head_type='default'):
        self.title = title
        self.date = date
        self.subtitle = subtitle
        self.location = location
        self.items = []
        self.head_type = head_type
    
    def add_item(self, item):
        self.items.append(item)
    
    def generate_latex(self):
        latex = ""
        if self.head_type == 'education' or self.head_type == 'default':
            latex += r'\resumeSubheading'
            latex += r'{' + self.title + r'}{' + self.date + r'}'
            latex += r'{' + self.subtitle + r'}{' + self.location + r'}'
        elif self.head_type == 'project':
            latex += r'\resumeProjectHeading'
            latex += r'{\textbf{' + self.title + r'}}{' + self.date + r'}'
        
        if self.items:
            latex += r'\resumeItemListStart'
            for item in self.items:
                latex += r'\resumeItem{' + item + r'}'
            latex += r'\resumeItemListEnd'
        
        return latex

class ResumeSection:
    def __init__(self, title):
        self.title = title
        self.subheadings = []
    
    def add_subheading(self, subheading):
        self.subheadings.append(subheading)
    
    def generate_latex(self):
        latex = r'\section{' + self.title + r'}'
        latex += r'\resumeSubHeadingListStart'
        for subheading in self.subheadings:
            latex += subheading.generate_latex()
        latex += r'\resumeSubHeadingListEnd'
        return latex

class Resume_Builder:
    def __init__(self, resume_instance, resume_dict):
        self.resume_instance = resume_instance
        self.__build_resume(resume_dict)

    def __build_resume(self, resume_dict):
        """Build resume from dictionary data"""
        # Create info section
        info = resumeInfo(
            name=resume_dict['info']['name'],
            phone=resume_dict['info']['phone'],
            email=resume_dict['info']['email'],
            github_url=resume_dict['info']['github_url'],
            linkedin_url=resume_dict['info']['linkedin_url'],
            portfolio_url=resume_dict['info']['portfolio_url']
        )
        self.resume_instance.add_section(info)

        # Create education section
        education = ResumeSection(resume_dict['education']['title'])
        for edu in resume_dict['education']['subheadings']:
            edu_entry = ResumeSubheading(
                title=edu['title'],
                date=edu['date'],
                subtitle=edu['subtitle'],
                location=edu['location'],
                head_type='education'
            )
            for item in edu['items']:
                edu_entry.add_item(item)
            education.add_subheading(edu_entry)
        self.resume_instance.add_section(education)

        # Create experience section
        experience = ResumeSection(resume_dict['experience']['title'])
        for exp in resume_dict['experience']['subheadings']:
            exp_entry = ResumeSubheading(
                title=exp['title'],
                date=exp['date'],
                subtitle=exp['subtitle'],
                location=exp['location']
            )
            for item in exp['items']:
                exp_entry.add_item(item)
            experience.add_subheading(exp_entry)
        self.resume_instance.add_section(experience)

        # Create projects section
        projects = ResumeSection(resume_dict['projects']['title'])
        for proj in resume_dict['projects']['subheadings']:
            proj_entry = ResumeSubheading(
                title=proj['title'],
                date=proj['date'],
                subtitle=proj['subtitle'],
                location=proj['location'],
                head_type='project'
            )
            for item in proj['items']:
                proj_entry.add_item(item)
            projects.add_subheading(proj_entry)
        self.resume_instance.add_section(projects)

        # Create skills section
        skills = TechnicalSkills()
        for category, items in resume_dict['skills'].items():
            # Split the skill string into category and items
            skills.add_skill_category(category, items)
        self.resume_instance.add_section(skills)


class Resume:
    def __init__(self, resume_dict):
        self.sections = []
        self.doc = None
        self.builder = Resume_Builder(self, resume_dict)
    
    def add_section(self, section):
        self.sections.append(section)
    
    def generate_latex(self):
        # Create a new document
        self.doc = Document(documentclass='article', document_options=['letterpaper', '11pt'])

        # Add necessary packages and setup
        self.doc.packages.append(Package('latexsym'))
        self.doc.packages.append(Package('fullpage', options=['empty']))
        self.doc.packages.append(Package('titlesec'))
        self.doc.packages.append(Package('marvosym'))
        self.doc.packages.append(Package('verbatim'))
        self.doc.packages.append(Package('enumitem'))
        self.doc.packages.append(Package('hyperref', options=['hidelinks']))
        self.doc.packages.append(Package('fancyhdr'))
        self.doc.packages.append(Package('babel', options=['english']))
        self.doc.packages.append(Package('tabularx'))
        self.doc.packages.append(Package('color', options=['usenames', 'dvipsnames']))

        # Add glyphtounicode
        self.doc.preamble.append(NoEscape(r'\input{glyphtounicode}'))

        # Setup page style
        self.doc.preamble.append(NoEscape(r'\pagestyle{fancy}'))
        self.doc.preamble.append(NoEscape(r'\fancyhf{}'))
        self.doc.preamble.append(NoEscape(r'\fancyfoot{}'))
        self.doc.preamble.append(NoEscape(r'\renewcommand{\headrulewidth}{0pt}'))
        self.doc.preamble.append(NoEscape(r'\renewcommand{\footrulewidth}{0pt}'))

        # Adjust margins
        self.doc.preamble.append(NoEscape(r'\addtolength{\oddsidemargin}{-0.5in}'))
        self.doc.preamble.append(NoEscape(r'\addtolength{\evensidemargin}{-0.5in}'))
        self.doc.preamble.append(NoEscape(r'\addtolength{\textwidth}{1in}'))
        self.doc.preamble.append(NoEscape(r'\addtolength{\topmargin}{-.5in}'))
        self.doc.preamble.append(NoEscape(r'\addtolength{\textheight}{1.0in}'))

        # Other settings
        self.doc.preamble.append(NoEscape(r'\urlstyle{same}'))
        self.doc.preamble.append(NoEscape(r'\raggedbottom'))
        self.doc.preamble.append(NoEscape(r'\raggedright'))
        self.doc.preamble.append(NoEscape(r'\setlength{\tabcolsep}{0in}'))

        # Section formatting
        self.doc.preamble.append(NoEscape(r'\titleformat{\section}{\vspace{-10pt}\scshape\raggedright\large}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]'))

        # Ensure that generate pdf is machine readable/ATS parsable
        self.doc.preamble.append(NoEscape(r'\pdfgentounicode=1'))

        # Custom commands
        self.doc.preamble.append(NoEscape(r'''
        \newcommand{\resumeItem}[1]{
        \item\small{#1 \vspace{-2pt}}
        }
        \newcommand{\resumeSubheading}[4]{
        \vspace{-2pt}\item
            \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
            \textbf{#1} & #2 \\
            \textit{\small#3} & \textit{\small #4} \\
            \end{tabular*}\vspace{-7pt}
        }
        \newcommand{\resumeSubSubheading}[2]{
            \item
            \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
            \textit{\small#1} & \textit{\small #2} \\
            \end{tabular*}\vspace{-7pt}
        }
        \newcommand{\resumeProjectHeading}[2]{
            \item
            \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
            \textbf{\small#1} & #2 \\
            \end{tabular*}\vspace{-7pt}
        }
        \newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}
        \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
        \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
        \newcommand{\resumeItemListStart}{\begin{itemize}}
        \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
        '''))

        # Document content
        self.doc.append(NoEscape(r'\begin{document}'))

        # Add sections
        for section in self.sections:
            if isinstance(section, TechnicalSkills):
                self.doc.append(NoEscape(section.generate_latex()))
            else:
                self.doc.append(NoEscape(section.generate_latex()))

        self.doc.append(NoEscape(r'\end{document}'))

        return self.doc

    def generate_pdf(self, pdf_name):
        if self.doc is None:
            self.generate_latex()
        
        # Generate the PDF
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        output_file = f'{output_dir}/{pdf_name}'
        pdflatex_path = "/Library/TeX/texbin/pdflatex"
        
        try:
            self.doc.generate_pdf(
                output_file,
                compiler=pdflatex_path,
                compiler_args=['-interaction=nonstopmode'],
                clean_tex=False
            )
            print(f"PDF generated successfully at {output_file}.pdf")
        except subprocess.CalledProcessError as e:
            if os.path.exists(f"{output_file}.pdf"):
                print("PDF generated successfully, despite LaTeX warnings.")
            else:
                print(f"Error generating PDF: {e}")
                print("LaTeX output:")
                print(e.output.decode())
                raise


class resumeInfo():
    def __init__(self, name, phone, email, github_url, linkedin_url, portfolio_url):
        self.name = name
        self.phone = phone
        self.email = email
        self.github_url = github_url
        self.linkedin_url = linkedin_url
        self.portfolio_url = portfolio_url
    
    def generate_latex(self):
        latex = r'\begin{center}'
        latex += r'\textbf{\Huge \scshape ' + self.name + r'} \\ \vspace{5pt}'
        latex += r'\small ' + self.phone + r' $|$ '
        latex += r'\href{mailto:' + self.email + r'}{\underline{' + self.email + r'}} $|$ '
        latex += r'\href{' + "https://" + self.linkedin_url + r'}{\underline{' + self.linkedin_url + r'}} $|$ '
        latex += r'\href{' + "https://" + self.github_url + r'}{\underline{' + self.github_url + r'}} $|$ '
        latex += r'\href{' + "https://" + self.portfolio_url + r'}{\underline{' + self.portfolio_url + r'}}'
        latex += r'\end{center}'
        return latex
    
    

class TechnicalSkills:
    def __init__(self):
        self.skills = {}

    def add_skill_category(self, category, skills):
        self.skills[category] = skills

    def generate_latex(self):
        latex = r'\section{Technical Skills}'
        latex += r'\begin{itemize}[leftmargin=0.15in, label={}]'
        latex += r'\small{\item{'
        for category, skills in self.skills.items():
            category = category.replace("_", " ")
            latex += r'\textbf{' + category.title() + r'}{: ' + ", ".join(skills) + r'} \\'
        latex += r'}}'
        latex += r'\end{itemize}'
        return latex

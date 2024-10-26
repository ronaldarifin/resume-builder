import os
import subprocess
from pylatex import Document, Package, NewPage, Command, Center, SmallText, MediumText, LargeText, LineBreak
from pylatex.base_classes import Command as NewCommand
from pylatex.utils import bold, italic, NoEscape

def generate_resume_pdf():
    # Create a new document
    doc = Document(documentclass='article', document_options=['letterpaper', '11pt'])

    # Add necessary packages and setup
    doc.packages.append(Package('latexsym'))
    doc.packages.append(Package('fullpage', options=['empty']))
    doc.packages.append(Package('titlesec'))
    doc.packages.append(Package('marvosym'))
    doc.packages.append(Package('verbatim'))
    doc.packages.append(Package('enumitem'))
    doc.packages.append(Package('hyperref', options=['hidelinks']))
    doc.packages.append(Package('fancyhdr'))
    doc.packages.append(Package('babel', options=['english']))
    doc.packages.append(Package('tabularx'))
    doc.packages.append(Package('color', options=['usenames', 'dvipsnames']))

    # Add glyphtounicode
    doc.preamble.append(NoEscape(r'\input{glyphtounicode}'))

    # Setup page style
    doc.preamble.append(NoEscape(r'\pagestyle{fancy}'))
    doc.preamble.append(NoEscape(r'\fancyhf{}'))
    doc.preamble.append(NoEscape(r'\fancyfoot{}'))
    doc.preamble.append(NoEscape(r'\renewcommand{\headrulewidth}{0pt}'))
    doc.preamble.append(NoEscape(r'\renewcommand{\footrulewidth}{0pt}'))

    # Adjust margins
    doc.preamble.append(NoEscape(r'\addtolength{\oddsidemargin}{-0.5in}'))
    doc.preamble.append(NoEscape(r'\addtolength{\evensidemargin}{-0.5in}'))
    doc.preamble.append(NoEscape(r'\addtolength{\textwidth}{1in}'))
    doc.preamble.append(NoEscape(r'\addtolength{\topmargin}{-.5in}'))
    doc.preamble.append(NoEscape(r'\addtolength{\textheight}{1.0in}'))

    # Other settings
    doc.preamble.append(NoEscape(r'\urlstyle{same}'))
    doc.preamble.append(NoEscape(r'\raggedbottom'))
    doc.preamble.append(NoEscape(r'\raggedright'))
    doc.preamble.append(NoEscape(r'\setlength{\tabcolsep}{0in}'))

    # Section formatting
    doc.preamble.append(NoEscape(r'\titleformat{\section}{\vspace{-10pt}\scshape\raggedright\large}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]'))

    # Ensure that generate pdf is machine readable/ATS parsable
    doc.preamble.append(NoEscape(r'\pdfgentounicode=1'))

    # Custom commands
    doc.preamble.append(NoEscape(r'''
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
          \small#1 & #2 \\
        \end{tabular*}\vspace{-7pt}
    }
    \newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}
    \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
    \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
    \newcommand{\resumeItemListStart}{\begin{itemize}}
    \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
    '''))

    # Document content
    doc.append(NoEscape(r'\begin{document}'))

    # Header
    doc.append(NoEscape(r'''
    \begin{center}
        \textbf{\Huge \scshape Ronald Arifin} \\ \vspace{5pt}
        \small 510-478-6156 $|$ \href{mailto:ronaldarifin@berkeley.edu}{\underline{ronaldarifin@berkeley.edu}} $|$ 
        \href{https://linkedin.com/in/ronaldarifin}{\underline{linkedin.com/in/ronaldarifin}} $|$
        \href{https://github.com/ronaldarifin}{\underline{github.com/ronaldarifin}} $|$
        \href{https://www.ronaldarifin.com}{\underline{ronaldarifin.com}}
    \end{center}
    '''))

    # Education
    doc.append(NoEscape(r'''
    \section{Education}
    \resumeSubHeadingListStart
        \resumeSubheading
          {University of California, Berkeley}{California}
          {Electrical Engineering and Computer Science, B.S.}{Expected Graduation: December 2024}
          \resumeItemListStart
            \resumeItem{\textbf{Relevant Coursework}: Introduction to Database Systems, Introduction to the Internet: Protocol and Architecture, Computer Security, Operating Systems, Algorithms and Data Structures}
            \resumeItem{\textbf{Campus Organizations:} Computer Science Mentors [Senior Mentor], Cloud Computing at Cal [Lead Engineer], Google Developers at DVC [President]}
          \resumeItemListEnd
    \resumeSubHeadingListEnd
    '''))

    # Experience
    doc.append(NoEscape(r'''
    \section{Experience}
    \resumeSubHeadingListStart
        \resumeSubheading
          {HrHouz – Software Engineer Intern}{Jun 2024 -- Present}
          {Python, Docker, PostgreSQL, Github Actions, Embeddings}{Berkeley, CA}
          \resumeItemListStart
            \resumeItem{Led the development of a top K applicant ranking service, expanding HRHouz's product offerings to recruiters.}
            \resumeItem{Optimized resume matching for recruiters by chunking candidate resume and applying keyword searches \& \textbf{cosine similarity vector search} using pgvector improving resume search precision by 37\%}
            \resumeItem{Built pipelines to batch data transfer from OLTP to OLAP system pushing over 50.000 records, streamlining data preparation for custom embedding training.}
            \resumeItem{Streamlined service setup for PostgreSQL \& back-end server with Make and Docker, reducing build and testing time by 28\%.}
          \resumeItemListEnd
        \resumeSubheading
          {UC Berkeley - CS61A Head Teaching Assistant}{May 2023 - Present}
          {Python, SQL, Scheme}{Berkeley, CA}
          \resumeItemListStart
            \resumeItem{Led labs and discussions for Berkeley's CS61A, teaching OOP, SQL, Scheme, and recursion to over 1,000 students, improving their understanding and performance in programming fundamentals.}
            \resumeItem{Managed CS61A Edstem platform, coordinating with TAs on logistics and addressing 300+ theory questions.}
          \resumeItemListEnd
        \resumeSubheading
          {Skygeni – Software Engineer Contract}{Jan 2024 -  May 2024}
          {Python, OpenAI API, Function Calling}{Remote}
          \resumeItemListStart
            \resumeItem{Integrated an LLM chatbot into Skygeni's services, providing real-time marketing metrics insights, improving user decision-making.}
            \resumeItem{Implemented tool calls, enabling the chatbot to retrieve key marketing data within Skygeni's platform.}
          \resumeItemListEnd
        \resumeSubheading
          {Sayurbox – Software Engineer Intern}{Aug 2021 -  Feb 2022}
          {Typescript, React, Axios}{Remote}
          \resumeItemListStart
            \resumeItem{Increased Sayurbox WMS receiving process by 23\% by changing the UI and UX in 5 view controllers impacting over 72 warehouse workers with \textbf{Typescript, React, and Reactstrap} library}
            \resumeItem{Integrated 10+ APIs using \textbf{Axios} to display, submit, and delete data in various warehouse processes}
            \resumeItem{Led task distribution and communicated git merging with other engineers hitting 1 epic task per scrum cycle}
          \resumeItemListEnd
    \resumeSubHeadingListEnd
    '''))

    # Projects
    doc.append(NoEscape(r'''
    \section{Projects}
    \resumeSubHeadingListStart
      \resumeProjectHeading
          {\textbf{StudySuite: Stanford Hackathon Winner} $|$ \emph{Python, Fetch AI}}{}
          \resumeItemListStart
            \resumeItem{Engineered an interactive learning platform using uAgents, video-to-text extraction, and Large Language Models, applying active recall and spaced repetition principles to boost student retention by 200\%, winning 1st place at Stanford Treehacks out of 120 teams.}
          \resumeItemListEnd
      \resumeProjectHeading
          {\textbf{Database System} $|$ \emph{Java}}{}
          \resumeItemListStart
            \resumeItem{Designed and implemented efficient B+ Tree indexing structures for quick file look ups}
            \resumeItem{Programmed multigranularity locking and lock management system to prevent deadlock in a transaction}
            \resumeItem{Applied ARIES recovery protocol to recover data in a database crash by implementing redo and undo logging}
          \resumeItemListEnd
    \resumeSubHeadingListEnd
    '''))

    # Honors and Certifications
    doc.append(NoEscape(r'''
    \section{Honors and Certifications}
    \begin{itemize}[leftmargin=0.15in, label={}]
        \small{\item{
         \textbf{AWS Cloud Practitioner – Foundational}{}
        }}
    \end{itemize}
    '''))

    # Technical Skills
    doc.append(NoEscape(r'''
    \section{Technical Skills}
    \begin{itemize}[leftmargin=0.15in, label={}]
        \small{\item{
         \textbf{Languages \& Technologies}{: Python, SQL (Postgres), NoSQL (MongoDB), Java} \\
         \textbf{Frameworks \& Libraries}{: React, Axios, Flask, Pytest, Parse} \\
         \textbf{Developer Tools}{: Git, Docker, Github Actions, VS Code, Postman, Make, AWS, Warp, Raycast, Vim} \\
        }}
    \end{itemize}
    '''))

    doc.append(NoEscape(r'\end{document}'))

    # Generate the PDF
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = f'{output_dir}/resume'
    pdflatex_path = "/Library/TeX/texbin/pdflatex"
    
    try:
        doc.generate_pdf(
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

if __name__ == "__main__":
    generate_resume_pdf()

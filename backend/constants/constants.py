class ResumeInfo:
    def __init__(self, name, phone, email, github_url, linkedin_url, portfolio_url):
        self.name = name
        self.phone = phone
        self.email = email
        self.github_url = github_url
        self.linkedin_url = linkedin_url
        self.portfolio_url = portfolio_url

class ResumeSubheading:
    def __init__(self, title, location, subtitle, date, items):
        self.title = title
        self.location = location
        self.subtitle = subtitle
        self.date = date
        self.items = items

class ResumeSection:
    def __init__(self, title, subheadings):
        self.title = title
        self.subheadings = subheadings

class TechnicalSkills:
    def __init__(self, language_and_technologies, frameworks, developer_tools):
        self.language_and_technologies = language_and_technologies
        self.frameworks = frameworks
        self.developer_tools = developer_tools

class Resume:
    def __init__(self, info, education, experience, projects, skills):
        self.info = info
        self.education = education
        self.experience = experience
        self.projects = projects
        self.skills = skills

# Create the dummy resume object
DUMMY_RESUME_1 = Resume(
    info=ResumeInfo(
        name="Ronald Arifin",
        phone="5104786156",
        email="ronaldarifin@berkeley.edu",
        github_url="github.com/ronaldarifin",
        linkedin_url="linkedin.com/in/ronaldarifin",
        portfolio_url="www.ronaldarifin.com"
    ),
    education=ResumeSection(
        title="Education",
        subheadings=[
            ResumeSubheading(
                title="University of California, Berkeley",
                location="California",
                subtitle="Electrical Engineering and Computer Science, B.S.",
                date="Expected Graduation: December 2024",
                items=[
                    "Relevant Coursework: Introduction to Database Systems, Introduction to the Internet: Protocol and Architecture, Computer Security, Operating Systems, Algorithms and Data Structures",
                    "Campus Organizations: Computer Science Mentors [Senior Mentor], Cloud Computing at Cal [Lead Engineer], Google Developers at DVC [President]"
                ]
            )
        ]
    ),
    experience=ResumeSection(
        title="Experience",
        subheadings=[
            ResumeSubheading(
                title="HRHouz",
                location="Remote",
                subtitle="Software Engineer Intern",
                date="June 2023 - Present",
                items=[
                    "Developed and maintained a full-stack web application using React, Node.js, and PostgreSQL to streamline HR processes",
                    "Implemented RESTful APIs to handle data communication between front-end and back-end systems",
                    "Collaborated with cross-functional teams to gather requirements and deliver features that improved user experience",
                    "Utilized Git for version control and participated in code reviews to ensure high code quality"
                ]
            ),
            ResumeSubheading(
                title="University of California, Berkeley",
                location="Berkeley, CA",
                subtitle="Teaching Assistant for CS61A: Structure and Interpretation of Computer Programs",
                date="January 2023 - May 2023",
                items=[
                    "Led weekly discussion sections and lab sessions for 30+ students, reinforcing concepts in Python, Scheme, and SQL",
                    "Held office hours to provide one-on-one support, improving student understanding and performance",
                    "Collaborated with course staff to develop and grade assignments, projects, and exams"
                ]
            ),
            ResumeSubheading(
                title="SkyGeni",
                location="Remote",
                subtitle="Software Engineer Intern",
                date="June 2022 - August 2022",
                items=[
                    "Developed and maintained microservices using Node.js and Express.js, improving system modularity and scalability",
                    "Implemented data processing pipelines using Apache Kafka for real-time event streaming",
                    "Contributed to the design and implementation of RESTful APIs, enhancing communication between services",
                    "Participated in Agile development processes, including daily stand-ups and sprint planning"
                ]
            ),
            ResumeSubheading(
                title="Sayurbox",
                location="Jakarta, Indonesia",
                subtitle="Software Engineer Intern",
                date="June 2021 - August 2021",
                items=[
                    "Assisted in the development of an e-commerce platform using React and Redux, improving user experience",
                    "Implemented responsive design principles, ensuring compatibility across various devices and screen sizes",
                    "Collaborated with the backend team to integrate APIs and optimize data retrieval processes",
                    "Participated in code reviews and contributed to the improvement of coding standards and best practices"
                ]
            )
        ]
    ),
    projects=ResumeSection(
        title="Projects",
        subheadings=[
            ResumeSubheading(
                title="Study Suite",
                location="Remote",
                subtitle="",
                date="September 2022 - December 2022",
                items=[
                    "Developed a comprehensive study management platform using React, Node.js, and MongoDB",
                    "Implemented features such as task scheduling, progress tracking, and collaborative study sessions",
                    "Utilized Redux for state management and Socket.io for real-time updates",
                    "Deployed the application on AWS, ensuring scalability and high availability"
                ]
            ),
            ResumeSubheading(
                title="Database Management System",
                location="Remote",
                subtitle="",
                date="January 2023 - May 2023",
                items=[
                    "Designed and implemented a relational database management system from scratch using C++",
                    "Developed key components including query parser, execution engine, and storage manager",
                    "Implemented B+ tree indexing for efficient data retrieval and query optimization",
                    "Achieved significant performance improvements over naive implementations in benchmark tests"
                ]
            )
        ]
    ),
    skills=TechnicalSkills(
        language_and_technologies=[
            "Python",
            "SQL (Postgres)",
            "NoSQL (MongoDB)",
            "Java"
        ],
        frameworks=[
            "React",
            "Axios",
            "Flask",
            "Pytest",
            "Parse"
        ],
        developer_tools=[
            "Git",
            "Docker",
            "Github Actions",
            "VS Code",
            "Postman",
            "Make",
            "AWS",
            "Warp",
            "Raycast",
            "Vim"
        ]
    )
)

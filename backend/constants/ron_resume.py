from backend.resume_builder.resume_builder import Resume, ResumeSection, ResumeSubheading, resumeInfo, TechnicalSkills
from backend.constants.constants import DUMMY_RESUME_DICT_1

def generate_resume_pdf():

    resume = Resume(DUMMY_RESUME_1)

    # # create header
    # info = resumeInfo("Ronald Arifin", "5104786156", "ronaldarifin@berkeley.edu", "https://linkedin.com/in/ronaldarifin", "https://github.com/ronaldarifin", "https://www.ronaldarifin.com")
    # resume.add_section(info)

    # education = ResumeSection("Education")
    # berkeley = ResumeSubheading(
    #     title="University of California, Berkeley",
    #     location="California",
    #     subtitle="Electrical Engineering and Computer Science, B.S.",
    #     date="Expected Graduation: December 2024",
    # )
    # course_work = "Relevant Coursework: Introduction to Database Systems, Introduction to the Internet: Protocol and Architecture, Computer Security, Operating Systems, Algorithms and Data Structures"
    # campus_orgs = "Campus Organizations: Computer Science Mentors [Senior Mentor], Cloud Computing at Cal [Lead Engineer], Google Developers at DVC [President]"
    # berkeley.add_item(course_work)
    # berkeley.add_item(campus_orgs)
    # education.add_subheading(berkeley) 
    # resume.add_section(education)

    # # added experience
    # experience = ResumeSection("Experience")
    # hrhouz = ResumeSubheading(
    #     title="HRHouz",
    #     location="Remote",
    #     subtitle="Software Engineer Intern",
    #     date="June 2023 - Present"
    # )
    # hrhouz.add_item("Developed and maintained a full-stack web application using React, Node.js, and PostgreSQL to streamline HR processes")
    # hrhouz.add_item("Implemented RESTful APIs to handle data communication between front-end and back-end systems")
    # hrhouz.add_item("Collaborated with cross-functional teams to gather requirements and deliver features that improved user experience")
    # hrhouz.add_item("Utilized Git for version control and participated in code reviews to ensure high code quality")
    
    # ta = ResumeSubheading(
    #     title="University of California, Berkeley",
    #     location="Berkeley, CA",
    #     subtitle="Teaching Assistant for CS61A: Structure and Interpretation of Computer Programs",
    #     date="January 2023 - May 2023"
    # )
    # ta.add_item("Led weekly discussion sections and lab sessions for 30+ students, reinforcing concepts in Python, Scheme, and SQL")
    # ta.add_item("Held office hours to provide one-on-one support, improving student understanding and performance")
    # ta.add_item("Collaborated with course staff to develop and grade assignments, projects, and exams")

    # skygeni = ResumeSubheading(
    #     title="SkyGeni",
    #     location="Remote",
    #     subtitle="Software Engineer Intern",
    #     date="June 2022 - August 2022"
    # )
    # skygeni.add_item("Developed and maintained microservices using Node.js and Express.js, improving system modularity and scalability")
    # skygeni.add_item("Implemented data processing pipelines using Apache Kafka for real-time event streaming")
    # skygeni.add_item("Contributed to the design and implementation of RESTful APIs, enhancing communication between services")
    # skygeni.add_item("Participated in Agile development processes, including daily stand-ups and sprint planning")

    # sayurbox = ResumeSubheading(
    #     title="Sayurbox",
    #     location="Jakarta, Indonesia",
    #     subtitle="Software Engineer Intern",
    #     date="June 2021 - August 2021"
    # )
    # sayurbox.add_item("Assisted in the development of an e-commerce platform using React and Redux, improving user experience")
    # sayurbox.add_item("Implemented responsive design principles, ensuring compatibility across various devices and screen sizes")
    # sayurbox.add_item("Collaborated with the backend team to integrate APIs and optimize data retrieval processes")
    # sayurbox.add_item("Participated in code reviews and contributed to the improvement of coding standards and best practices")

    # experience.add_subheading(hrhouz)
    # experience.add_subheading(ta)
    # experience.add_subheading(skygeni)
    # experience.add_subheading(sayurbox)
    # resume.add_section(experience)

    # projects = ResumeSection("Projects")

    # study_suite = ResumeSubheading(
    #     title="Study Suite",
    #     location="",
    #     subtitle="Full-Stack Web Application",
    #     date="September 2022 - December 2022",
    #     head_type='project'
    # )
    # study_suite.add_item("Developed a comprehensive study management platform using React, Node.js, and MongoDB")
    # study_suite.add_item("Implemented features such as task scheduling, progress tracking, and collaborative study sessions")
    # study_suite.add_item("Utilized Redux for state management and Socket.io for real-time updates")
    # study_suite.add_item("Deployed the application on AWS, ensuring scalability and high availability")

    # database_system = ResumeSubheading(
    #     title="Database Management System",
    #     location="",
    #     subtitle="C++ Implementation",
    #     date="January 2023 - May 2023",
    #     head_type='project'
    # )
    # database_system.add_item("Designed and implemented a relational database management system from scratch using C++")
    # database_system.add_item("Developed key components including query parser, execution engine, and storage manager")
    # database_system.add_item("Implemented B+ tree indexing for efficient data retrieval and query optimization")
    # database_system.add_item("Achieved significant performance improvements over naive implementations in benchmark tests")

    # projects.add_subheading(study_suite)
    # projects.add_subheading(database_system)
    # resume.add_section(projects)

    # honors = ResumeSection("Honors and Certifications")
    # aws_cert = ResumeSubheading(
    #     title="AWS Cloud Practitioner – Foundational",
    #     location="",
    #     subtitle="",
    #     date="",
    #     head_type='default'
    # )
    # honors.add_subheading(aws_cert)
    # resume.add_section(honors)

    # # Technical Skills
    # skills = TechnicalSkills()
    # skills.add_skill_category("Languages & Technologies", "Python, SQL (Postgres), NoSQL (MongoDB), Java")
    # skills.add_skill_category("Frameworks & Libraries", "React, Axios, Flask, Pytest, Parse")
    # skills.add_skill_category("Developer Tools", "Git, Docker, Github Actions, VS Code, Postman, Make, AWS, Warp, Raycast, Vim")
    # resume.add_section(skills)

    resume.generate_pdf()

if __name__ == "__main__":
    generate_resume_pdf()

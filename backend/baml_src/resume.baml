// Defining a data model.
class Resume {
  info ResumeInfo
  education ResumeSection
  experience ResumeSection
  projects ResumeSection
  skills TechnicalSkills
}

class ResumeInfo {
  name string
  phone string
  email string
  github_url string
  linkedin_url string
  portfolio_url string
}

class ResumeSection {
  title string
  subheadings ResumeSubheading[]
}

class ResumeSubheading {
  title string
  location string
  subtitle string
  date string
  items string[]
}

class TechnicalSkills {
  language_and_technologies string[]
  frameworks string[]
  developer_tools string[]
}

// Create a function to extract the resume from a string.
function ExtractResume(resume: string) -> Resume {
  // Specify a client as provider/model-name
  // you can use custom LLM params with a custom client name from clients.baml like "client CustomHaiku"
  client "openai/gpt-4o" // Set OPENAI_API_KEY to use this client.
  prompt #"
    Extract from this content:
    {{ resume }}

    {{ ctx.output_format }}
  "#
}

function ExtractResumeSimple(resume: string) -> string {
  client "openai/gpt-4o-mini"
  prompt #"
    Explain the candidate's resume:
    {{ resume }}
    {{ ctx.output_format }}
  "#
}

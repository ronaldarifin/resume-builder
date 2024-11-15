class CoverLetter {
  letter string @description("The cover letter content")
  user_info UserInfo
}
class UserInfo {
  name string
  address string
  city string
  state string
  zip string
  phone string
  date string
}

function GenerateCoverLetter(resume: string, culture: string, company_name: string, values: string, user_info: string) -> CoverLetter {
  client "openai/gpt-4o"
  prompt #"
    You are a FAANG hiring manager. Help {{user_info}} get hired at {{company_name}} by writing a cover letter.
    I would like you to write a 3 point based Cover Letter based on these 3 value propositions: {{values}}.
    Please tailor the cover letter to the company's culture of {{culture}}.
    Be concise, use simple sentences, and avoid fluff words.
    Put relevant information from the resume to support your points.
    Here is their resume:
    {{ resume }}
    {{ ctx.output_format }}
  "#
}

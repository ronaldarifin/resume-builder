

function GenerateCoverLetter(resume: string, culture: string, company: string, values: string) -> string {
  client "openai/gpt-4o"
  prompt #"
    You are a FAANG hiring manager. Help me get hired at {{company}} by writing a cover letter.
    I would like you to write a 3 point based Cover Letter based on these 3 value propositions: {{values}}.
    Please tailor the cover letter to the company's culture of {{culture}}.
    Here is their resume:
    {{ resume }}
    {{ ctx.output_format }}
  "#
}

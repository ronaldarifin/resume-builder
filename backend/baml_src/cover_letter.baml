class CoverLetter {
  letter string @description("The cover letter content only")
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


function GenerateCoverLetter(resume: string, culture: string, company_name: string, user_info: string) -> CoverLetter {
  client "openai/gpt-4o"
  prompt #"
    You are a FAANG hiring manager. Help {{user_info}} get hired at {{company_name}} by writing a cover letter.
    Please tailor it to {{company_name}}'s culture of {{culture}}.
    Don't just name the culture blatantly, but rather weave it into the letter and how I'm excited about the opportunity as an engineer.
    Be concise, use simple sentences, and avoid fluff words. Limit to maximum 1 page or 4 paragraphs.
    Put relevant information from the resume to support your points.
    Here is their resume:
    {{ resume }}

    This is a good cover letter example:
    Dear Maureen and hiring team,
    
    I was so excited to see your post on LinkedIn because it’s exactly the type of job I’m looking for: an opportunity to bring my experience with video production and enthusiasm for storytelling to an organization that sets the standard for high-quality management content.

    In addition to five years of experience in broadcast journalism, research, and video production, I would bring an organized and systems-level perspective to this role. I view video production as a puzzle, and like to think about which parts need to come together in order to make a great final product. My approach is to have in-depth conversations with my team members, and the various stakeholders, before each project. This helps me nail down the logistics — from location to talent.

    From there, the fun begins: fleshing out the concept and identifying what visuals will best represent it. Ideation and storyboarding are essential in this step. I know I’m not right all the time, so I enjoy working with a diverse team that can bring in new perspectives, brainstorm, and pitch ideas that will make the final product stronger. Whenever possible, I also try to seek out other sources for inspiration, like magazines, which allow me to observe different ways of expression and storytelling. This approach has served me well. It’s what has allowed me to enter the film industry and grow as a creator.

    On my website, you can see examples of how I use the above process to create fun, engaging content.

    Given this experience and my enthusiasm for the work you do, I believe I’d make a great addition to your team. I recently had a chance to try out your Patient Zero product at my current organization. The simulation is both challenging and engaging. I was impressed by your ability to apply  different storytelling methods to an online training course (which, let’s admit, can often be a little dry). Your work exemplifies exactly what I believe: There’s an opportunity to tell a compelling story in everything — all you have to do is deliver it right.

    I’d love to come in and speak with you more about what I’d be able to offer in this role. Harvard Business Publishing is my top choice and I believe I’d make valuable contributions to your team.

    Thank you for your time and consideration!
    {{ ctx.output_format }}
  "#
}

#core/prompts.py
class Prompts:
    def system_prompt(self):
        return """You are an assistant that analyzes the contents of a website 
                  and provides a short summary, ignoring text that might be navigation related. 
                  Respond in markdown."""
    
    def user_prompt_for(self, website):
        user_prompt = f"You are looking at a website titled {website.title}"
        user_prompt += "\nThe contents of this website is as follows; \
    please provide a short summary of this website in markdown. \
    If it includes news or announcements, then summarize these too.\n\n"
        user_prompt += website.text
        return user_prompt

    def messages_for(self, website):
        return [
            {"role": "system", "content": self.system_prompt()},
            {"role": "user", "content": self.user_prompt_for(website)}
        ]
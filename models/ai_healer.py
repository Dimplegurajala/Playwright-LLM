import ollama
from langextract import extract

class AIHealer:
    def __init__(self, model="llama3.2"):
        self.model = model

    def suggest_fix(self, broken_selector, html_source):
        # use Langextract to prune the DOM and get structured data
        schema = {
            "type": "string",   # role, label, text, placeholder
            "value": "string",  # button, link
            "name": "string",   # Submit, Login
            "confidence_score": "number"
        }
        
        # Pruned context for the model
        pruned_elements = extract(html_source, schema)

        # User Prompt for Ollama
        user_prompt = f"""
        CONTEXT: The following elements were found on the page: {pruned_elements}
        PROBLEM: The Playwright selector '{broken_selector}' is no longer working.
        TASK: Based on the context, identify the most likely replacement. 
        Return ONLY a JSON object with 'type', 'value', and 'name'.
        """

        # Calling the Ollama API
        response = ollama.chat(model=self.model, messages=[
            {
                'role': 'user',
                'content': user_prompt,
            },
        ])

        return response['message']['content']
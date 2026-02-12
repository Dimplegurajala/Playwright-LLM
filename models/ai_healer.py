from langextract import extract

class AIHealer:
    def __init__(self, model="llama3.2"):
        self.model = model

    def suggest_fix(self, broken_selector, html_source):
        schema = {
            "type": "string",   # role, label, text, placeholder
            "value": "string",  # button, link
            "name": "string",   # Submit, Login
            "confidence_score": "number"
        }
        prompt = f"The element {broken_selector} is missing. Suggest a stable Playwright Semantic Locator from this HTML."
        
        try:
            result = extract(html_source, schema, prompt=prompt)
            attr = result[0].attributes
            return {
                "type": attr.get("type"),
                "value": attr.get("value"),
                "name": attr.get("name")
            }
        except Exception:
            return None
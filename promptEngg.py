import google.generativeai as genai

class SimplePromptManager:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def get_response(self, user_input: str) -> str:
        """Get AI response for user input with a structured prompt."""
        prompt = f"""
        Question: {user_input}
        Please provide a clear and helpful response.
        """
        response = self.model.generate_content(prompt)
        return response.text

def main():
    api_key = "AIzaSyC9SOZ_dr2Dfg53HNxrAWrurhwKORT_DjY" 
    pm = SimplePromptManager(api_key)
    
    while True:
        user_input = input("\nEnter your question : ")  
        if user_input.lower() == 'quit':
            print("Bye")
            break
        response = pm.get_response(user_input)
        print("\nAI :", response)

if __name__ == "__main__":
    main()
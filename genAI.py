import google.generativeai as genai
from typing import Optional
import logging

class GoogleAIChat:
    
    def __init__(self, api_key: str, model_name: str = "gemini-pro"):
        try:
            genai.configure(api_key=api_key)
            
            self.generation_config = {
                "temperature": 1,
                "top_p": 0.95,
                "max_output_tokens": 8192
            }
            
            self.model = genai.GenerativeModel(
                model_name=model_name,
                generation_config=self.generation_config
            )
            
            self.chat_session = self.model.start_chat(history=[])
            
        except Exception as e:
            logging.error(f"Failed to initialize Google AI chat: {str(e)}")
            raise
    
    def send_message(self, message: str) -> Optional[str]:
        try:
            response = self.chat_session.send_message(message)
            return response.text
            
        except Exception as e:
            logging.error(f"Failed to send message: {str(e)}")
            return None
            
    def start_interactive_chat(self):
        print("Start a chat! Type 'quit' to exit.")
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
                
            if user_input:
                response = self.send_message(user_input)
                if response:
                    print("\nAI:", response)
                else:
                    print("\nError: Failed to get response")

def main():
    try:
        # Initialize chat client
        chat = GoogleAIChat(api_key="AIzaSyC9SOZ_dr2Dfg53HNxrAWrurhwKORT_DjY")
        
        # Start interactive chat
        chat.start_interactive_chat()
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
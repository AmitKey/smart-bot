'''

genai.configure(api_key = API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("help me explain for a friend that im taking online course to become Data Engineer, 1 sentcne ")

print(response)
'''

import google.generativeai as genai


class GenAiManager:
    def __init__(self):
        self.configurations = {}
        self.initialized = False
        self.model = None

    def genai_init(self):
        # Initialize with some default configurations
        self.configurations = {
            'api_key': None,
            'model': None,
            'version': '1.0',
            'parameters': {}
        }
        self.initialized = True
        print("GenAI Manager initialized with default settings.")

    def configure(self, api_key):
        if not self.initialized:
            raise Exception("GenAI Manager is not initialized. Call genai_init() first.")
        # Configure the API key
        self.configurations['api_key'] = api_key
        genai.configure(api_key=api_key)
        print(f"API key configured.")

    def set_model(self, model_name):
        if not self.initialized:
            raise Exception("GenAI Manager is not initialized. Call genai_init() first.")
        # Load the generative model
        self.model = genai.GenerativeModel(model_name)
        self.configurations['model'] = model_name
        print(f"Model set to: {model_name}")

    def generate_response(self, message):
        if not self.initialized:
            raise Exception("GenAI Manager is not initialized. Call genai_init() first.")
        if not self.model:
            raise Exception("Model is not set. Call set_model() first.")
        # Generate a response using the model
        response = self.model.generate_content(message)
        return response

    def get_config(self):
        # Retrieve current configurations
        return self.configurations

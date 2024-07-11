from GenaiManager import GenAiManager
from config import API_KEY


def ask_bot(manager, message):
	answer = manager.generate_response(message)
	return answer


if __name__ == "__main__":
	manager = GenAiManager()
	manager.genai_init()  # Initialize with default settings
	manager.configure(api_key=API_KEY)  # Configure API key
	manager.set_model('gemini-1.5-flash')  # Set the model

	# Generate a response
	message = input('What is your message?')
	# response = manager.generate_response(message)
	# print(response)
	response = ask_bot(manager, message)
	print(response)

import openai
import os


api = os.getenv("OPEAI_API")


class Chatbot:
    def __init__(self):
        openai.api_key = api

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=4000,
            temperature=0.5
        ).choices[0].message.content

        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response(user_input="Write a joke about birds")
    print(response)

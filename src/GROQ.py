from groq import Groq


# from  trash import s, sys, m_m


class Model():
    def __init__(self, key):
        self.key = key
        self.client = Groq(
            api_key=self.key
        )

    def get_answer(self, content: str) -> str:
        chat = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a respectful, helpful and honest stock market analysis assistant. You should give a forecast of the stock market's reaction to events that occur in the world or with a certain company"
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            model="llama3-70b-8192"
        )

        return chat.choices[0].message.content


if __name__ == "__main__":
    model = Model("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")
    print(model.get_answer('что может произойти после этого события: '))

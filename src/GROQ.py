from groq import Groq


# from  trash import s, sys, m_m


class Model():
    def __init__(self, key):
        self.key = key
        self.client = Groq(
            api_key=self.key
        )

    def get_answer(self, content: str) -> str:
        answer = ''

        chat = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "As a factual stock market analyst, I can provide insights into the impact of significant events on the performance of stocks. I will base my analysis solely on real-world data and credible sources to deliver accurate explanations for stock price fluctuations."
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            model="llama3-70b-8192"
        )

        answer = chat.choices[0].message.content

        return answer


if __name__ == "__main__":
    # ВКЛЮЧИТЬ VPN!!!!!!!!!!!!!!!!!!
    model = Model("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")
    print(model.get_answer('что может произойти после этого события: '))

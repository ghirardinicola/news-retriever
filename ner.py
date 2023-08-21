import os
import openai

# Ensure you have the OpenAI library installed
# pip install openai

def get_answers_from_gpt(content, questions):
    openai.api_key  = os.environ.get("OPENAI_API_KEY")

    answers = []

    for question in questions:
        prompt = f"{content}\n\nQuestion: {question}\nAnswer:"
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=500)
        answer = response.choices[0].text.strip()
        answers.append(answer)

    return answers

# Usage
if __name__ == "__main__":
    # Sample usage:
    content = "The sun is a star located at the center of our Solar System. It is primarily composed of hydrogen and helium."

    questions = [
        "Where is the sun located?",
        "What is the sun primarily composed of?"
    ]

    responses = get_answers_from_gpt(content, questions)
    for q, a in zip(questions, responses):
        print(f"Q: {q}\nA: {a}\n")

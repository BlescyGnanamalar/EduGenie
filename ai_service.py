from google import genai

from .config import settings


def ask_ai(question: str) -> str:

    if not settings.GEMINI_API_KEY:
        return "Gemini API key is missing. Please add it to the .env file."

    try:

        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=question
        )

        if response.text:
            return response.text

        return "No answer was generated."

    except Exception as e:

        return f"Unable to answer question: {str(e)}"


def generate_quiz(topic: str) -> str:

    prompt = f"""
Create a short educational quiz about:

{topic}

Create 5 multiple-choice questions.

For each question provide:
1. Question
2. Four options (A, B, C, D)
3. Correct answer
4. Short explanation

Keep the quiz suitable for college students.
"""

    return ask_ai(prompt)


def simplify_concept(topic: str) -> str:

    prompt = f"""
Explain the following concept in very simple language:

{topic}

Give:
1. Simple definition
2. Easy explanation
3. One real-life example
4. Key points

Make it easy for a college student to understand.
"""

    return ask_ai(prompt)


def generate_learning_path(topic: str) -> str:

    prompt = f"""
Create a structured learning path for:

{topic}

Include:

1. Beginner topics
2. Intermediate topics
3. Advanced topics
4. Suggested timeline
5. Practice suggestions
6. Projects or exercises

Make the learning path clear and practical for a student.
"""

    return ask_ai(prompt)


def summarize_text(text: str) -> str:

    prompt = f"""
Summarize the following educational text.

Give:
1. Short summary
2. Important points
3. Key terms

Text:

{text}
"""

    return ask_ai(prompt)
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
print("=" * 60)
print("          AI CODE EXPLAINER V1")
print("=" * 60)

print("\nPaste your code below.")
print("Type END on a new line when finished.\n")

lines = []

while True:
    line = input()
    if line.upper() == "END":
        break
    lines.append(line)

code = "\n".join(lines)

prompt = f"""
You are an expert software engineer.

Analyze the following code.

Code:
{code}

Provide:

1. Programming Language
2. Purpose of the Code
3. Line-by-Line Explanation
4. Input and Output
5. Time Complexity
6. Space Complexity
7. Bug Detection (if any)
8. Optimization Suggestions
9. Best Practices

Explain in simple language.
"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = response.text

    print("\n" + "=" * 60)
    print("CODE ANALYSIS REPORT")
    print("=" * 60 + "\n")

    print(result)

    # Save report
    with open("analysis_report.txt", "w", encoding="utf-8") as file:
        file.write(result)

    print("\nReport saved as analysis_report.txt")

except Exception as e:
    print("Error:", e)
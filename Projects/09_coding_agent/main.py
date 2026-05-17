import argparse
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)
def get_response(file_name,user_prompt):
    # print(f"Filename: {file_name}")
    # print(f"Prompt: {user_prompt}")
    try:
        with open(file_name, "r") as f:
            file_content = f.read()
    except FileNotFoundError as e:
        return (f"File not found error: {e}")
    
    PARTS = '''You are a strict code-generation engine.

Your job is to generate ONLY source code based on the user's instruction.

Rules (MANDATORY):
1. Output ONLY valid source code.
2. Do NOT add explanations, comments, markdown, or headings.
3. Do NOT wrap code in backticks.
4. Do NOT describe what the code does.
5. Do NOT include any text before or after the code.
6. If the instruction is unclear, make reasonable assumptions and still produce code.
7. The output must be directly copy-paste runnable.
8. Follow best practices for the given programming language.
9. Do not include placeholder text like "your code here".
10. If modifying existing code, return the FULL modified code, not a diff.
11. If modifying existing code, preserve the original formatting and style as much as possible.,
12. Don't vanish user code entirely unless explicitly instructed.
If you violate any rule, the output is considered incorrect.
'''
    if file_content:
        final_prompt = f"""
{PARTS}

User instruction:
{user_prompt}

Existing code:
{file_content}
"""

    else:
        final_prompt = f"""{PARTS}

User instruction:
{user_prompt}
"""

    
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=final_prompt
        )

        final_code = response.text

        with open(file_name,"w") as f:
            f.write(final_code)

    except Exception as e:
        print(f"An error occurred: {e}")


parser = argparse.ArgumentParser(
    prog = "coding-agent",
    description = "CLI coding agent powered by gemini-2.5-flash-lite",
    epilog = "Example:\n coding-agent 'file.py' --prompt 'Write a code for calculator'"
)

parser.add_argument(
                    "filename",
                    help="name of the file to modify"
)
parser.add_argument(
                    "--prompt",
                    help="changes that should be done in file",
                    required=True
)

if __name__ == "__main__":
    args = parser.parse_args()
    get_response(args.filename,args.prompt)
    

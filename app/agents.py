from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from app.config import GOOGLE_API_KEY
from app.tools import calculator
import os

tools=[calculator]
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}")
])

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant for whether info",
)

chain = prompt | llm

def run_genai(question: str) -> str:
    response = chain.invoke({"question": question})
    return response.content

# Run the agent
def run_agent2(question: str) -> str:
    result = agent.invoke(
    {"messages": [{"role": "user", "content": question}]}
    )
    return result['messages'][-1].content


       

def _read_project_files(folder_path: str):
    """
    Reads all relevant files from a folder and returns:
    - tree structure string
    - combined file contents
    """

    if not os.path.exists(folder_path):
        return None, None, "Folder does not exist."

    project_tree = ""
    combined_content = ""
    max_total_chars = 15000  # Safety limit for LLM input size

    ignored_dirs = {"venv", "node_modules", "__pycache__", ".git"}
    ignored_files = {".env"}

    for root, dirs, files in os.walk(folder_path):
        # remove ignored directories
        dirs[:] = [d for d in dirs if d not in ignored_dirs]

        level = root.replace(folder_path, "").count(os.sep)
        indent = "  " * level
        project_tree += f"{indent}{os.path.basename(root)}/\n"

        subindent = "  " * (level + 1)

        for file in files:
            if file in ignored_files:
                continue

            file_path = os.path.join(root, file)

            # skip large files
            if os.path.getsize(file_path) > 200000:  # 200 KB limit
                continue

            project_tree += f"{subindent}{file}\n"

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    entry = f"\n\n### File: {file_path}\n{content}\n"

                    # Apply total size limit
                    if len(combined_content) + len(entry) < max_total_chars:
                        combined_content += entry

            except:
                continue

    if not combined_content.strip():
        return None, None, "No readable source files found."

    return project_tree, combined_content, None



def generate_readme_from_folder(folder_path: str):
    project_name = os.path.basename(folder_path)
    """
    Generates README.md content using Gemini based on project folder.
    """

    project_tree, project_content, error = _read_project_files(folder_path)

    if error:
        return error

    prompt = f"""
You are a senior technical writer.

Generate a professional README.md for the project named "{project_name}".

Include:
- Project Overview
- Folder Structure explanation
- Tech Stack used
- How to Run
- Features
- Possible Improvements

Project Structure:
{project_tree}

Project Files Content:
{project_content}

Return only clean README markdown.
"""

    response = run_genai(prompt)

    return response

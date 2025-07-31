import os
import fitz  
from docx import Document  
from langchain.tools import tool

@tool

def get_file(file_path: str) -> dict:
    """
    Reads content from a file (txt, pdf, docx).
    Returns first 1000 characters.
    """
    try:
        if not os.path.exists(file_path):
            return {
                "error": f"❌ File not found: {file_path}"
            }

        ext = os.path.splitext(file_path)[-1].lower()

        if ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

        elif ext == ".pdf":
            content = ""
            with fitz.open(file_path) as doc:
                for page in doc:
                    content += page.get_text()

        elif ext == ".docx":
            doc = Document(file_path)
            content = "\n".join([p.text for p in doc.paragraphs])

        else:
            return {
                "error": f"⚠️ Unsupported file type: {ext}",
                "file_path": file_path
            }

        return {
            "tool": "file",
            "file_path": file_path,
            "content": content[:1000] + "......" if len(content) > 1000 else content
        }

    except Exception as e:
        return {
            "error": f"⚠️ Error reading file: {str(e)}",
            "file_path": file_path
        }

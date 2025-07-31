import requests
import urllib.parse
from langchain.tools import tool

@tool
def get_calculator(expression:str) -> dict:
    """
    evaluates a math expression using the math.js ApI.

    Args:
    expression (str): A valid mathematical expression(e.g , "2+2*3)

    returns:
    dict:a dictionary with either the result or an error message.
    """
    try:
        expression = expression.strip().lower().replace("^","**").replace("×", "*").replace("÷", "/")
        encoded_expr = urllib.parse.quote(expression)

        url=f"https://api.mathjs.org/v4/?expr={encoded_expr}"
        response= requests.get(url,timeout=5)

        if response.status_code == 200:
            return{
                "tool":"calculator",
                "input":expression,
                "result":response.text.strip()
            }
        
        return{
                "error": f"❌ calculator returned an error: {response.status_code}",
                "input":expression
            }
    except requests.exceptions.RequestException as e:
        return {
            "error": f"🌐 Network Error: {str(e)}",
            "input": expression
        }
    except Exception as e:
        return{
           "Error" : f"💥 oops something went wrong : {str(e)}",
           "input" : expression
        }
        

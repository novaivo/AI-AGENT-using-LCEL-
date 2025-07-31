import requests
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
from urllib.parse import quote
from langchain.tools import tool

@tool
def get_wikipedia(topic: str) -> dict:
    """
    Searches for a topic on Wikipedia and returns a summary with title and URL.

    Args:
        topic (str): The topic to search on Wikipedia (e.g., 'Ada Lovelace').

    Returns:
        dict: Title, summary, and link to the article, or an error message.
    """
    try:
        clean_topic = topic.lower().replace("who is", "").replace("what is", "").strip()
        search_results = wikipedia.search(clean_topic)
        if not search_results:
            return {"error": f"❌ No results found for: '{clean_topic}'"}
        
        page_title = search_results[0]
        encoded_title = quote(page_title.replace(" ", "_"))
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_title}"
        
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        return {
            "title": data.get("title", page_title),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
            "summary": data.get("extract", "No summary available"),
        }
    
    except DisambiguationError as e:
        return {"error": f"🔍 Multiple matches: {', '.join(e.options[:3])}..."}
    except PageError:
        return {"error": f"❌ Page not found for: '{clean_topic}'"}
    except requests.RequestException as e:
        return {"error": f"🌐 Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"🚫 Unexpected error: {str(e)}"}
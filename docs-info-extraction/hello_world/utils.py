from re import findall
from re import DOTALL


def extract_snippet_from_tags(text, tag = 'json'):
    # Padrao de regex para encontrar o snippet dentro das tags <json> e </json>
    pattern = rf'<{tag}>(.*?)</{tag}>'        
    results = findall(pattern, text, DOTALL)
    
    if results:
        return results[0]
    return text
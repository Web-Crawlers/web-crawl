import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        main_content = extract_main_content(soup)
        if main_content: 
            return { 
                "url": url, 
                "content": main_content, 
            } 
        return None

def extract_main_content(soup): 
    main_content = '' 
    # Look for common tags used for main content 
    main_content_tags = soup.find_all(['div', 'article', 'section'], class_=['main-content', 'content', 'post', 'article', 'entry-content', 'entry-header']) 
    for tag in main_content_tags: 
        main_content += tag.get_text(separator='\n')
    # Remove extra whitespace 
    main_content = ' '.join(main_content.split())
    return main_content.strip()

# Example usage
if __name__ == "__main__":
    url = "https://blogs.nvidia.com/blog/geforce-now-thursday-farming-simulator-25/"  # "https://www.example.com" #https://blogs.nvidia.com/blog/geforce-now-thursday-farming-simulator-25/
    content = crawl(url)
    if content:
        print(content)
    else:
        print("Failed to retrieve content")

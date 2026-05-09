import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://www.bbc.com/news"
    
    print("data BBC load...\n")
    
    try:
        
        response = requests.get(url)
        
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        headlines = soup.find_all('h2')
        
        print("--- today news---")
        
        count = 0
        for title in headlines:
            text = title.get_text().strip()
            if text and count < 10:
                count += 1
                print(f"{count}. {text}")
                
    except Exception as e:
        print(f"error do: {e}")

if __name__ == "__main__":
    get_news()
        


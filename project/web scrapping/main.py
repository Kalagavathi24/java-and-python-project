from scraper import scrape_books
from save_data import save_to_csv
import requests

def scrape_and_store():
    try:
        book_data = scrape_books()
        if book_data:
            save_to_csv(book_data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data:{e}")
if __name__ == "__main__": 
    scrape_and_store()      
            
    

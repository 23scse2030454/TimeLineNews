from dataingestion.ingest import fetch_news
from database.db_handler import init_db, save_news

def start_scraper():
    print("--- News Scraper Starting ---")
    
    # 1. Initialize Database
    init_db()
    
    # 2. Fetch News Data
    print("Fetching latest news articles...")
    fresh_news = fetch_news()
    
    # 3. Save to Database
    if fresh_news:
        save_news(fresh_news)
        print("--- Scraper task completed successfully! ---")
    else:
        print("No new articles found or an error occurred.")

if __name__ == "__main__":
    start_scraper()

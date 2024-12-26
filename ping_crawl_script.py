import requests
import time

# Constants
PING_CRAWL_URL_TEMPLATE = "https://dash.parsely.com/{api_key}/ping_crawl?secret={api_secret}&url="
BATCH_SIZE = 150  # Number of URLs to process in each batch
WAIT_TIME = 10    # Delay (in seconds) between batches

def send_ping(url, ping_crawl_url):
    """
    Send a POST request to the Parse.ly crawl endpoint for a specific URL.

    Args:
        url (str): The URL to be crawled.
        ping_crawl_url (str): The formatted Parse.ly crawl endpoint URL.
    """
    try:
        response = requests.post(f"{ping_crawl_url}{url}")
        if response.status_code == 200:
            print(f"Successfully pinged: {url}")
        else:
            print(f"Failed to ping: {url} - HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging {url}: {e}")

def process_urls(file_path, api_key, api_secret):
    """
    Read URLs from a file and process them in batches.

    Args:
        file_path (str): Path to the file containing the list of URLs.
        api_key (str): Parse.ly API key.
        api_secret (str): Parse.ly API secret.
    """
    # Format the base crawl URL with the provided API key and secret
    ping_crawl_url = PING_CRAWL_URL_TEMPLATE.format(api_key=api_key, api_secret=api_secret)
    
    # Read URLs from the specified file
    with open(file_path, "r") as file:
        urls = [line.strip() for line in file if line.strip()]  # Strip whitespace and ignore empty lines
    
    total_urls = len(urls)
    print(f"Total URLs to process: {total_urls}")
    
    # Process URLs in batches
    for i in range(0, total_urls, BATCH_SIZE):
        batch = urls[i:i + BATCH_SIZE]
        print(f"Processing batch {i // BATCH_SIZE + 1} of {((total_urls - 1) // BATCH_SIZE) + 1}")
        
        for url in batch:
            send_ping(url, ping_crawl_url)
        
        # Add a delay between batches if more URLs remain
        if i + BATCH_SIZE < total_urls:
            print(f"Waiting {WAIT_TIME} seconds before processing the next batch...")
            time.sleep(WAIT_TIME)

if __name__ == "__main__":
    # Prompt for API_KEY and API_SECRET
    api_key = input("Enter your Parse.ly API_KEY: ").strip()
    api_secret = input("Enter your Parse.ly API_SECRET: ").strip()
    
    # Replace 'urls.txt' with the path to your file containing the URLs
    process_urls("urls.txt", api_key, api_secret)

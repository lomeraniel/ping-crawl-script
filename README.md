# Parse.ly URL Ping Script

This script is designed to send URLs to the Parse.ly crawl endpoint in batches. It allows you to efficiently manage the number of URLs sent in each batch and includes a delay between batches to avoid overloading the system. The script reads URLs from a file, pings the Parse.ly crawl API, and logs the results.

## Features
- Batch processing of URLs (default: 150 URLs per batch).
- Delay between batches to avoid rate-limiting (default: 10 seconds).
- Customizable API Key and Secret integration.
- Graceful handling of errors during API requests.

## Prerequisites
- Python 3.x installed on your machine.
- requests library installed (pip install requests).

## Setup
1. Clone or download this script to your local machine.
2. Ensure you have a file (urls.txt by default) with one URL per line.
3. Install dependencies using:

```
pip install requests
```

## Usage
1. Run the script:

```
python script_name.py
```

2. Enter your Parse.ly API Key and Secret when prompted.
3. Ensure the urls.txt file is in the same directory or provide the full path to the file in the process_urls function.

## Input File Format

The input file should contain one URL per line. Example:

```			
https://example.com/article1
https://example.com/article2
https://example.com/article3
```

## How It Works
1. The script reads URLs from the specified file.
2. URLs are processed in batches (default: 150 per batch).
3. Each URL is sent to the Parse.ly crawl API:

```
https://dash.parsely.com/<API_KEY>/ping_crawl?secret=<API_SECRET>&url=<URL>
```

4. After each batch, the script waits for a specified delay (default: 10 seconds).
5. Logs the success or failure of each URL ping.

## Example Output

```
Enter your Parse.ly API_KEY: your_api_key
Enter your Parse.ly API_SECRET: your_api_secret
Total URLs to process: 300
Processing batch 1 of 2
Successfully pinged: https://example.com/article1
Successfully pinged: https://example.com/article2
...
Waiting 10 seconds before processing the next batch...
Processing batch 2 of 2
Successfully pinged: https://example.com/article299
Successfully pinged: https://example.com/article300
```

## Customization

Change Batch Size and Wait Time

To modify the number of URLs processed per batch or the delay between batches, update the following constants in the script:

```
BATCH_SIZE = 150  # Number of URLs per batch
WAIT_TIME = 10    # Delay in seconds between batches
```

## Change Input File Path

By default, the script reads from urls.txt. To use a different file, change this line in the script:

process_urls("urls.txt", api_key, api_secret)

Replace "urls.txt" with your desired file path.

Error Handling
- The script logs failed requests with the HTTP status code and URL.
- If the API fails, it retries the remaining URLs in the next batch.

## License

This script is provided as-is and is free to use and modify.

Feel free to contribute or raise issues if you encounter any problems!

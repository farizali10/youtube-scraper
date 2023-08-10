# Krish Naik YouTube Data Scraper
This project is a YouTube data scraper that extracts video information, including video details, likes, and comments, from Krish Naik's YouTube channel. The scraped data is then stored in a MySQL database for further analysis and reference.

## Features
- Scrapes video information from Krish Naik's YouTube channel.
- Retrieves video title, video details, number of likes, and person name with comments.
- Stores the extracted data in a MySQL database.
- Implements exception handling to manage potential errors during scraping and database operations.
- Follows a modular coding structure for better organization and maintainability.
## Requirements
- Python 3.8
- MySQL Server
- Required Python libraries
```
  pip install -r requirements.txt
```
## How to Use
1. Clone the repository to your local machine.
2. Install the required Python libraries if you haven't already.

3. Run the person_comment.py script to start scraping and storing data.
```
python person_comment.py
```
## Exception Handling
Exception handling has been implemented to ensure that the script handles errors gracefully. This includes handling network errors, parsing errors, and database connection errors.

## Modular Coding
The codebase follows a modular structure for better organization. Different functions are separated into appropriate modules to enhance readability and maintainability.

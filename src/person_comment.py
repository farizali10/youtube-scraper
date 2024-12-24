from slow_scroll_func import slow_scroll_to_end
from url_driver import driver
from href import get_url
from urllib.parse import urlparse
import mysql.connector as connection

# Connect to the MySQL database
mydb = connection.connect(
    host='localhost',
    user='root',
    passwd="example"
)
cursor = mydb.cursor()

# Uncomment the lines below if the database and table need to be created
cursor.execute("DROP DATABASE IF EXISTS channel_details")
cursor.execute("CREATE DATABASE IF NOT EXISTS channel_details")
cursor.execute("USE channel_details")
cursor.execute("CREATE TABLE if not exists urls (id INT NOT NULL UNIQUE AUTO_INCREMENT, url VARCHAR(100) NOT NULL UNIQUE)")
cursor.execute("create table if not exists comments(id int not null unique auto_increment, coment text not null, name text not null,url_id int not null, foreign key (url_id) references urls(id))")

# Set YouTube channel URL
yt_url = "https://www.youtube.com/@krishnaik06/videos"

# Get video URLs
href_list = []
get_url(href_list, yt_url)
href_list = href_list[:3]
url_counter = 1

### STORE THE EXTRACTED COMMENTS + URL IN THE DATABASE ###

for url_string in href_list:
    try:
        cursor.execute("INSERT INTO channel_details.urls (url) VALUES (%s)", (url_string,))
        mydb.commit()
        print(f"Inserted URL: {url_string} - URL Key: {url_counter}")

        # Iterate through video URLs and extract comments
        converted_url = urlparse(url_string)
        driver.get(converted_url.geturl())
        slow_scroll_to_end(driver)

        comments = driver.find_elements_by_css_selector("yt-formatted-string.style-scope.ytd-comment-renderer")
        comment_counter = 0
        for index in range(0, len(comments), 2):
            if index + 1 < len(comments):
                comment = comments[index]
                next_view = comments[index + 1]
                if next_view and comment:
                    comment_str = f"-{next_view.text} -- Dated: {comment.text}"
                    cursor.execute("INSERT INTO channel_details.comments (coment, url_id) VALUES (%s, %s)", (comment_str, url_counter))
                    mydb.commit()
                    comment_counter += 1

        comment_authors = driver.find_elements_by_css_selector("h3.style-scope.ytd-comment-renderer")
        comment_authors_counter = 0
        for comment_author in comment_authors:
            if comment_author:
                comment_author_name = comment_author.text
                cursor.execute("INSERT INTO channel_details.comments (coment, name, url_id) VALUES ('', %s, %s)",(comment_author_name, url_counter))
                mydb.commit()
                comment_authors_counter += 1

        print(f"Total comments found: {comment_counter}")
        print(f"URL_ID - {url_counter}")
        print(f"Total authors found: {comment_authors_counter}")

        url_counter += 1

    except Exception as e:
        print(f"Error: {str(e)}")

# Quit the web driver
driver.quit()

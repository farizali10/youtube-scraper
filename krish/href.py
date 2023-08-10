from slow_scroll_func import slow_scroll_to_end
from url_driver import driver

def get_url(url_list,yt_url):
    driver.get(yt_url)
    slow_scroll_to_end(driver)

    urls = driver.find_elements_by_css_selector("a.yt-simple-endpoint.focus-on-expand.style-scope.ytd-rich-grid-media")
    print(f"Total videos available: {len(urls)}")

    url_counter = 0

    for url in urls:
        try:
            href = url.get_attribute("href")  # Extract the href attribute
            url_list.append(href)
            print(url_counter + 1, ".", "URL:", href)
            url_counter += 1

        except Exception as e:
            print("Error occurred:", str(e))  # Print any error messages during execution

    print(f"Total urls available: {url_counter}")
    print(f"Total urls not available: Fetched({len(urls)}) - Retrieved({url_counter}) = {len(urls) - url_counter}")
   

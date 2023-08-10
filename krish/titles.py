from slow_scroll_func import slow_scroll_to_end
from url_driver import driver

yt_url = "https://www.youtube.com/@krishnaik06/videos"
driver.get(yt_url)
slow_scroll_to_end(driver)

def get_titles():
    titles = driver.find_elements_by_css_selector("a.yt-simple-endpoint.focus-on-expand.style-scope.ytd-rich-grid-media")
    print(f"Total videos available: {len(titles)}")

    title_counter = 0

    for title in titles:
        try:
            if title.text.strip():  # Skip empty titles
                print(title_counter+1, ".", title.text)
                title_counter += 1

        except Exception as e:
            print("Error occurred:", str(e))  # Print any error messages during execution

    driver.quit()

    print(f"Total titles available: {title_counter}")
    print(f"Total titles not available: Fetched({len(titles)}) - Retrieved({title_counter}) = {len(titles) - title_counter}")

get_titles()










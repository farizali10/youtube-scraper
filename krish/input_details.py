from slow_scroll_func import slow_scroll_to_end
from url_driver import driver
from title import get_titles

yt_url = "https://www.youtube.com/@krishnaik06/videos"
driver.get(yt_url)
slow_scroll_to_end(driver)

videos = driver.find_elements_by_css_selector("ytd-rich-item-renderer.style-scope.ytd-rich-grid-row")
print(f"Total videos available: {len(videos)}")

title_counter = 0

for video in videos:
    try:
        if video.find_elements_by_css_selector("a.yt-simple-endpoint.focus-on-expand.style-scope.ytd-rich-grid-media"):
            urls = video.find_elements_by_css_selector("a.yt-simple-endpoint.focus-on-expand.style-scope.ytd-rich-grid-media")
        else:
            urls = "URL Not Available"
        
        if video.find_elements_by_css_selector("yt-formatted-string.style-scope.ytd-rich-grid-media"):
            titles = video.find_elements_by_css_selector("yt-formatted-string.style-scope.ytd-rich-grid-media")
        else:
            titles = "Title Not Available"

        if video.find_elements_by_css_selector("span.inline-metadata-item.style-scope.ytd-video-meta-block"):
            views = video.find_elements_by_css_selector("span.inline-metadata-item.style-scope.ytd-video-meta-block")
        else:
            views = "Views Not Available"

        href = urls.get_attribute("href")  # Extract the href attribute
        print(title_counter + 1, ".", titles.text, "Total Views:", views.text, "URL:", href)

        title_counter += 1

    except Exception as e:
        print("Error occurred:", str(e))  # Print any error messages during execution

driver.quit()

print(f"Total titles available: {title_counter}")
print(f"Total titles not available: Fetched({len(videos)}) - Retrieved({title_counter}) = {len(videos) - title_counter}")







#for i in range(len(urls)):
#    url = urls[i]
#    title = titles[i]
#    view = views[i]
# Finding out how many videos are uplaoded
from slow_scroll_func import slow_scroll_to_end
from url_driver import driver

yt_url = "https://www.youtube.com/@krishnaik06/about"

driver.get(yt_url)
slow_scroll_to_end(driver)

counter = 0

about = driver.find_elements_by_css_selector("yt-formatted-string.style-scope.ytd-c4-tabbed-header-renderer")

for video_count in about:
    counter = counter + 1
    if counter == 5:
        print(video_count.text)

driver.quit()

# inline-metadata-item style-scope ytd-video-meta-block
# inline-metadata-item.style-scope.ytd-video-meta-block
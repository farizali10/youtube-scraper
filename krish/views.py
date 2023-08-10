from slow_scroll_func import slow_scroll_to_end
from url_driver import driver

yt_url = "https://www.youtube.com/@krishnaik06/videos"
driver.get(yt_url)
slow_scroll_to_end(driver)


views = driver.find_elements_by_css_selector("span.inline-metadata-item.style-scope.ytd-video-meta-block")
print(f"Total videos available: {len(views)}")

view_counter = 0

for i in range(0, len(views), 2):
    try:
        view = views[i]
        next_view = views[i+1] if i+1 < len(views) else None
        
        if view.text.strip():  # Skip empty views
            print(f"{view_counter+1}. {view.text} {next_view.text}")
            view_counter += 1

    except Exception as e:
        print("Error occurred:", str(e))

driver.quit()

print(f"Total views available: {view_counter}")
print(f"Total views not available: Fetched({len(views)}) - Retrieved({view_counter}) = {len(views) - view_counter}")


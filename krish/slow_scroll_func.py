import time

def slow_scroll_to_end(wd=None):
    """
    Function to scroll and wait across the webpage as per the need.
    """
    scroll_increment = 400  # Scroll size in pixels
    scroll_delay = 1 # Delay in seconds between scrolls

    # Get initial page height
    last_height = wd.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Scroll down to the bottom
        wd.execute_script(f"window.scrollTo(0, {last_height});")

        # Wait for the page to load
        time.sleep(scroll_delay)

        # Scroll down by the specified increment
        wd.execute_script(f"window.scrollBy(0, {scroll_increment});")

        # Wait for the page to load
        time.sleep(scroll_delay)

        # Calculate new scroll height and check if the page height has changed
        new_height = wd.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

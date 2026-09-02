"""Visits the deployed Streamlit app in a real headless browser so Streamlit
Community Cloud counts it as a visitor, and clicks the "wake this app back up"
button if the app has already gone to sleep. Run on a schedule by keepalive.yml.
"""

import re
import sys

from playwright.sync_api import sync_playwright

APP_URL = "https://portfolio-gokulnath.streamlit.app/"
WAKE_BUTTON_PATTERN = re.compile(r"(wake|get this app back up)", re.IGNORECASE)


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(APP_URL, wait_until="networkidle", timeout=60_000)

        wake_button = page.get_by_role("button", name=WAKE_BUTTON_PATTERN)
        if wake_button.count() > 0:
            print("App was asleep — clicking the wake-up button.")
            wake_button.first.click()
            page.wait_for_timeout(45_000)  # give the app time to cold-start
        else:
            print("App was already awake.")

        # Give the underlying Streamlit session a moment to fully establish
        # before we close the tab, so the visit registers as real activity.
        page.wait_for_timeout(5_000)
        browser.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 - this is a best-effort ping job
        print(f"Keep-alive ping failed: {exc}", file=sys.stderr)
        sys.exit(1)

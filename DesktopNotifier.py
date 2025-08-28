import time
import notify2
from topnews import topStories

ICON_PATH = None  # e.g., "/usr/share/icons/hicolor/48x48/apps/news.png"

NOTIFY_INTERVAL = 15


def show_news_notifications():
    try:
        newsitems = topStories()
        if not newsitems:
            print("⚠️ No news items found.")
            return
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return

    notify2.init("News Notifier")

    n = notify2.Notification("News Notifier", icon=ICON_PATH)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(10000)  # 10 seconds

    for item in newsitems:
        title = item.get("title", "No Title")
        description = item.get("description", "No Description")

        n.update(title, description)
        n.show()

        time.sleep(NOTIFY_INTERVAL)


if __name__ == "__main__":
    show_news_notifications()

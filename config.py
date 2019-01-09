from collections import namedtuple

SITE_TITLE = "K Jay Miller"
SITE_SUBTITLE = "The Corner of Automation, Productivity, and Community"
SITE_URL = "https://kjaymiller.com"
AUTHOR = 'KJAYMILLER'
REGION = 'US/Pacific'
CONTENT_PATH = 'content'
OUTPUT_PATH = 'output'
STATIC_PATH = 'static'

# Header Links
Link = namedtuple('Link', ['title', 'href'])
HEADER_LINKS = (
    Link('Blog', '/blog_posts_0.html'),
    Link('Newsletter', '/pages/subscribe.html'),
    Link('Contact','/pages/contact.html'),
    Link('PIT', 'https://productivityintech.com'),
)

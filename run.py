import feedparser
import logging
from render_engine import Site, Page, Collection
from render_engine.blog import Blog
from render_engine.microblog import MicroBlog
from render_engine.links import Link
from render_engine.search import Fuse

def get_latest_post(rss_feed):
    f = feedparser.parse(rss_feed)
    latest_post = sorted(f['entries'], key=lambda x:x['published_parsed'])[-1]
    return {
            'title': latest_post['title'],
            'link': latest_post['link'],
            }

class PodcastLink(Link):
    def __init__(self, name, url, image, feed):
        super().__init__(name=name, url=url, image=image)
        self.latest_post = get_latest_post(feed)


class site(Site):
    strict = True
    HEADER_LINKS = (
        Link(name='About', url='/about.html'),
        Link(name='Blog', url='/blog-0.html'),
        Link(name='Projects', url='/projects.html'),
        Link(name='Resume', url='/static/files/Jay_Miller_-_Software_Engineer.pdf'),
        Link(name='Newsletter', url='/subscribe'),
        Link(name='Contact', url="/contact"),
        )

    timezone = 'US/Pacific'
    SITE_TITLE = '(K) Jay Miller'
    SITE_URL = 'https://kjaymiller.com'
    AUTHOR = 'Jay Miller'
    HEADER_LINKS = HEADER_LINKS
    PODCASTS = [
            PodcastLink(
                name="Bob's Taverncast",
                url='https://bobstavern.pub',
                image="https://kjaymiller.s3-us-west-2.amazonaws.com/images/bobstavern_256.jpg",
                feed='https://feeds.transistor.fm/bobs-taverncast-a-hearthstone-battlegrounds-podcast',
                ),
            PodcastLink(name="PIT Podcast", url='https://podcast.productivityintech.com',
                image="https://s3-us-west-2.amazonaws.com/kjaymiller/images/pit-logo-v4.jpg",
                feed='https://feeds.transistor.fm/productivity-in-tech-podcast',
                ),

            PodcastLink(name="TekTok Podcast", url='https://www.tekside.net/tektok',
                image="https://kjaymiller.s3-us-west-2.amazonaws.com/images/tektok_256.jpeg",
                feed='http://tekside.net/tektok?format=rss'),
                ]
    search = Fuse


mysite = site()
@mysite.register_collection
class Pages(Collection):
    routes = ["", "pages"]
    content_path = "content/pages"
    template = "page.html"

@mysite.register_collection
class Blog(Blog):
    routes = ['', '/blog']
    template = 'blog.html'
    archive_template = '_archive.html'
    archive_slug = 'all_posts'
    content_path = 'content'
    subcollections = ['category', 'tags']
    paginated = True

@mysite.register_collection
class MicroBlog(MicroBlog):
    content_path = 'content/microblog'
    routes = ['/microblog']
    template = 'blog.html'
    archive_template = 'microblog_archive.html'
    archive_slug = 'all_microblog_posts'
    paginated = True

@mysite.register_route
class Index(Page):
    template = "index.html"
    slug = "index"
    no_index = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # logging.warning(mysite.collections['MicroBlog'].archive[0])
        # logging.warning(mysite.collections['Blog'].archive[0])
        self.microblog_posts = mysite.collections['MicroBlog'].archive[0].pages[:5]
        self.blog_posts = mysite.collections['Blog'].archive[0].pages[:5]


mysite.render(dry_run=False)

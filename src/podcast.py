from dataclasses import dataclass


@dataclass
class Podcast:
    podcast_title: str
    link_feed: str
    page_link: str
    description: str
    subtitle: str
    author_name: str
    author_email: str
    image_link: str

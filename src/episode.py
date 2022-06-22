from dataclasses import dataclass


@dataclass
class Episode:
    title: str
    link: str
    date: str
    description: str
    link_mp3: str
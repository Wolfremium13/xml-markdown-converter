
import xml.etree.ElementTree as ET
from markdownify import markdownify as md


from src.podcast import Podcast
from src.episode import Episode


class XMLToMarkdown:

    def parse(self, xml_path) -> str:
        content = self._read_file_content(xml_path)
        podcast = self._parse_xml_to_podcast(content)
        content_episodes = [p for p in content if p.tag == "item"]
        episodes = map(self._parse_xml_to_episode, content_episodes)
        return self._parse_to_markdown(podcast, episodes)

    def _read_file_content(self, xml_path):
        tree = ET.parse(xml_path)
        rss_tag = tree.getroot()
        channel_tag = rss_tag[0]
        return channel_tag

    def _parse_xml_to_podcast(self, content: ET.Element) -> Podcast:
        podcast = Podcast(
            podcast_title=content[0].text,
            link_feed=content[1].attrib["href"],
            page_link=content[2].text,
            description=content[3].text,
            subtitle=content[8].text,
            author_name=content[8].text,
            author_email=content[11][1].text,
            image_link=content[15][0].text
        )
        return podcast

    def _parse_xml_to_episode(self, content_episode: ET.Element) -> Episode:
        episode = Episode(
            title=content_episode[0].text,
            link=content_episode[1].text,
            date=content_episode[2].text,
            description=md(content_episode[5].text),
            link_mp3=content_episode[8].attrib["url"]
        )
        return episode

    def _parse_to_markdown(self, podcast: Podcast, episodes) -> str:
        # Watch out string are literals, take care with indentations
        result = ("---\n"
                  f"title: \"{podcast.podcast_title}\"\n"
                  f"feed_link: \"{podcast.link_feed}\"\n"
                  f"page_link: \"{podcast.page_link}\"\n"
                  f"description: \"{podcast.description}\"\n"
                  f"subtitle: \"{podcast.subtitle}\"\n"
                  f"author_name: \"{podcast.author_name}\"\n"
                  f"author_email: \"{podcast.author_email}\"\n"
                  f"image_link: \"{podcast.image_link}\"\n"
                  "episodes:\n")
        for episode in episodes:
            result += (f"  - title: \"{episode.title}\"\n"
                       f"    link: \"{episode.link}\"\n"
                       f"    date: \"{episode.date}\"\n"
                       f"    description: \"{episode.description}\"\n"
                       f"    link_mp3: \"{episode.link_mp3}\"\n")
        result += "---"
        return result

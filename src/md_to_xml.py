import os
import xml.etree.ElementTree as ET
from markdown import Markdown

from src.episode import Episode


class MarkdownToXML:

    def parse(self, folder_path: str, xml_template_path: str) -> ET.ElementTree:
        md_contents = self._read_files(folder_path)
        episodies = map(self._parse_text_to_episode, md_contents)
        return self._parse_xml_content(episodies, xml_template_path)

    def _read_files(self, folder_path: str) -> str:
        all_folder_files = os.listdir(folder_path)
        all_folder_files.sort(reverse=True)
        md_file_names = [f for f in all_folder_files if f
                         != "episodios.md"]  # Duplicated content
        md_paths = [f"{folder_path}{file_name}" for file_name in md_file_names]
        return map(self._extract_file_content, md_paths)

    def _extract_file_content(self, md_full_path: str) -> str:
        with open(md_full_path, 'r') as file:
            return file.read()

    def _parse_text_to_episode(self, content: str) -> Episode:
        md = Markdown(extensions=['meta'])
        html_content = md.convert(content)
        metadata = md.Meta
        last_phrase_after_description = "\n<h2>template: templates/episode.html</h2>\n"
        description = html_content.split(last_phrase_after_description)[1]
        episode = Episode(
            title=metadata.get('title')[0].replace("\"", ""),
            link=(
                f"https://savvily.es/podcasts/ni-cero-ni-uno"
                f"/episodios{metadata.get('slug')[0]}/"),
            date=metadata.get('publishedtext')[0],
            description=description,
            link_mp3=metadata.get('audiolink')[0]
        )
        return episode

    def _parse_xml_content(self, episodies, xml_template_path: str) -> str:
        # Watch out string are literals, take care with indentations
        self._register_all_namespaces(xml_template_path)
        template = ET.parse(xml_template_path)
        rss_tag = template.getroot()
        channel_tag = rss_tag[0]
        for episode in episodies:
            item = ET.fromstring("<item></item>")
            title = ET.fromstring(f"<title>{episode.title}</title>")
            item.append(title)
            link = ET.fromstring(f"<link>{episode.link}</link>")
            item.append(link)
            date = ET.fromstring(f"<pubDate>{episode.date}</pubDate>")
            item.append(date)
            guid = ET.fromstring(f"<guid isPermaLink=\"false\">{episode.link}</guid>")
            item.append(guid)
            enclosure = ET.fromstring(
                f"<enclosure url=\"{episode.link_mp3}\" type=\"audio/mpeg\"></enclosure>")
            item.append(enclosure)
            description = ET.fromstring(f"<description></description>")
            description.text = f"<![CDATA[{episode.description}]]>"
            item.append(description)
            duration = ET.Element("{http://www.itunes.com/dtds/podcast-1.0.dtd}duration")
            duration.text = "0:00"
            item.append(duration)
            channel_tag.append(item)
        ET.indent(template, space="\t", level=0)
        return template

    def _register_all_namespaces(self, xml_template_path: str):
        namespaces = dict([node for _, node in ET.iterparse(
            xml_template_path, events=['start-ns'])])
        for ns in namespaces:
            ET.register_namespace(ns, namespaces[ns])

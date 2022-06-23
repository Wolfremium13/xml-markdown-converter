

from src.md_to_xml import MarkdownToXML
from src.xml_to_md import XMLToMarkdown


if __name__ == "__main__":
    # Markdown to XML
    md_folder_path = "./data/podcasts/ni-cero-ni-uno/episodios/"
    xml_template_path = "./data/parse_to_xml_template.xml"
    xml = MarkdownToXML().parse(md_folder_path, xml_template_path)
    xml.write("./data/template_converted.xml", encoding="utf-8")

    # XML to Markdown function
    xml_path = './data/updated-xml-data.xml'
    markdown_parsed_content = XMLToMarkdown().parse(xml_path)

    output_file_name = 'markdown-converted'
    with open(f"./data/{output_file_name}.md", "w") as text_file:
        text_file.write(markdown_parsed_content)

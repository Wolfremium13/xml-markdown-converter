
from src.xml_to_md import XMLToMarkdown


if __name__ == "__main__":
    xml_path = './data/updated-xml-data.xml'
    markdown_parsed_content = XMLToMarkdown().parse(xml_path)

    output_file_name = 'markdown-converted'
    with open(f"./data/{output_file_name}.md", "w") as text_file:
        text_file.write(markdown_parsed_content)

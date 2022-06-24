# 🔖 Usage

## Requirements and context

Check /data folder contains `parse_to_xml_template.xml`, `/podcast` folder like
savvily and, `updated-xml-data.xml`.

> Right now we have straightforward code for Carlos Ble podcast and 0 tests,
> which is (for now) not a problem. You can change params in `__main__.py` inside `src`.

## XML > Markdown

Use `make update-xml` for update data from feed, it's saved on
`data/updated-xml-data.xml`. The code takes the xml data and saves all episodes
inside one markdown file, parsing html description into markdown. The output is
on `/data`.

## Markdown > XML

Copy podcast folder from savvily repository into `/data` and execute the code
using docker or the actual machine. This will take all files and parse the
content into a single xml file with spotify requirements. The output is on
`/data`.

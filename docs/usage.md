# 🔖 Usage

## Prerequisites

The easiest way to run this project is with Docker and the make command.

## Getting started

1. Build the Docker image with:

```
make build-image
```

2. Run docker container to convert all markdown episodes to xml file.

```
make run-image
```

3. The xml file generated should be `/data/template_converted.xml`. If the file 
`/data/template_converter.xml` was already created previously, it is recommended to delete it
and run the command `make run-image` when new episodes are added to the folder `data/podcasts/ni-cero-ni-uno/episodios`.

   
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

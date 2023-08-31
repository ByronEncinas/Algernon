# Algernon is a CLI/GUI app to manipulate data in different formats

## What this commit is implementing (this section is different in **all** commits)

    (this format just for now) $ python alger.py [ARGS] [FLAGS] ...

    - [x] When using Algernon the GUI.py file is called

    - [x] We will make it so that 

    > $ python alger.py non 

        +------------------+
        |                  |                    
        |    GUI Window    |
        |                  |
        +------------------+ 

    > $ python alger.py 
          o_o
         (_^_) ( °)>   
               |   U
               (__ )    


    displays in the terminal a message with those two little animals


## Table of Contents
  
  - [Pip Installation](#pip)
  - [Parser & Visuals](#parser-&-visuals)
  - [Commands CLI Algernon](#cli-commands)
  - [Usage GUI Algernon](#gui-usage)

## Pip (production)

Algernon will be planned to be released as a pip package.

> pip install algernon

## Parser & Visuals

Algernon will count with the functionality of visualization of ASCII, JSON, XML, TOML, YAML, CSV with graphic interfaces: diagrams, arrows and even datatables.

**Example JSON**

    {
        "name": "Soup",
        "ingredients": [
            {
                "ingredientName": "Water",
                "requiredAmount": 1
            },
            {
                "ingredientName": "Potatoes",
                "requiredAmount": 4
            }
        ]
    }

**Example XML**

    <recipe>
        <name>Soup</name>
        <ingredients>
            <ingredient>
                <ingredientName>Water</ingredientName>
                <requiredAmount>1</requiredAmount>
            </ingredient>
            <ingredient>
                <ingredientName>Potatoes</ingredientName>
                <requiredAmount>4</requiredAmount>
            </ingredient>
        </ingredients>
    </recipe>

**Example YAML**

    name: Soup
    ingredients:
      - ingredientName: Water
        requiredAmount: 1
      - ingredientName: Potatoes
        requiredAmount: 4


**Example TOML**

    name = "Soup"

    [[ingredients]]
    ingredientName = "Water"
    requiredAmount = 1

    [[ingredients]]
    ingredientName = "Potatoes"
    requiredAmount = 4

## Crystallographic convertion of data

Due to some interest in taking a more scientific use of this, we will add a set of instructions to convert from XYZ format to CIF. This feature remains pending.

## Commands CLI Algernon

## Usage GUI Algernon

<!-- From here on this is just ideas 

## Data Manipulation

- [visidata](https://github.com/saulpw/visidata) - Spreadsheet multitool for data discovery and arrangement.

### Processors

- [jq](https://github.com/stedolan/jq) - JSON processor.
- [yq](https://github.com/kislyuk/yq) - YAML processor.
- [dasel](https://github.com/tomwright/dasel) - JSON/YAML/TOML/XML processor (like jq/yq).
- [yaml-cli](https://github.com/pandastrike/yaml-cli) - Query/update YAML.
- [ramda-cli](https://github.com/raine/ramda-cli) - Process data with functional pipelines.
- [xq](https://github.com/sibprogrammer/xq) - XML and HTML beautifier and content extractor.

### JSON

- [jp](https://github.com/therealklanni/jp) - JSON parser.
- [fx](https://github.com/antonmedv/fx) - Command-line JSON viewer.
- [vj](https://github.com/busyloop/vj) - Makes JSON human readable.
- [underscore-cli](https://github.com/ddopson/underscore-cli) - Utility-belt for hacking JSON and Javascript.
- [strip-json-comments-cli](https://github.com/sindresorhus/strip-json-comments-cli) - Strip comments from JSON.
- [GROQ](https://github.com/sanity-io/groq-cli) – JSON processor with queries and projections.
- [gron](https://github.com/tomnomnom/gron) - Make JSON greppable.

### YAML

- [dyff](https://github.com/homeport/dyff) - YAML diff tool.

### Columns

- [parse-columns-cli](https://github.com/sindresorhus/parse-columns-cli) - Parse text columns to JSON.
- [q](http://harelba.github.io/q/) - Execution of SQL-like queries on CSV/TSV/tabular text file.

### Text

- [figlet](http://www.figlet.org/) - Creates large text out of ASCII characters.
- [stegcloak](https://github.com/kurolabs/stegcloak) - Hide secrets with invisible characters in plain text securely.

-->

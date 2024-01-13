import pandas as pd
import os

# Read the CSV file
csv_file_path = 'Layout.csv'  # Replace with your CSV file path
data = pd.read_csv(csv_file_path)
file_path = "XML"

for index, row in data.iterrows():
    file_name = row['File']
    id_value = row['ID']
    layout_value = row['Layout']

    # Open the corresponding file
    text_file_path = os.path.join('XML', file_name)  # Folder containing text files
    with open(text_file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

        # Find the ID value and insert TAGREFS attribute with Layout value
        modified_content = text_content.replace(f'ID="{id_value}"', f'ID="{id_value}" TAGREFS="{layout_value}"')

    # Write the modified content back to the text file
    with open(text_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

for fname in os.listdir(file_path):
    print(fname)
    xml_file_path = file_path + "/" + fname
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        tag_content = file.read()

        # Find the ID value and insert TAGREFS attribute with Layout value
        tag_values = tag_content.replace(f'</Styles>', f'</Styles>\n <Tags>\n    <LayoutTag ID="LAYOUT_TAG_001" LABEL="Heading"/>\n    <LayoutTag ID="LAYOUT_TAG_002" LABEL="Textblock"/>\n    <LayoutTag ID="LAYOUT_TAG_003" LABEL="Illustration"/>\n    <LayoutTag ID="LAYOUT_TAG_004" LABEL="Caption"/>\n    <LayoutTag ID="LAYOUT_TAG_005" LABEL="Author"/>\n    <LayoutTag ID="LAYOUT_TAG_006" LABEL="Advertisement"/>\n    <LayoutTag ID="LAYOUT_TAG_007" LABEL="Table"/>\n </Tags> ')

    # Write the modified content back to the text file
    with open(xml_file_path, 'w', encoding='utf-8') as file:
        file.write(tag_values)


print("Text files updated successfully!")

import os
import re

# Define the directory path where your files are located
directory_path = "XML"  # Change this to your folder path containing the files

processed_files = set()

find1 = "1" #90%
find2 = "2" #80%
find3 = "3" #70%
find4 = "4" #60%
find5 = "5" #50%
find6 = "6" #40%
find7 = "7" #30%
find8 = "8" #20%
find9 = "9" #10%

repl1 = "1"
repl2 = "2"
repl3 = "3"
repl4 = "4"
repl5 = "5"
repl6 = "6"
repl7 = "7"
repl8 = "8"
repl9 = "9"
repl0 = "0"


# Check if the directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the item is a file
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding as 'utf-8'
                file_content = file.read()

                # Define a regular expression pattern to match the CC attribute inside String tags
                cc_pattern = r'(CC=")(\d+)(")'

                # Replace each digit in the CC attribute with a required value
                modified_content = re.sub(cc_pattern, lambda match: match.group(1) + match.group(2).replace(find1, repl0).replace(find2, repl0).replace(find3, repl0).replace(find4, repl1).replace(find5, repl1).replace(find6, repl2).replace(find7, repl2).replace(find8, repl3).replace(find9, repl4) + match.group(3), file_content)

                # Write modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as modified_file:  # Use 'utf-8' encoding for writing
                    modified_file.write(modified_content)

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the item is a file
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

                # Define a regular expression pattern to match the String tags and CC attribute
                string_pattern = r'(WC=")(\d*\.\d+)("\s+CC=")(\d+)'

                # Find all matches of the String tags with WC and CC attributes
                string_matches = re.findall(string_pattern, file_content)
                modified_content = file_content

                # Calculate total number of digits and sum
                for match in string_matches:
                    wc_value = float(match[1])
                    cc_digits = [10 - int(digit) for digit in match[3]]
                    avg = (sum(cc_digits) / len(cc_digits)) / 10
                    #print(cc_digits)
                    #print(avg)

                    modified_content = re.sub(string_pattern, lambda m: f'WC="{avg:.2f}{m.group(3)}{m.group(4)}' if m.group(4) == match[3] else m.group(0), modified_content)

                    # Write modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as modified_file:
                    modified_file.write(modified_content)
                    print(f"Updated WC attribute in {filename} with average value")


    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the item is a file
        if os.path.isfile(file_path) and filename not in processed_files:
            total_wc = 0
            wc_count = 0

            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

                # Define a regular expression pattern to match the WC attribute
                wc_pattern = r'WC="([\d.]+)"'

                # Find all matches of the WC attribute
                wc_matches = re.findall(wc_pattern, file_content)
                #print(wc_matches)

                # Calculate total sum of WC attribute values

                for wc_value1 in wc_matches:
                    total_wc += float(wc_value1)
                    #print(total_wc)
                    wc_count += 1

                if wc_count > 0:
                    average_wc = total_wc / wc_count

                    # Calculate ACCURACY and PC values
                    accuracy = average_wc * 100  # Multiply by 100 for percentage value
                    pc = average_wc  # PC value is the same as average WC value
                    #print(accuracy)
                    #print(pc)

                    # Iterate through files again to update ACCURACY and PC attributes
                    #for filename in os.listdir(directory_path):
                    #file_path = os.path.join(directory_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                       main_xml_content = file.read()
                       main_xml_content = re.sub(r'(ACCURACY=")([^"]+)(")', f'ACCURACY="{accuracy:.2f}"', main_xml_content)
                       main_xml_content = re.sub(r'(PC=")([^"]+)(")', f'PC="{pc:.6f}"', main_xml_content)

                    with open(file_path, 'w', encoding='utf-8') as modified_file:
                       modified_file.write(main_xml_content)
                       print(f"Updated ACCURACY and PC attributes in {file_path}")
            processed_files.add(filename)

    if wc_count == 0:
        print("No WC attributes found in the files.")


else:
    print(f"The directory '{directory_path}' does not exist or is not a directory.")



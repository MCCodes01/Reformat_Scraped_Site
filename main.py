def reformat_text(input_file, output_file):
    try:
        # Feedback: Start processing
        print("Starting the reformatting process...")

        # Read the content of the input file
        print(f"Reading from {input_file}...")
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        print("File read successfully.")

        # Replace multiple spaces with a single space
        print("Replacing multiple spaces with a single space...")
        text = ' '.join(text.split())
        print("Spaces replaced.")

        # Add a double line break after periods to create paragraphs
        print("Adding double line breaks after periods...")
        text = text.replace('. ', '.\n\n')

        # Add a double line break after question marks and exclamation marks
        print("Adding double line breaks after question marks and exclamation marks...")
        text = text.replace('? ', '?\n\n')
        text = text.replace('! ', '!\n\n')

        # Optionally, reformat headings if needed
        print("Reformatting headings, if any...")
        text = text.replace(': ', ':\n\n')

        # Write the reformatted text to the output file
        print(f"Writing reformatted text to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text has been successfully reformatted and saved to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

#Usage
input_file = "scraped_text.txt"
output_file = "reformatted_text.txt"
reformat_text(input_file, output_file)


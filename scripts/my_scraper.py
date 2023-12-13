import os
import subprocess

# Step 1: Generate a list of composers (Assuming you already have the list)
try:
    # Run get_people_page_urls.py and capture its output into the "Composers" list
    result = subprocess.run(["python", "get_people_page_urls.py"], stdout=subprocess.PIPE, text=True)
    Composers = result.stdout.strip().split('\n')
except Exception as e:
    print(f"Error running get_people_page_urls.py: {e}")
    Composers = []

# Step 2: Create a loop to run get_pdf.py for each composer
output_folder = "MusicScoreData"

for composer in Composers:
    # Create a directory for the composer's PDFs
    composer_folder = os.path.join(output_folder, composer)
    os.makedirs(composer_folder, exist_ok=True)

    # Run get_pdf.py on the composer
    subprocess.run(["python", "get_pdf.py", composer, composer_folder])
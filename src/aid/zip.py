import zipfile
import os

def unpack_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f'Unpacked {zip_path} to {extract_to_directory}')
    except Exception as e:
        print(f'An error occurred while unpacking {zip_path}: {e}')

zip_files_directory = os.path.join('.', 'data', 'zip_files')
extract_to_directory = os.path.join('.', 'data', 'zip_files', 'extracted_files')

# Ensure the extract_to_directory exists
if not os.path.exists(extract_to_directory):
    os.makedirs(extract_to_directory)

print('Unpacking zip files...')
for zip_file in os.listdir(zip_files_directory):
    if zip_file.endswith('.zip'):
        zip_path = os.path.join(zip_files_directory, zip_file)
        print(f'Unpacking {zip_path}...')
        unpack_zip(zip_path, extract_to_directory)
print('Done unpacking zip files.')
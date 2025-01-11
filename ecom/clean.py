with open('C:/Github/E-commerce-Website-using-Django/ecom/data.json', 'rb') as file:
    content = file.read()

# Remove BOM if present
if content.startswith(b'\xef\xbb\xbf'):
    content = content[3:]

# Save the file back without BOM
with open('db_backup_clean.json', 'wb') as file:
    file.write(content)

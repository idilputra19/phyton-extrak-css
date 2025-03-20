import re
import os
from bs4 import BeautifulSoup

# Folder berisi file HTML
html_folder = 'C:\\Users\\idilp\\Downloads\\dll\\spmb2025'  # Ruta absoluta que veo en tu terminal
output_css_file = 'main.css'

# Inisialisasi string untuk menyimpan CSS gabungan
combined_css = ''
css_sections = {}

def extract_css_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    style_tags = soup.find_all('style')
    
    css_content = ''
    for style_tag in style_tags:
        css_content += style_tag.string + '\n\n'
    
    return css_content

def replace_css_with_link(file_path, css_link):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    style_tags = soup.find_all('style')
    
    for style_tag in style_tags:
        style_tag.decompose()
    
    head_tag = soup.find('head')
    link_tag = soup.new_tag('link')
    link_tag['rel'] = 'stylesheet'
    link_tag['href'] = css_link
    head_tag.append(link_tag)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

def normalize_css(css_content, filename):
    # Tambahkan komentar untuk menunjukkan asal CSS
    return f'/* CSS from {filename} */\n{css_content}\n\n'

# Proses setiap file HTML
for filename in os.listdir(html_folder):
    if filename.endswith('.html'):
        file_path = os.path.join(html_folder, filename)
        css_content = extract_css_from_html(file_path)
        
        if css_content:
            css_sections[filename] = css_content
            normalized_css = normalize_css(css_content, filename)
            combined_css += normalized_css
            
            # Ganti tag style dengan link ke CSS eksternal
            replace_css_with_link(file_path, output_css_file)

# Tulis CSS gabungan ke file
with open(os.path.join(html_folder, output_css_file), 'w', encoding='utf-8') as file:
    file.write('/* Combined CSS for PPDB Online Kota Solok 2025 */\n\n')
    file.write(combined_css)

print("CSS has been successfully extracted and combined into " + output_css_file)
print("Style tags in HTML files have been replaced with links to " + output_css_file)


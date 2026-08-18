import os

search_dir = "/Users/andreadepolis/Documents/My_Website"

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(('.html', '.xml', '.json', '.yml')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            new_content = new_content.replace('>Policy Notes &amp; Op-Eds</a>', '>Policy &amp; Op-Eds</a>')
            new_content = new_content.replace('>Policy Notes &amp; Op-Eds</span></a>', '>Policy &amp; Op-Eds</span></a>')
            new_content = new_content.replace('>Policy Notes &amp; Op-Eds</span>', '>Policy &amp; Op-Eds</span>')
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")

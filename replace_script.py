import os
import glob
import re

search_dir = "/Users/andreadepolis/Documents/My_Website"

# regex patterns
ivan_pattern = re.compile(r'https://(sites\.google\.com/a/ivanpetrella\.com/www/?|ivanpetrella\.github\.io/?|sites\.google\.com/view/ivanpetrella/home\?authuser=0)')
new_ivan = "https://sites.google.com/view/ivanpetrella/home/"

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(('.html', '.xml', '.json', '.yml')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = ivan_pattern.sub(new_ivan, content)
            
            # also replace Policy Work in top menu. In HTML, the top menu has:
            # <li><a href="policy-work.html">Policy Work</a></li> or similar.
            # I will just replace ">Policy Work</a></li>" with ">Policy Notes &amp; Op-Eds</a></li>"
            new_content = new_content.replace('>Policy Work</a>', '>Policy Notes &amp; Op-Eds</a>')
            
            # and maybe the dropdown: <span>Policy Work</span>
            new_content = new_content.replace('>Policy Work</span></a>', '>Policy Notes &amp; Op-Eds</span></a>')
            new_content = new_content.replace('>Policy Work</span>', '>Policy Notes &amp; Op-Eds</span>')
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")

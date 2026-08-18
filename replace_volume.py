import os

search_dir = "/Users/andreadepolis/Documents/My_Website"

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            new_content = new_content.replace(
                'Journal of Business &amp; Economic Statistics, Vol. 42, No. 3 (2024)',
                'Journal of Business &amp; Economic Statistics, Vol. 42, No. 3, 1010–1025 (2024)'
            )
            new_content = new_content.replace(
                'Economics Letters, Vol. 267 (2026)',
                'Economics Letters, Vol. 267, 113096 (2026)'
            )
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")

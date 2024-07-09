import os
import markdown

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def compile_content():
    content = "# Repository Content\n\n"
    
    # Compile repository files
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'wiki' in root or '.github' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                content += f"## {file_path}\n\n"
                content += get_file_content(file_path) + "\n\n"
    
    # Compile wiki pages
    if os.path.exists('wiki'):
        content += "# Wiki Content\n\n"
        for root, dirs, files in os.walk('wiki'):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    content += f"## {os.path.splitext(file)[0]}\n\n"
                    content += get_file_content(file_path) + "\n\n"
    
    # Write compiled content to file
    with open('GenerativeAI/compiled_content.md', 'w') as f:
        f.write(content)

if __name__ == "__main__":
    compile_content()

import os

EXCLUDE_DIRS = {
    'venv', 'logs', '.nonadmin', 'conda-meta', '.git', 
    '.ebextensions', '.vscode', '__pycache__', 'catboost_info', 
    'mlproject.egg-info'
}
TEMPLATES_DIR = 'templates'
TEMPLATES_EXTENSIONS = {'.html'}

def print_tree(root, prefix=''):
    try:
        entries = [e for e in os.listdir(root) if e not in EXCLUDE_DIRS]
    except FileNotFoundError:
        return

    entries.sort()
    for i, entry in enumerate(entries):
        path = os.path.join(root, entry)
        connector = '`-- ' if i == len(entries) - 1 else '|-- '

        if os.path.isdir(path):
            print(prefix + connector + entry)
            print_tree(path, prefix + ('    ' if i == len(entries) - 1 else '|   '))
        else:
            ext = os.path.splitext(entry)[1].lower()
            # Show only .html files inside templates, all files elsewhere
            if os.path.normpath(root).endswith(TEMPLATES_DIR):
                if ext in TEMPLATES_EXTENSIONS:
                    print(prefix + connector + entry)
            else:
                print(prefix + connector + entry)

if __name__ == "__main__":
    root_dir = '.'  # Adjust if needed
    print_tree(root_dir)

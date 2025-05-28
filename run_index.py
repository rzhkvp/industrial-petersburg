import webbrowser
import sys

def open_in_codespaces(owner: str, repo: str) -> None:
   
    # Формируем URL для создания нового Codespace
    url = f"https://github.com/codespaces/new?repo={owner}/{repo}"
    print(f"Opening GitHub Codespace: {url}")
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python open_codespace.py <owner> <repo>")
        sys.exit(1)

    owner, repo = sys.argv[1], sys.argv[2]
    open_in_codespaces(owner, repo)

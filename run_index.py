import webbrowser
import sys

def open_in_github_dev(owner: str, repo: str, branch: str = "main") -> None:
    """
    Формирует ссылку для открытия файла index.html в github.dev (веб-редакторе).
    """
    # Формируем URL для открытия веб-редактора с файлом index.html
    url = f"https://github.dev/{owner}/{repo}/blob/{branch}/index.html"
    print(f"Opening GitHub.dev editor: {url}")
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    # Предполагаем, что запускают так: python open_github_dev.py <owner> <repo> [branch]
    if len(sys.argv) not in (3, 4):
        print("Использование: python open_github_dev.py <owner> <repo> [branch]")
        sys.exit(1)

    owner, repo = sys.argv[1], sys.argv[2]
    branch = sys.argv[3] if len(sys.argv) == 4 else "main"
    open_in_github_dev(owner, repo, branch)

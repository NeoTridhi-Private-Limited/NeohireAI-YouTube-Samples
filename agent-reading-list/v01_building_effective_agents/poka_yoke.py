# Poka-yoke for tools: make the mistake impossible, not just unlikely

def read_file(path: str) -> str:
    """Read a file. path MUST be absolute, e.g. /repo/src/app.py"""
    if not path.startswith("/"):
        return f"ERROR: '{path}' is relative. Pass an absolute path."
    return f"(contents of {path})"

print(read_file("src/app.py"))
print(read_file("/repo/src/app.py"))

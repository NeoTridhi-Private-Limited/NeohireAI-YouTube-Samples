# A tiny secret scanner that runs before every commit
import re

RULES = {
    "AWS access key": r"AKIA[0-9A-Z]{16}",
    "private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "password": r"(?i)password\s*=\s*['\"][^'\"]{6,}",
}
diff = """+ DB_HOST = "db.school.example.com"
+ password = "Summer@2026"
+ aws_key = "AKIAIOSFODNN7EXAMPLE"
+ password = os.environ["DB_PASSWORD"]"""

for no, line in enumerate(diff.splitlines(), 1):
    hits = [name for name, rx in RULES.items() if re.search(rx, line)]
    print(f"line {no}: {'BLOCK  ' + ', '.join(hits) if hits else 'ok'}")

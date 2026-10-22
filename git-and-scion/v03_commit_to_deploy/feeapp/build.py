"""Build step: pack the app into dist/feeapp.zip."""
import os
import zipfile

os.makedirs("dist", exist_ok=True)
with zipfile.ZipFile("dist/feeapp.zip", "w") as z:
    z.write("fee.py")
print("built dist/feeapp.zip")

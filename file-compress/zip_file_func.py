import zipfile
import pathlib

def make_archive(filepaths , dest_dir ,filename):
    # dest_path = pathlib.Path(dest_dir  "compressed.zip")
    dest_path = pathlib.Path(dest_dir) / f"{filename}.zip"
    with zipfile.ZipFile(dest_path,'w' ) as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["a1.py", "b1.py"], dest_dir="dest")
    
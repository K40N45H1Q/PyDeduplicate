from hashlib import md5
from sys import argv, exit
from getpass import getpass
from os import path, listdir, remove, system, name

class Deduplicator:
    def __init__(self):
        try:
            cache = {}
            if len(argv) == 2 and path.isdir(argv[1]):
                directory = argv[1]
                targets = listdir(directory)
                if targets:
                    for target in targets:
                        _path = path.join(directory, target)
                        if path.isfile(_path):
                            with open(_path, "rb") as file:
                                file_hash = md5(file.read()).hexdigest()
                                cache.setdefault(file_hash, []).append(_path)
                    cache = {k: v for k, v in cache.items() if len(v) > 1}
                    for md5sum, paths in cache.items():
                        print(f"Found {len(paths)} duplicate files with the MD5 hash: {md5sum}")
                        if input("Do you want to delete the duplicates? (y/n): ").lower() == "y":
                            for _path in paths[1:]:
                                if _path != __file__:
                                    remove(_path)
                            print("Duplicates have been successfully deleted!")
                if not cache:
                    print("No duplicates were found in the target directory.")
            else:
                print("The target directory was not found!")
            if len(argv) == 1:
                print(f"Usage: {path.basename(__file__)} ~/path/to/directory")
        except KeyboardInterrupt: pass
        finally:
            getpass("Press any key to exit...")
            system("clear") if name != "nt" else system("cls"); exit(0)

if __name__ == "__main__":
    Deduplicator()
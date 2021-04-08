#!/usr/bin/python3

import os
import argparse

class DirectoryWalk:
    def __init__(self):
        """Ici, nous définissons les valeurs par défaut globales"""
        self.path = ''

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Analyser tous les fichiers magiques")
        parser.add_argument("path", help="Chemin d'accès au dossier")

        return parser.parse_args()

    def scan_path(self):
        with os.scandir(self.path) as iter_path:
            for entry in iter_path:
                print(entry.name)

    def main(self):
        args = self.get_args()
        self.path = args.path

        self.scan_path()


if __name__ == '__main__':
    walk_instance = DirectoryWalk()
    walk_instance.main()
    
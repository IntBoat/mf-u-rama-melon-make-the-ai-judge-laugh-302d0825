#!/usr/bin/env python3
"""Make the AI Judge Laugh (make.fun).

Writes the entry -- one original one-line text -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

ENTRY = 'Our printer only jams when someone important is watching, which is why IT calls it the most reliable performance review in the building.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()

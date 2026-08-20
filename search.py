#!/usr/bin/env python3

import os
import sys
from pathlib import Path


def search_file(file_path: str, word: str) -> None:
	"""Print lines containing word, including their line numbers."""
	try:
		with Path(file_path).open("r", encoding="utf-8") as file:
			found = False
			for line_number, line in enumerate(file, start=1):
				if word in line:
					print(f"{line_number}: {line}", end="")
					found = True

		if not found:
			print(f'No matches found for "{word}".')
	except FileNotFoundError:
		print(f"File not found: {file_path}")
	except OSError as error:
		print(f"Could not read file: {error}")


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"Usage: python3 {sys.argv[0]} <word>")
		sys.exit(1)

	file_path = os.environ.get("FILE_TO_TEST")
	if not file_path:
		print("Error: the FILE_TO_TEST environment variable is required")
		sys.exit(1)

	search_file(file_path, sys.argv[1])

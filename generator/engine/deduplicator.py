"""
Duplicate detection for generated cybersecurity programs.
"""

import hashlib
import json
from pathlib import Path


class ProgramDeduplicator:
    """Detect whether a generated program already exists."""

    def __init__(self, catalog_path):
        self.catalog_path = Path(catalog_path)
        self.catalog_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.catalog = self._load_catalog()

    def _load_catalog(self):
        """Load the program catalog."""

        if not self.catalog_path.exists():
            return {
                "programs": []
            }

        try:
            with self.catalog_path.open(
                "r",
                encoding="utf-8",
            ) as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError):
            return {
                "programs": []
            }

    @staticmethod
    def fingerprint(source):
        """Generate a SHA-256 fingerprint for source code."""

        normalized_source = source.strip()

        return hashlib.sha256(
            normalized_source.encode("utf-8")
        ).hexdigest()

    def exists(self, source):
        """Check whether the generated source already exists."""

        fingerprint = self.fingerprint(source)

        return any(
            program.get("fingerprint") == fingerprint
            for program in self.catalog["programs"]
        )

    def add(self, source, metadata=None):
        """Add a generated program to the catalog."""

        fingerprint = self.fingerprint(source)

        if self.exists(source):
            return False

        entry = {
            "fingerprint": fingerprint,
            "metadata": metadata or {},
        }

        self.catalog["programs"].append(entry)

        self._save_catalog()

        return True

    def _save_catalog(self):
        """Save the catalog to disk."""

        with self.catalog_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                self.catalog,
                file,
                indent=4,
            )
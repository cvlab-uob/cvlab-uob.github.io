from pathlib import Path
import re

BIB_PATH = Path("/Users/hjchang/Project/cvlab-uob.github.io/_bibliography/papers.bib")


def normalize_author_list(authors: str) -> str:
    parts = [a.strip() for a in authors.split(" and ")]
    normalized = []
    for name in parts:
        if not name or name.lower() == "others":
            normalized.append(name)
            continue
        if "," in name:
            bits = [b.strip() for b in name.split(",") if b.strip()]
            if len(bits) >= 2:
                last = bits[0]
                first = " ".join(bits[1:])
                normalized.append(f"{first} {last}".strip())
                continue
        normalized.append(name)
    return " and ".join(normalized)


def main() -> None:
    text = BIB_PATH.read_text()
    author_re = re.compile(r"(author\s*=\s*\{)(.*?)(\})", re.DOTALL)

    def repl(match: re.Match) -> str:
        prefix, authors, suffix = match.groups()
        return prefix + normalize_author_list(authors) + suffix

    BIB_PATH.write_text(author_re.sub(repl, text))


if __name__ == "__main__":
    main()

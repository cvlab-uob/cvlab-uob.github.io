from pathlib import Path
import re

BIB_PATH = Path("/Users/hjchang/Project/cvlab-uob.github.io/_bibliography/papers.bib")


def has_field(entry: str, field: str) -> bool:
    return re.search(r"\n\s*" + re.escape(field) + r"\s*=", entry) is not None


def is_arxiv_entry(entry: str) -> bool:
    lower = entry.lower()
    return bool(re.search(r"\n\s*journal\s*=\s*\{[^}]*arxiv[^}]*\}", lower)) or bool(
        re.search(r"\n\s*journal\s*=\s*\{[^}]*e-prints[^}]*\}", lower)
    )


def ensure_commas(entry: str) -> str:
    lines = entry.strip().split("\n")
    if lines[-1].strip() != "}":
        lines.append("}")
    field_idxs = [
        i
        for i, line in enumerate(lines)
        if "=" in line and not line.lstrip().startswith("@")
    ]
    last_field_idx = field_idxs[-1] if field_idxs else None
    for i in field_idxs:
        if i == last_field_idx:
            continue
        line = lines[i].rstrip()
        if not line.endswith(","):
            lines[i] = line + ","
    return "\n".join(lines)


def normalize_entry(entry: str) -> str:
    entry = entry.strip()
    if not entry.endswith("}"):
        entry += "\n}"

    insert_fields = []
    if not has_field(entry, "abbr"):
        insert_fields.append("  abbr = {},")
    if not has_field(entry, "img"):
        insert_fields.append("  img = {},")
    if not has_field(entry, "selected"):
        insert_fields.append("  selected = {false},")

    if insert_fields:
        if has_field(entry, "selected"):
            entry = re.sub(
                r"\n(\s*selected\s*=)",
                "\n" + "\n".join(insert_fields) + "\n\\1",
                entry,
                count=1,
            )
        else:
            entry = entry[:-1] + "\n" + "\n".join(insert_fields) + "\n}"

    if "supplementary" in entry.lower() and not has_field(entry, "supplementary"):
        entry = entry[:-1] + "\n  supplementary = {true},\n}"

    if is_arxiv_entry(entry) and not has_field(entry, "preprint"):
        entry = entry[:-1] + "\n  preprint = {true},\n}"

    return ensure_commas(entry)


def main() -> None:
    text = BIB_PATH.read_text()
    header, _, rest = text.partition("@")
    if not rest:
        raise SystemExit("No entries found")

    entries = [e for e in re.split(r"(?=@\w+\{)", "@" + rest) if e.strip()]
    normalized = [normalize_entry(e) for e in entries]
    new_text = header.strip() + "\n" + "\n\n".join(normalized) + "\n"
    BIB_PATH.write_text(new_text)


if __name__ == "__main__":
    main()

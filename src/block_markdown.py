from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered list"
    OL = "ordered list"


def markdown_to_blocks(md):
    blocks = []
    parts = md.split("\n\n")
    for part in parts:
        if part == "":
            continue
        stripped = part.strip()
        blocks.append(stripped)
    return blocks


def block_to_block_type(md):
    if md.startswith("```") and md.endswith("```"):
        return BlockType.CODE
    elif md.startswith("#"):
        count = 0
        for ch in md:
            if ch == "#" and count < 6:
                count += 1
            elif ch == " " and 1 <= count <= 6:
                return BlockType.HEADING
            else:
                return BlockType.PARAGRAPH
    elif all(line.startswith(">") for line in md.splitlines()):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in md.splitlines()):
        return BlockType.UL
    elif md.startswith("1. "):
        lines = md.splitlines()
        count = 0
        for line in lines:
            count += 1
            if not line.startswith(f"{count}. "):
                return BlockType.PARAGRAPH
        return BlockType.OL
    else:
        return BlockType.PARAGRAPH

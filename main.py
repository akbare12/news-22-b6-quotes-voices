#!/usr/bin/env python3
"""Copy the entry image to /output/entry.png (stdlib only).

The image is drawn by draw.py and stored in this repository as entry.png.
This program copies it byte-for-byte and verifies size + sha256.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"
EXPECTED_SHA256 = "d9a14730fddad885f51fb27b21d999201117cf68cd47fc72e37f139f6f6136c0"
EXPECTED_BYTES = 194338


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    data = open(DST, "rb").read()
    assert len(data) == EXPECTED_BYTES, f"size mismatch: {len(data)}"
    digest = hashlib.sha256(data).hexdigest()
    assert digest == EXPECTED_SHA256, f"sha256 mismatch: {digest}"
    # Re-read the source and confirm the copy is identical to it.
    src_data = open(SRC, "rb").read()
    assert hashlib.sha256(src_data).hexdigest() == digest, "copy differs from source"
    print(f"wrote {DST} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()

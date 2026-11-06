# Source Provenance

This source subset was prepared on 2026-11-06 using independently stored local Forlinx ELF2 RTOS and accompanying HAL reference trees. Retained files were independently compared with the actual reference bytes. Local directory names alone are not provenance evidence.

| Layer | Evidence | Publication choice |
| --- | --- | --- |
| RT-Thread core | Version macros identify 4.1.1. Three core SHA256 fingerprints and the full same-path comparison match the local Forlinx ELF2 RTOS baseline. | Retain compared vendor source with documented release-preparation changes; exclude local additions. |
| Rockchip HAL | Compared separately with the HAL beside the same Forlinx package, originally referenced by an external symlink. Retained HAL files are compared with that actual reference. | Embed reviewed baseline HAL source and preserve its nested notices; omit restricted or unresolved payloads. |

The vendor references are local supplied package trees. This release does not attest to a pristine upstream tag, a vendor endorsement, or validated behavior on any target board.

The public file manifest uses repository-relative paths, SHA256 hashes, origin labels and available license evidence. A root license is not treated as blanket permission for unrelated third-party implementations. Exact private source locations, private diffs and scan findings are not part of this payload.

## Core Fingerprints

| Path | SHA256 |
| --- | --- |
| `include/rtdef.h` | `af53ca210865d859453f535397dfb36561f7d0d22078f683424715ba5269b57e` |
| `src/thread.c` | `aab2565bec5b27d8452e0a90d612552f44106b846a9b0314f862dedbde8f8622` |
| `src/scheduler.c` | `a76258a3a2df8c5dca4606715367b9c60d063df882ea61831583ccfe3efd4edd` |

## Manifest Interpretation

`PUBLIC_FILE_MANIFEST.csv` lists regular payload files and internal symlinks. The manifest itself is excluded from its own hash rows to avoid self-reference; the final Git commit and archive checksum bind that file as well. Original license texts and per-file notices remain authoritative.

Source-preparation modifications include portable path placeholders, explicit exclusion/disablement of unavailable optional packages, source-preserving Git attributes and public documentation. They are distinct from the removed private application changes. Existing vendor examples/default values and author attribution are retained where appropriate.

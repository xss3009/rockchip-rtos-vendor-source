# Source Preparation Checks

| Check | Result for this candidate |
| --- | --- |
| Independent source comparison | Read published Git blobs and actual local vendor RTOS/HAL reference files; classify byte-identical files and documented release-preparation differences. |
| Local application/board additions | Excluded, including the separately stored board/IOMUX references present in the initial source candidate. |
| Top-level applications | All 297 vendor files retained. |
| Top-level examples | All 242 vendor files retained. |
| Selected RK3568/RK3588 inputs | Required files present; selected Python/SCons source parses; no private entry-point/board references. |
| Literal shared Kconfig references | 52 checked, none missing. |
| Symlinks | Five retained relative links resolve inside the payload; no external link is shipped. |
| Case-sensitive paths | Original RK2108 `Image/` and `image/` configurations remain distinct. Use a case-sensitive filesystem. |
| Private application/deployment identifiers and credential signatures | No unresolved high-priority rule finding in the reviewed payload. This is a defined scan result, not a proof that all possible secrets can be detected. |
| Host-path examples | 156 files normalized to portable placeholders; copyrights and original author credit preserved. |
| Mixed licensing | Identified restricted or unresolved components omitted; file-specific/nested terms retained. No blanket root-license claim or universal linked-license compatibility claim. |
| Compilation, linking and FIT generation from real payloads | NOT RUN. |
| Board boot, UART/tick, shared transport and peripherals | NOT RUN. |

Coverage includes text paths, recognized user/deployment markers, token/private-key/URL-credential patterns, file types/hashes, and printable/selected UTF-16 binary metadata. Original RFC1918 sample addresses, public demonstration values and words used in ordinary documentation are reviewed as vendor examples rather than erased blindly.

Legacy utilities for unrelated BSPs retain their original language/version assumptions. Whole-tree Python parsing can flag original Python-2 or optional tools; the selected BSP input result above does not promise every utility works with the host Python version.

Some optional vendor examples reference omitted tools, libraries, firmware or assets. See `EXTERNAL_DEPENDENCIES.md` before building. This source collection is not a complete deployable Linux/RT system image.

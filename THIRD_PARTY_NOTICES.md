# Third-Party Notices and Redistribution Scope

The following table records component-level evidence found in the supplied source. File-specific notices and nested license files take precedence. This is not a declaration that every component has the same license, nor that every possible linked combination has been reviewed.

| Component | Evidence and applicable terms | Release treatment |
| --- | --- | --- |
| RT-Thread kernel and applicable original ports/components | Root `LICENSE` and per-file Apache-2.0 notices | Preserve `LICENSE`, `AUTHORS`, headers and original author credit. |
| Rockchip HAL | `bsp/rockchip/common/hal/LICENSE`; per-file BSD-3-Clause and nested notices | Source included; opaque utilities and unresolved optional algorithm dependencies omitted. |
| ARM CMSIS | `third_party/cmsis/LICENSE`, nested CMSIS licenses, and `bsp/rockchip/common/hal/lib/CMSIS/LICENSE.txt` | Preserve Apache-2.0 and file-specific BSD notices; do not infer rights to unrelated firmware. |
| RPMsg-Lite | `bsp/rockchip/common/drivers/rpmsg-lite/LICENSE` and HAL middleware license | BSD-3-Clause source and original rights holders retained. |
| OpenAMP and libmetal | File-level BSD notices under HAL middleware | Preserve original BSD attribution in each implementation. |
| FreeRTOS kernel | MIT text in `third_party/os/freertos/Source/tasks.c` and related kernel files | Kernel source retained; package membership does not relicense adaptation files with unclear terms. |
| Unity / tinymembench | Nested MIT licenses under HAL test / benchmark directories | Preserve full license text and author credit. |
| netutils | Package GPLv2 text and file-specific GPL-2.0-or-later, BSD or Apache notices | Retain mixed terms, including BSD netio and Apache TFTP source; no blanket relicensing. |
| Open Wi-Fi adapter source | Explicit GPL-2.0-or-later headers in AMPAK / Cypress adapter files | Retain only independently authorized adapter source. Required restricted wireless stack, headers, libraries and firmware are absent. |
| Build/check utilities and selected image descriptions | Kconfig-frontends `COPYING`, GPL file headers in checkpatch and selected HAL ITS templates | Source retained with GPL notices; precompiled vendor tools omitted. |
| CoreMark | Apache-2.0 source headers plus its nested trademark conditions | Preserve both source and trademark notices. No benchmark result is claimed by this release. |
| Other retained architecture/BSP libraries | Nested license texts and file-specific conditions | Original restrictions such as applicable hardware-use conditions remain in force. Retention is not a grant for unrelated hardware. |

## Omitted Components

The source candidate omits Cypress/Broadcom packages carrying proprietary or non-disclosure notices, unverified AMPAK binary libraries and NVRAM images, unresolved optional Bluetooth/adaptation source, vendor-only audio algorithm binaries, unidentified packaging executables, and embedded DSP/wireless firmware.

It also omits selected non-Rockchip BSPs containing confidential vendor SDK material or board files requiring a separate FSP agreement. Original vendor PDFs, software installers, binary archives and unverified font assets are not bundled. See the release scope and external-dependency list.

Examples of a `.c` or `.h` file containing an array converted from a firmware image are treated as firmware, not automatically as redistributable source.

## Distribution of Changes

The standalone preparation restores vendor baseline implementations where private business changes had been inserted, replaces original host-specific configuration examples where necessary, and disables optional packages whose implementation is absent. Preparation changes do not remove or replace original copyrights. Consult the provenance manifest for file hashes and origins.

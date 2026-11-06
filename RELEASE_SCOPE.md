# Release Scope

## Retained

- RT-Thread 4.1.1 core, permissible architecture ports/components and source build helpers.
- Original top-level vendor `applications/` demos and `examples/` sources.
- Vendor Rockchip BSP application entry points and configuration templates.
- Reviewed Rockchip HAL source embedded within this tree; relative links remain inside the repository.
- Original authors, copyrights, license/notice texts and applicable source attribution.

## Removed From This Source Candidate

- Local applications, board-integration additions, deployment scripts, captures, working records and assets outside the compared vendor baseline.
- Original machine/user paths, private environment snapshots, browser/Python environments, agent metadata and private repository histories.
- Generated objects, executables, AMP images, ELF/map files, generated caches and build logs.
- Vendor-only or unresolved wireless/audio/DSP firmware, libraries, proprietary headers, prebuilt host utilities and algorithm binaries.
- Selected vendor BSPs requiring unverified redistribution agreements, non-source vendor manuals/installers, and unverified font assets.

## Source Recovery Choices

Retained shared drivers, core build/configuration files and BSP application entry points are compared with the vendor baseline. The external HAL is materialized from its explicitly reviewed baseline source. Local application, HAL and board-integration modifications are excluded.

This provides a traceable source subset with documented release-preparation changes. There is no claim of identical peripheral behavior, pin mapping, interrupt ownership or memory layout on a currently deployed board.

## Known Limits

Only static source preparation was performed for this candidate. Some optional vendor build paths depend on excluded packages. Original vendor examples may retain public default/example addresses, symbolic credential fields and the original author names. Private scanning preserves these legitimate examples and attributions rather than deleting keywords indiscriminately.

The private review evidence and original local paths are maintained outside this source directory and are not part of the public payload.

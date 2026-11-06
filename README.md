# Rockchip AMP RTOS Source Collection

本仓库是经过发布整理的 RT-Thread / Rockchip 源码子集，内核版本为 4.1.1。保留可分发的原厂例程、原有版权及许可说明，排除基线以外的本地应用和板级集成内容。该源码子集不是官方未修改发行包，也不是完整 Linux SDK。

部分构建依赖需自行取得。当前只完成静态源码审计，未执行编译、烧录或硬件验收。请先阅读下方来源、许可、依赖和验证范围。

This is a source-only RT-Thread / Rockchip subset prepared from compared local vendor reference trees. It retains redistributable vendor examples and third-party attribution while excluding local applications, board-integration additions, working records, build outputs and components whose redistribution authorization was not established.

This is an independently prepared source subset, not a complete vendor SDK or an official unmodified release. The RTOS was added to the host Linux SDK from external sources; it is not an original Embedfire RTOS distribution.

## Source and Version

- The RT-Thread core identifies itself as version **4.1.1**.
- Whole-tree comparison used a local **Forlinx ELF2 RTOS baseline**. Retained files were compared byte for byte with that reference; documented release-preparation changes are distinguished from unchanged source.
- The Rockchip HAL was compared separately against the HAL supplied beside that baseline. Its source is included as a real directory rather than an external SDK symlink.
- A local package match does not attest to a pristine upstream tag or an official vendor endorsement.
- Local application and board-integration additions are excluded. Shared/BSP files are restored from the compared baseline; remaining modifications serve documented source-release preparation.

See [SOURCE_PROVENANCE.md](SOURCE_PROVENANCE.md), [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [RELEASE_SCOPE.md](RELEASE_SCOPE.md). The original upstream RT-Thread introduction is retained in [README.upstream.md](README.upstream.md).

## Retained Examples

The original top-level `applications/` collection is retained, including animation, clock, LVGL, recording, PCBA, IoT and startup examples. The original top-level `examples/` collection is retained except for separately listed non-source or sensitive assets. BSP application entry points are restored to vendor examples rather than private business applications.

The tree also contains the RT-Thread kernel, architecture ports, components, Rockchip BSPs, permitted HAL sources, RPMsg-related source, configuration templates and source build helpers. Some unrelated BSPs or optional vendor packages were omitted where their source notices require a separate agreement or their redistribution terms could not be established.

## Build Prerequisites

Use Linux, Python and SCons versions compatible with the selected vendor BSP. Supply a suitable cross toolchain yourself and set `RTT_EXEC_PATH` to its `bin/` directory. The 32-bit RK3568 and 64-bit RK3588 BSPs require different toolchains and configuration choices.

Use a case-sensitive Linux filesystem when cloning or extracting. The original RK2108 source has distinct `Image/` and `image/` paths; a case-insensitive checkout can silently overwrite configuration files.

For example, from the repository root:

```sh
export RTT_ROOT="$PWD"
export RTT_EXEC_PATH=/path/to/compatible/toolchain/bin
cd bsp/rockchip/rk3568-32
scons -j4
```

This illustrates the vendor build entry point; it is not a tested build command for every retained BSP. Configuration files describe vendor boards and are not a validated Linux/RT resource layout for an arbitrary target board.

Prebuilt packaging utilities, boot firmware, cross toolchains, Linux/U-Boot images, wireless libraries and firmware, and some optional vendor algorithms are not distributed here. Consult [EXTERNAL_DEPENDENCIES.md](EXTERNAL_DEPENDENCIES.md) before attempting builds that use them. Do not substitute arbitrary firmware or memory addresses from another board.

## Validation Boundary

The preparation checks file provenance, retained example files, source references, symlink boundaries, static syntax and potential private information. The release audit describes the exact coverage and remaining limitations.

Compilation/linking, FIT generation from real payloads, board boot, tick/UART interrupts, RPMsg transport, CAN buses and hardware peripherals were **NOT RUN** for this source candidate. Prior private-project test records are not included and are not evidence that this candidate is hardware-ready.

## Licensing

The root [LICENSE](LICENSE) is Apache-2.0 for the applicable RT-Thread work. It does not relicense every file in this collection. BSD, MIT, GPL and other retained notices continue to apply to their respective components. Preserve all copyright, author, license and notice files when redistributing or modifying those components.

Some original vendor examples contain public sample addresses or demonstration credentials. These are baseline example values, not access to a deployed system. Configure your own runtime values before enabling a network example.

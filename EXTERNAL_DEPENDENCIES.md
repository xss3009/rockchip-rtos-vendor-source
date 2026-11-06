# External Dependencies

This source collection deliberately does not bundle a complete Linux SDK. Optional examples may require additional components supplied under their own licenses.

| Dependency | How it is used | Availability in this collection |
| --- | --- | --- |
| Compatible ARM/AArch64 cross toolchain | Compiles the selected BSP; select the proper execution state and vendor-compatible compiler | Supply separately; configure `RTT_EXEC_PATH`. |
| Python and SCons | Runs RT-Thread build helpers | Supply from an appropriate host environment. No Python environment or cache is bundled. |
| Device-tree / FIT packaging tools | Reads ITS descriptions and produces AMP/FIT images | Precompiled vendor executables are omitted. Supply compatible tools with their own corresponding source and licenses. |
| Linux, DTS/DTB, U-Boot and boot firmware | Owns the Linux boot chain, CPU isolation, memory reservations, interrupts and peripherals | Not included. A retained ITS file alone is not sufficient to create a safe image for a board. |
| Wireless vendor stack, header, library and firmware packages | Used by optional Cypress/AMPAK/WICED/Bluetooth examples and adapters | Restricted or unresolved packages are omitted. Disabled package selections must not be treated as working wireless support. Obtain lawful vendor packages separately in a local private integration if needed. |
| Optional audio / DSP algorithm libraries and firmware | Used by vendor audio/vehicle/DSP examples | Omitted where binary redistribution authorization or corresponding source was not established. |
| Non-source vendor tools / flash algorithms | Used by some vendor-specific packaging or IDE flows | Omitted; original source build scripts may refer to these external tools. |
| Vendor assets excluded from source distribution | Some examples reference fonts, media, documents or binary demo resources | The release scope lists exclusions. Obtain suitable replacements under appropriate terms. |

Original example applications are retained wherever their own source can be distributed. Their presence is not a promise that every optional feature is self-contained, compiles with an arbitrary compiler, or runs on an unconfigured board.

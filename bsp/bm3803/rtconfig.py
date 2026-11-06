# Source release preparation 2026-11-06: portable path or reference adaptation; original notices retained.
import os

# toolchains options
ARCH='sparc-v8'
CPU='bm3803'
CROSS_TOOL='gcc'

if  CROSS_TOOL == 'gcc':
    PLATFORM 	= 'gcc'
    EXEC_PATH 	= r'/path/to/toolchain/bin'

BUILD = 'debug'

if PLATFORM == 'gcc':
    # toolchains
    PREFIX = 'sparc-gaisler-elf-'
    CC = PREFIX + 'gcc'
    CXX = PREFIX + 'g++'
    AS = PREFIX + 'gcc'
    AR = PREFIX + 'ar'
    LINK = PREFIX + 'gcc'
    TARGET_EXT = 'elf'
    SIZE = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY = PREFIX + 'objcopy'

    DEVICE = ' -mcpu=v8 -nostartfiles'
    #DEVICE = ' '
    CFLAGS = DEVICE
    AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp -D__ASSEMBLY__'
    LFLAGS = DEVICE + ' -Wl,-Map=rtthread-bm3803.map -T bm3803.lds -Ttext=0x40000000'

    CPATH = ''
    LPATH = ''

    if BUILD == 'debug':
        CFLAGS += ' -O0 -gdwarf-2 -Wall'
        AFLAGS += ' -gdwarf-2'
    else:
        CFLAGS += ' -O2 -Wall'

    POST_ACTION = OBJCPY + ' -O binary $TARGET rtthread.bin\n' +\
                  SIZE + ' $TARGET \n'

# Source release preparation 2026-11-06: portable path or reference adaptation; original notices retained.
###
 # @Author: hh
 # @Date: 2020-12-23 13:53:50
 # @LastEditTime: 2021-05-18 16:48:25
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: \ft\bare\2_base\factory.sh
### 
#/bin/sh
# scons --clean
# ./update.sh 
scons -j8
rm /path/to/local/input
cp ./rtthread.bin /path/to/local/input

# arm-none-eabi-objdump -D -m arm ft2004.elf > rtt.dis
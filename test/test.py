# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_cpu (dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Testing reset")
    dut.rst_n.value = 0
    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 3)
    assert dut.ewire.value == 0
    assert dut.twire.value == 1
    assert dut.acwire.value == 0
    assert dut.arwire.value == 0
    assert dut.drwire.value == 0
    assert dut.irwire.value == 0
    assert dut.pcwire.value == 0

    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uio_oe.value == 252
    dut._log.info("Testing CPU and BOOT ROM")
    dut._log.info("Testing Initial")
    await ClockCycles(dut.clk, 1)
    assert dut.irwire.value == 0
    dut._log.info("Testing SKI")
    await ClockCycles(dut.clk, 3)
    assert dut.irwire.value == 61952
    dut._log.info("Testing SKI and BUN")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 16384
    dut._log.info("Testing BUN")
    dut.intrin.value = 1 # This is needed for next SKI
    await ClockCycles(dut.clk, 8)
    assert dut.irwire.value == 61952
    dut._log.info("Testing SKI")
    dut.ui_in.value = 119 # This is needed for next INP
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 63488
    dut._log.info("Testing INP")
    await ClockCycles(dut.clk, 1)
    assert dut.acwire.value == 119
    dut._log.info("Testing ADD")
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 4103
    await ClockCycles(dut.clk, 3)
    assert dut.drwire.value == 17
    await ClockCycles(dut.clk, 1)
    assert dut.acwire.value == 136
    dut._log.info("Testing OUT")
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 62464
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 136
    dut._log.info("Testing STA to SPI")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 12432
    dut._log.info("Testing SPA")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 28688
    dut._log.info("Testing LDA")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 8199
    await ClockCycles(dut.clk, 4)
    assert dut.acwire.value == 17
    dut._log.info("Testing AND")
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 11
    await ClockCycles(dut.clk, 3)
    assert dut.drwire.value == 160
    await ClockCycles(dut.clk, 1)
    assert dut.acwire.value == 0
    dut._log.info("Testing SZA")
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 28676
    dut._log.info("Testing LDAI")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 40967
    await ClockCycles(dut.clk, 3)
    assert dut.drwire.value == 17
    await ClockCycles(dut.clk, 3)
    assert dut.acwire.value == 7
    dut._log.info("Testing ADDI")
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 36881
    await ClockCycles(dut.clk, 6)
    assert dut.acwire.value == 24
    dut._log.info("Testing CMA")
    await ClockCycles(dut.clk, 12)
    assert dut.irwire.value == 29184
    await ClockCycles(dut.clk, 1)
    assert dut.acwire.value == 65511
    dut._log.info("Testing SNA")
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 28680
    dut._log.info("Testing CIR")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 28800
    await ClockCycles(dut.clk, 1)
    assert dut.acwire.value == 32755
    dut._log.info("Testing OUT")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 62464
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 243
    dut._log.info("Testing CLE")
    assert dut.ewire.value == 1 # this is because of earlier CIR
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 29696
    await ClockCycles(dut.clk, 1)
    assert dut.ewire.value == 0
    dut._log.info("Testing CIL")
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 28736
    await ClockCycles(dut.clk, 1)
    assert dut.acwire.value == 65510
    dut._log.info("Testing STA to timer")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 12320
    dut._log.info("Testing INC")
    await ClockCycles(dut.clk, 6)
    assert dut.irwire.value == 28704
    await ClockCycles(dut.clk, 1)
    assert dut.acwire.value == 65511
    dut._log.info("Testing CME")
    assert dut.ewire.value == 0
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 28928
    await ClockCycles(dut.clk, 1)
    assert dut.ewire.value == 1
    dut._log.info("Testing CIL")
    await ClockCycles(dut.clk, 4)
    assert dut.irwire.value == 28736
    await ClockCycles(dut.clk, 1)
    assert dut.acwire.value == 65487
    dut._log.info("Testing STA to pwm")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 12352
    dut._log.info("Testing BSA")
    await ClockCycles(dut.clk, 6)
    assert dut.irwire.value == 20510
    await ClockCycles(dut.clk, 1)
    assert dut.arwire.value == 30
    await ClockCycles(dut.clk, 5)
    assert dut.arwire.value == 31
    dut._log.info("Testing BUNI")
    await ClockCycles(dut.clk, 2)
    assert dut.irwire.value == 49182
    await ClockCycles(dut.clk, 1)
    assert dut.arwire.value == 30
    await ClockCycles(dut.clk, 2)
    assert dut.arwire.value == 28
    dut._log.info("Testing ISZ")
    await ClockCycles(dut.clk, 5)
    assert dut.irwire.value == 24705
    await ClockCycles(dut.clk, 1)
    assert dut.arwire.value == 129
    dut._log.info("Testing HLT")
    await ClockCycles(dut.clk, 10)
    assert dut.irwire.value == 28673

@cocotb.test()
async def test_spi (dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Testing reset")
    dut.rst_n.value = 0
    dut.intrin.value = 0
    await ClockCycles(dut.clk, 3)
    assert dut.ewire.value == 0
    assert dut.twire.value == 1
    assert dut.acwire.value == 0
    assert dut.arwire.value == 0
    assert dut.drwire.value == 0
    assert dut.irwire.value == 0
    assert dut.pcwire.value == 0

    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uio_oe.value == 252
    dut._log.info("Testing SPI LOAD")
    dut._log.info("Testing Initial")
    await ClockCycles(dut.clk, 1)
    assert dut.irwire.value == 0
    await ClockCycles(dut.clk, 8)
    dut.intrin.value = 1 # This is needed for next SKI
    await ClockCycles(dut.clk, 8)
    dut.ui_in.value = 119 # This is needed for next INP
    await ClockCycles(dut.clk, 23)
    assert dut.irwire.value == 12432
    await ClockCycles(dut.clk, 2)
    assert dut.spireg.value == 136
    assert dut.uio_out.value == 40
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 0
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 8
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 0
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 40
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 0
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 8
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 0

@cocotb.test()
async def test_pwm (dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Testing reset")
    dut.rst_n.value = 0
    dut.intrin.value = 0
    await ClockCycles(dut.clk, 3)
    assert dut.ewire.value == 0
    assert dut.twire.value == 1
    assert dut.acwire.value == 0
    assert dut.arwire.value == 0
    assert dut.drwire.value == 0
    assert dut.irwire.value == 0
    assert dut.pcwire.value == 0

    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uio_oe.value == 252
    dut._log.info("Testing PWM LOAD")
    dut._log.info("Testing Initial")
    await ClockCycles(dut.clk, 1)
    assert dut.irwire.value == 0
    await ClockCycles(dut.clk, 8)
    dut.intrin.value = 1 # This is needed for next SKI
    await ClockCycles(dut.clk, 8)
    dut.ui_in.value = 119 # This is needed for next INP
    await ClockCycles(dut.clk, 137)
    assert dut.irwire.value == 12352
    await ClockCycles(dut.clk, 2)
    assert dut.pwmreg.value == 7
    assert dut.uio_out.value == 16
    await ClockCycles(dut.clk, 6)
    assert dut.uio_out.value == 20
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 20
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 20
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 20
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 20
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 20
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 20
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 16
    await ClockCycles(dut.clk, 1)
    assert dut.uio_out.value == 20

@cocotb.test()
async def test_timer (dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Testing reset")
    dut.rst_n.value = 0
    dut.intrin.value = 0
    await ClockCycles(dut.clk, 3)
    assert dut.ewire.value == 0
    assert dut.twire.value == 1
    assert dut.acwire.value == 0
    assert dut.arwire.value == 0
    assert dut.drwire.value == 0
    assert dut.irwire.value == 0
    assert dut.pcwire.value == 0

    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uio_oe.value == 252
    dut._log.info("Testing TIMER LOAD")
    dut._log.info("Testing Initial")
    await ClockCycles(dut.clk, 1)
    assert dut.irwire.value == 0
    await ClockCycles(dut.clk, 8)
    dut.intrin.value = 1 # This is needed for next SKI
    await ClockCycles(dut.clk, 8)
    dut.ui_in.value = 119 # This is needed for next INP
    await ClockCycles(dut.clk, 115)
    assert dut.irwire.value == 12320
    await ClockCycles(dut.clk, 2)
    assert dut.timereg.value == 6
    assert dut.uio_out.value == 16
    await ClockCycles(dut.clk, 28)
    assert dut.uio_out.value == 20
    await ClockCycles(dut.clk, 32)
    assert dut.uio_out.value == 28
    await ClockCycles(dut.clk, 32)
    assert dut.uio_out.value == 28

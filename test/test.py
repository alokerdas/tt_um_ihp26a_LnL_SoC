# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_loopback(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    assert dut.uio_oe.value == 255

    # When under reset: Output is uio_in, uio is in input mode
    for i in range(256):
        dut.ui_in.value = i
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == i

@cocotb.test()
async def test_cpu (dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.intrin.value = 0
    dut._log.info("Testing reset")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)
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
    await ClockCycles(dut.clk, 1)
    dut._log.info("Testing SKI")
    assert dut.irwire.value == 0
    # dut.intrin.value = 1
    # dut.ui_in.value = 119

`default_nettype none
`timescale 1ns / 1ps

/* This testbench just instantiates the module and makes some convenient wires
   that can be driven / tested by the cocotb test.py.
*/
module tb ();

  // Dump the signals to a FST file. You can view it with gtkwave or surfer.
  initial begin
    $dumpfile("tb.fst");
    $dumpvars(0, tb);
    #1;
  end

  // Wire up the inputs and outputs:
  reg clk;
  reg rst_n;
  reg ena;
  reg [7:0] ui_in; // connected to keyboard
  wire [7:0] uio_in;
  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

  reg intrin, spin, spcsin;
  wire [15:0] acwire, drwire, irwire;
  wire [11:0] arwire, pcwire;
  wire [10:0] twire;
  wire [7:0] display, socbidin, socbidut, socbiden;
  wire ewire;

  assign arwire = user_project.cpu0.addr;
  assign ewire = user_project.cpu0.e;
  assign twire = user_project.cpu0.t;
  assign acwire = user_project.cpu0.ac;
  assign drwire = user_project.cpu0.dr;
  assign pcwire = user_project.cpu0.pc;
  assign irwire = user_project.cpu0.ir;

  assign uio_in = {1'b0, 1'b0, 1'b0, 1'b0, 1'b0, spcsin, spin, intrin};

  // Replace tt_um_example with your module name:
  tt_um_LnL_SoC user_project (
      .ui_in  (ui_in),    // Dedicated inputs
      .uo_out (uo_out),   // Dedicated outputs
      .uio_in (uio_in),   // IOs: Input path
      .uio_out(uio_out),  // IOs: Output path
      .uio_oe (uio_oe),   // IOs: Enable path (active high: 0=input, 1=output)
      .ena    (ena),      // enable - goes high when design is selected
      .clk    (clk),      // clock
      .rst_n  (rst_n)     // not reset
  );

endmodule

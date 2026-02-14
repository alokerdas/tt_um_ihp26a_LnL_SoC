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
  wire [7:0] display, spireg;
  wire ewire;

`ifdef GL_TEST
  assign ewire = user_project.\cpu0.e ;

  assign arwire[0] = user_project.\addr_to_memio[0] ;
  assign arwire[1] = user_project.\addr_to_memio[1] ;
  assign arwire[2] = user_project.\addr_to_memio[2] ;
  assign arwire[3] = user_project.\addr_to_memio[3] ;
  assign arwire[4] = user_project.\addr_to_memio[4] ;
  assign arwire[5] = user_project.\addr_to_memio[5] ;
  assign arwire[6] = user_project.\addr_to_memio[6] ;
  assign arwire[7] = user_project.\addr_to_memio[7] ;
  assign arwire[8] = user_project.\addr_to_memio[8] ;
  assign arwire[9] = user_project.\addr_to_memio[9] ;
  assign arwire[10] = user_project.\addr_to_memio[10] ;
  assign arwire[11] = user_project.\addr_to_memio[11] ;

  assign twire[0] = user_project.\cpu0.t[0] ;
  assign twire[1] = user_project.\cpu0.t[1] ;
  assign twire[2] = user_project.\cpu0.t[2] ;
  assign twire[3] = user_project.\cpu0.t[3] ;
  assign twire[4] = user_project.\cpu0.t[4] ;
  assign twire[5] = user_project.\cpu0.t[5] ;
  assign twire[6] = user_project.\cpu0.t[6] ;
  assign twire[7] = user_project.\cpu0.t[7] ;
  assign twire[8] = user_project.\cpu0.t[8] ;
  assign twire[9] = user_project.\cpu0.t[9] ;
  assign twire[10] = user_project.\cpu0.t[10] ;

  assign acwire[0] = user_project.\cpu0.ac[0] ;
  assign acwire[1] = user_project.\cpu0.ac[1] ;
  assign acwire[2] = user_project.\cpu0.ac[2] ;
  assign acwire[3] = user_project.\cpu0.ac[3] ;
  assign acwire[4] = user_project.\cpu0.ac[4] ;
  assign acwire[5] = user_project.\cpu0.ac[5] ;
  assign acwire[6] = user_project.\cpu0.ac[6] ;
  assign acwire[7] = user_project.\cpu0.ac[7] ;
  assign acwire[8] = user_project.\cpu0.ac[8] ;
  assign acwire[9] = user_project.\cpu0.ac[9] ;
  assign acwire[10] = user_project.\cpu0.ac[10] ;
  assign acwire[11] = user_project.\cpu0.ac[11] ;
  assign acwire[12] = user_project.\cpu0.ac[12] ;
  assign acwire[13] = user_project.\cpu0.ac[13] ;
  assign acwire[14] = user_project.\cpu0.ac[14] ;
  assign acwire[15] = user_project.\cpu0.ac[15] ;

  assign drwire[0] = user_project.\cpu0.dr[0] ;
  assign drwire[1] = user_project.\cpu0.dr[1] ;
  assign drwire[2] = user_project.\cpu0.dr[2] ;
  assign drwire[3] = user_project.\cpu0.dr[3] ;
  assign drwire[4] = user_project.\cpu0.dr[4] ;
  assign drwire[5] = user_project.\cpu0.dr[5] ;
  assign drwire[6] = user_project.\cpu0.dr[6] ;
  assign drwire[7] = user_project.\cpu0.dr[7] ;
  assign drwire[8] = user_project.\cpu0.dr[8] ;
  assign drwire[9] = user_project.\cpu0.dr[9] ;
  assign drwire[10] = user_project.\cpu0.dr[10] ;
  assign drwire[11] = user_project.\cpu0.dr[11] ;
  assign drwire[12] = user_project.\cpu0.dr[12] ;
  assign drwire[13] = user_project.\cpu0.dr[13] ;
  assign drwire[14] = user_project.\cpu0.dr[14] ;
  assign drwire[15] = user_project.\cpu0.dr[15] ;

  assign irwire[0] = user_project.\cpu0.ir[0] ;
  assign irwire[1] = user_project.\cpu0.ir[1] ;
  assign irwire[2] = user_project.\cpu0.ir[2] ;
  assign irwire[3] = user_project.\cpu0.ir[3] ;
  assign irwire[4] = user_project.\cpu0.ir[4] ;
  assign irwire[5] = user_project.\cpu0.ir[5] ;
  assign irwire[6] = user_project.\cpu0.ir[6] ;
  assign irwire[7] = user_project.\cpu0.ir[7] ;
  assign irwire[8] = user_project.\cpu0.ir[8] ;
  assign irwire[9] = user_project.\cpu0.ir[9] ;
  assign irwire[10] = user_project.\cpu0.ir[10] ;
  assign irwire[11] = user_project.\cpu0.ir[11] ;
  assign irwire[12] = user_project.\cpu0.decode2.a[0] ;
  assign irwire[13] = user_project.\cpu0.decode2.a[1] ;
  assign irwire[14] = user_project.\cpu0.decode2.a[2] ;
  assign irwire[15] = user_project.\cpu0.ir[15] ;

  assign pcwire[0] = user_project.\cpu0.pc[0] ;
  assign pcwire[1] = user_project.\cpu0.pc[1] ;
  assign pcwire[2] = user_project.\cpu0.pc[2] ;
  assign pcwire[3] = user_project.\cpu0.pc[3] ;
  assign pcwire[4] = user_project.\cpu0.pc[4] ;
  assign pcwire[5] = user_project.\cpu0.pc[5] ;
  assign pcwire[6] = user_project.\cpu0.pc[6] ;
  assign pcwire[7] = user_project.\cpu0.pc[7] ;
  assign pcwire[8] = user_project.\cpu0.pc[8] ;
  assign pcwire[9] = user_project.\cpu0.pc[9] ;
  assign pcwire[10] = user_project.\cpu0.pc[10] ;
  assign pcwire[11] = user_project.\cpu0.pc[11] ;

  assign spireg[0] = user_project.\spi0.datareg[0] ;
  assign spireg[1] = user_project.\spi0.datareg[1] ;
  assign spireg[2] = user_project.\spi0.datareg[2] ;
  assign spireg[3] = user_project.\spi0.datareg[3] ;
  assign spireg[4] = user_project.\spi0.datareg[4] ;
  assign spireg[5] = user_project.\spi0.datareg[5] ;
  assign spireg[6] = user_project.\spi0.datareg[6] ;
  assign spireg[7] = user_project.\spi0.datareg[7] ;
`else
  assign arwire = user_project.cpu0.addr;
  assign ewire = user_project.cpu0.e;
  assign twire = user_project.cpu0.t;
  assign acwire = user_project.cpu0.ac;
  assign drwire = user_project.cpu0.dr;
  assign pcwire = user_project.cpu0.pc;
  assign irwire = user_project.cpu0.ir;
  assign spireg = user_project.spi0.datareg;
`endif

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

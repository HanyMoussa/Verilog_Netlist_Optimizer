module testcase10 (in, out);
input in;
output out;
wire vdd = 1'b1;
wire gnd = 1'b0;
NAND2X1 U1 ( .A(in), .Y(wire_1) );
INVX2 U2_s_s_s ( .A(wire_1), .Y(out) );
endmodule
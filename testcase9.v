module testcase9(in, out);

input in;
output out;

wire vdd = 1'b1;
wire gnd = 1'b0;

INVX1 INVX1_1 ( .A(in), .Y(w1) );
INVX1 INVX1_2 ( .A(w1), .Y(w2) );
INVX1 INVX1_3 ( .A(w2), .Y(w3) );
INVX1 INVX1_4 ( .A(w3), .Y(w4) );
INVX1 INVX1_5 ( .A(w4), .Y(out) );

endmodule
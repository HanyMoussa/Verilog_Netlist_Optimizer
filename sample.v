module testcase1 (in, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12 , out13, out14, out15, out16, out17, out18, out19, out20);

input in;
output out1;
output out2;
output out3;
output out4;
output out5;
output out6;
output out7;
output out8;
output out9;
output out10;
output out11;
output out12;
output out13;
output out14;
output out15;
output out16;
output out17;
output out18;
output out19;
output out20;

wire vdd = 1'b1;
wire gnd = 1'b0;

INVX1 INVX1_0 ( .A(in), .Y(w1) );
INVX1 INVX1_1 ( .A(w1), .Y(out1) );
INVX1 INVX1_2 ( .A(w1), .Y(out2) );
INVX1 INVX1_3 ( .A(w1), .Y(out3) );
INVX1 INVX1_4 ( .A(w1), .Y(out4) );
INVX1 INVX1_5 ( .A(w1), .Y(out5) );
INVX1 INVX1_6 ( .A(w1), .Y(out6) );
INVX1 INVX1_7 ( .A(w1), .Y(out7) );
INVX1 INVX1_8 ( .A(w1), .Y(out8) );
INVX1 INVX1_9 ( .A(w1), .Y(out9) );
INVX1 INVX1_10 ( .A(w1), .Y(out10) );
INVX1 INVX1_11 ( .A(w1), .Y(out11) );
INVX1 INVX1_12 ( .A(w1), .Y(out12) );
INVX1 INVX1_13 ( .A(w1), .Y(out13) );
INVX1 INVX1_14 ( .A(w1), .Y(out14) );
INVX1 INVX1_15 ( .A(w1), .Y(out15) );
INVX1 INVX1_16 ( .A(w1), .Y(out16) );
INVX1 INVX1_17 ( .A(w1), .Y(out17) );
INVX1 INVX1_18 ( .A(w1), .Y(out18) );
INVX1 INVX1_19 ( .A(w1), .Y(out19) );
INVX1 INVX1_20 ( .A(w1), .Y(out20) );

endmodule
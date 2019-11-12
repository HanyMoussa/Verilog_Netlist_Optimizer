module testcase9(in, out);
input in;
output out;
wire vdd = 1'b1;
wire gnd = 1'b0;
INVX8 INVX1_1_s_s_s ( .A(in), .Y(w1) );
INVX2 INVX1_2_s_s_s ( .A(w1), .Y(w2) );
INVX2 INVX1_3_s_s_s ( .A(w2), .Y(w3) );
INVX2 INVX1_4_s_s_s ( .A(w3), .Y(w4) );
INVX4 INVX1_5_s_s_s_s ( .A(w4), .Y(out) );
endmodule
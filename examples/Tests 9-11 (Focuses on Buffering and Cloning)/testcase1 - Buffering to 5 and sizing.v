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
INVX8 INVX1_0_s_s_s ( .A(in), .Y(w1) );
INVX4 INVX1_1_s_s_s_s ( .A(new_wire_1), .Y(out1) );
INVX4 INVX1_2_s_s_s_s ( .A(new_wire_1), .Y(out2) );
INVX4 INVX1_3_s_s_s_s ( .A(new_wire_1), .Y(out3) );
INVX4 INVX1_4_s_s_s_s ( .A(new_wire_1), .Y(out4) );
INVX4 INVX1_5_s_s_s_s ( .A(new_wire_1), .Y(out5) );
INVX4 INVX1_6_s_s_s_s ( .A(new_wire_2), .Y(out6) );
INVX4 INVX1_7_s_s_s_s ( .A(new_wire_2), .Y(out7) );
INVX4 INVX1_8_s_s_s_s ( .A(new_wire_2), .Y(out8) );
INVX4 INVX1_9_s_s_s_s ( .A(new_wire_2), .Y(out9) );
INVX4 INVX1_10_s_s_s_s ( .A(new_wire_2), .Y(out10) );
INVX4 INVX1_11_s_s_s_s ( .A(new_wire_3), .Y(out11) );
INVX4 INVX1_12_s_s_s_s ( .A(new_wire_3), .Y(out12) );
INVX4 INVX1_13_s_s_s_s ( .A(new_wire_3), .Y(out13) );
INVX4 INVX1_14_s_s_s_s ( .A(new_wire_3), .Y(out14) );
INVX4 INVX1_15_s_s_s_s ( .A(new_wire_3), .Y(out15) );
INVX4 INVX1_16_s_s_s_s ( .A(new_wire_4), .Y(out16) );
INVX4 INVX1_17_s_s_s_s ( .A(new_wire_4), .Y(out17) );
INVX4 INVX1_18_s_s_s_s ( .A(new_wire_4), .Y(out18) );
INVX4 INVX1_19_s_s_s_s ( .A(new_wire_4), .Y(out19) );
INVX4 INVX1_20_s_s_s_s ( .A(new_wire_4), .Y(out20) );
BUFX4 new_buffer_1_s ( .A(w1), .Y(new_wire_1) );
BUFX4 new_buffer_2_s ( .A(w1), .Y(new_wire_2) );
BUFX4 new_buffer_3_s ( .A(w1), .Y(new_wire_3) );
BUFX4 new_buffer_4_s ( .A(w1), .Y(new_wire_4) );
endmodule
module testcase1 (in, out);

input in;
output out;

wire vdd = 1'b1;
wire gnd = 1'b0;

AND2X1 AND2X1_1 ( .A(in), .B(in), .Y(w1) );
AND2X1 AND2X1_2 ( .A(w1), .B(w1), .Y(w2) );
AND2X1 AND2X1_3 ( .A(w2), .B(w2), .Y(w3) );
AND2X1 AND2X1_4 ( .A(w3), .B(w3), .Y(w4) );
AND2X1 AND2X1_5 ( .A(w4), .B(w4), .Y(out) );
endmodule
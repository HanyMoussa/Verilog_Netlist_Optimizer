BUFX4 BUFX4_1 ( .A(1), .Y(2) );
INVX8 INVX8_1 ( .A(2), .Y(3) );
NAND2X1 NAND2X1_1 ( .A(1), .B(3), .Y(4) );
NOR2X1 NOR2X1_2 ( .A(4), .B(3), .Y(5) );
DFFPOSX1 DFFPOSX1_2121 ( .CLK(myclk), .D(5), .Q(6) );
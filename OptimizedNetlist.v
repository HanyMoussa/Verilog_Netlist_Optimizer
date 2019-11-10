module uart (reset, clk, uart_rxd, rx_ack, tx_data, tx_wr, uart_txd, rx_data, rx_avail, rx_error, tx_busy);
input reset;
input clk;
input uart_rxd;
input rx_ack;
input tx_wr;
output uart_txd;
output rx_avail;
output rx_error;
output tx_busy;
input [7:0] tx_data;
output [7:0] rx_data;
wire vdd = 1'b1;
wire gnd = 1'b0;
BUFX4 BUFX4_1 ( .A(_13_), .Y(_13__bF_buf3) );
BUFX4 BUFX4_2 ( .A(_13_), .Y(_13__bF_buf2) );
BUFX4 BUFX4_3 ( .A(_13_), .Y(_13__bF_buf1) );
BUFX4 BUFX4_4 ( .A(clk), .Y(clk_bF_buf6) );
BUFX4 BUFX4_5 ( .A(clk), .Y(clk_bF_buf5) );
BUFX4 BUFX4_6 ( .A(clk), .Y(clk_bF_buf4) );
BUFX4 BUFX4_7 ( .A(clk), .Y(clk_bF_buf3) );
BUFX4 BUFX4_8 ( .A(clk), .Y(clk_bF_buf2) );
BUFX4 BUFX4_9 ( .A(clk), .Y(clk_bF_buf1) );
BUFX4 BUFX4_10 ( .A(clk), .Y(clk_bF_buf0) );
INVX8 INVX8_1 ( .A(reset), .Y(_13_) );
OAI21X1 OAI21X1_1 ( .A(_233_), .B(tx_wr), .C(_13__bF_buf2), .Y(_14_) );
NOR2X1 NOR2X1_1 ( .A(tx_bitcount_2_), .B(_16_), .Y(_17_) );
NAND2X1 NAND2X1_1 ( .A(_15_), .B(_17_), .Y(_18_) );
NOR2X1 NOR2X1_2 ( .A(enable16_counter_3_), .B(enable16_counter_2_), .Y(_21_) );
NOR2X1 NOR2X1_3 ( .A(enable16_counter_1_), .B(enable16_counter_0_), .Y(_22_) );
NAND2X1 NAND2X1_2 ( .A(_21_), .B(_22_), .Y(_23_) );
NOR2X1 NOR2X1_4 ( .A(enable16_counter_4_), .B(enable16_counter_7_), .Y(_24_) );
NOR2X1 NOR2X1_5 ( .A(enable16_counter_5_), .B(enable16_counter_6_), .Y(_25_) );
NAND2X1 NAND2X1_3 ( .A(_24_), .B(_25_), .Y(_26_) );
NOR2X1 NOR2X1_6 ( .A(new_wire_17), .B(_26_), .Y(_27_) );
NOR2X1 NOR2X1_7 ( .A(enable16_counter_8_), .B(enable16_counter_11_), .Y(_28_) );
NOR2X1 NOR2X1_8 ( .A(enable16_counter_9_), .B(enable16_counter_10_), .Y(_29_) );
NAND2X1 NAND2X1_4 ( .A(_28_), .B(_29_), .Y(_30_) );
NOR2X1 NOR2X1_9 ( .A(enable16_counter_15_), .B(enable16_counter_12_), .Y(_31_) );
NOR2X1 NOR2X1_10 ( .A(enable16_counter_14_), .B(enable16_counter_13_), .Y(_32_) );
NAND2X1 NAND2X1_5 ( .A(_31_), .B(_32_), .Y(_33_) );
NOR2X1 NOR2X1_11 ( .A(_30_), .B(_33_), .Y(_34_) );
NAND3X1 NAND3X1_1 ( .A(_233_), .B(new_wire_19), .C(_34_), .Y(_35_) );
NOR2X1 NOR2X1_12 ( .A(tx_count16_1_), .B(tx_count16_0_), .Y(_36_) );
NOR2X1 NOR2X1_13 ( .A(tx_count16_3_), .B(tx_count16_2_), .Y(_37_) );
NAND2X1 NAND2X1_6 ( .A(_36_), .B(_37_), .Y(_38_) );
OR2X2 OR2X2_1 ( .A(new_wire_21), .B(new_wire_23), .Y(_39_) );
NOR2X1 NOR2X1_14 ( .A(_20_), .B(_39_), .Y(_40_) );
AOI21X1 AOI21X1_1 ( .A(_40_), .B(_19_), .C(_14_), .Y(_9_) );
OAI21X1 OAI21X1_2 ( .A(_233_), .B(_41_), .C(_13__bF_buf2), .Y(_42_) );
XNOR2X1 XNOR2X1_1 ( .A(new_wire_23), .B(tx_bitcount_0_), .Y(_43_) );
NAND2X1 NAND2X1_7 ( .A(new_wire_19), .B(_34_), .Y(_45_) );
OAI21X1 OAI21X1_3 ( .A(_44_), .B(new_wire_27), .C(_20_), .Y(_46_) );
OAI21X1 OAI21X1_4 ( .A(new_wire_21), .B(_43_), .C(_46_), .Y(_47_) );
NOR2X1 NOR2X1_15 ( .A(new_wire_23), .B(new_wire_21), .Y(_48_) );
NOR2X1 NOR2X1_16 ( .A(tx_bitcount_1_), .B(new_wire_29), .Y(_49_) );
NOR2X1 NOR2X1_17 ( .A(tx_bitcount_1_), .B(tx_bitcount_0_), .Y(_51_) );
NOR2X1 NOR2X1_18 ( .A(_15_), .B(_20_), .Y(_52_) );
NOR2X1 NOR2X1_19 ( .A(_51_), .B(_52_), .Y(_53_) );
OAI21X1 OAI21X1_5 ( .A(_53_), .B(_39_), .C(_50_), .Y(_54_) );
OAI21X1 OAI21X1_6 ( .A(_15_), .B(_20_), .C(_55_), .Y(_56_) );
NAND2X1 NAND2X1_8 ( .A(tx_bitcount_2_), .B(_52_), .Y(_57_) );
AOI21X1 AOI21X1_2 ( .A(_57_), .B(_56_), .C(new_wire_23), .Y(_58_) );
AOI21X1 AOI21X1_3 ( .A(_55_), .B(new_wire_23), .C(_58_), .Y(_59_) );
OAI21X1 OAI21X1_7 ( .A(_44_), .B(new_wire_27), .C(_55_), .Y(_60_) );
OAI21X1 OAI21X1_8 ( .A(new_wire_21), .B(_59_), .C(_60_), .Y(_61_) );
XNOR2X1 XNOR2X1_2 ( .A(_57_), .B(_16_), .Y(_62_) );
MUX2X1 MUX2X1_1 ( .A(_16_), .B(_62_), .S(new_wire_23), .Y(_63_) );
OAI21X1 OAI21X1_9 ( .A(_44_), .B(new_wire_27), .C(_16_), .Y(_64_) );
OAI21X1 OAI21X1_10 ( .A(new_wire_21), .B(_63_), .C(_64_), .Y(_65_) );
NAND2X1 NAND2X1_9 ( .A(_13__bF_buf1), .B(_66_), .Y(_67_) );
NOR2X1 NOR2X1_20 ( .A(_233_), .B(_41_), .Y(_68_) );
AND2X2 AND2X2_1 ( .A(_68_), .B(_13__bF_buf2), .Y(_69_) );
AOI21X1 AOI21X1_4 ( .A(_67_), .B(tx_count16_0_), .C(new_wire_31), .Y(_70_) );
OAI21X1 OAI21X1_11 ( .A(tx_count16_0_), .B(_67_), .C(_70_), .Y(_10__0_) );
NAND2X1 NAND2X1_10 ( .A(reset), .B(tx_count16_1_), .Y(_71_) );
AND2X2 AND2X2_2 ( .A(tx_count16_1_), .B(tx_count16_0_), .Y(_72_) );
OAI21X1 OAI21X1_12 ( .A(_36_), .B(_72_), .C(_66_), .Y(_73_) );
OAI21X1 OAI21X1_13 ( .A(tx_count16_1_), .B(_66_), .C(_73_), .Y(_74_) );
OAI21X1 OAI21X1_14 ( .A(new_wire_25), .B(_74_), .C(_71_), .Y(_10__1_) );
AOI21X1 AOI21X1_5 ( .A(_66_), .B(_72_), .C(tx_count16_2_), .Y(_75_) );
NAND3X1 NAND3X1_2 ( .A(tx_count16_2_), .B(_72_), .C(_66_), .Y(_76_) );
AOI22X1 AOI22X1_1 ( .A(reset), .B(tx_count16_2_), .C(_50_), .D(_76_), .Y(_77_) );
NOR2X1 NOR2X1_21 ( .A(_75_), .B(_77_), .Y(_10__2_) );
NAND2X1 NAND2X1_11 ( .A(tx_count16_2_), .B(_72_), .Y(_79_) );
XNOR2X1 XNOR2X1_3 ( .A(_79_), .B(tx_count16_3_), .Y(_80_) );
OAI21X1 OAI21X1_15 ( .A(_44_), .B(new_wire_27), .C(_78_), .Y(_81_) );
OAI21X1 OAI21X1_16 ( .A(new_wire_22), .B(_80_), .C(_81_), .Y(_82_) );
NOR3X1 NOR3X1_1 ( .A(_19_), .B(new_wire_24), .C(new_wire_22), .Y(_83_) );
NAND3X1 NAND3X1_3 ( .A(_84_), .B(new_wire_15), .C(new_wire_29), .Y(_85_) );
OAI21X1 OAI21X1_17 ( .A(txd_reg_0_), .B(new_wire_33), .C(_85_), .Y(_86_) );
AOI22X1 AOI22X1_2 ( .A(reset), .B(txd_reg_0_), .C(tx_data[0]), .D(new_wire_31), .Y(_87_) );
OAI21X1 OAI21X1_18 ( .A(new_wire_25), .B(_86_), .C(_87_), .Y(_11__0_) );
NAND3X1 NAND3X1_4 ( .A(_88_), .B(new_wire_15), .C(new_wire_29), .Y(_89_) );
OAI21X1 OAI21X1_19 ( .A(txd_reg_1_), .B(new_wire_33), .C(_89_), .Y(_90_) );
AOI22X1 AOI22X1_3 ( .A(reset), .B(txd_reg_1_), .C(tx_data[1]), .D(new_wire_31), .Y(_91_) );
OAI21X1 OAI21X1_20 ( .A(new_wire_25), .B(_90_), .C(_91_), .Y(_11__1_) );
NAND3X1 NAND3X1_5 ( .A(_92_), .B(new_wire_15), .C(new_wire_29), .Y(_93_) );
OAI21X1 OAI21X1_21 ( .A(txd_reg_2_), .B(new_wire_33), .C(_93_), .Y(_94_) );
AOI22X1 AOI22X1_4 ( .A(reset), .B(txd_reg_2_), .C(tx_data[2]), .D(new_wire_31), .Y(_95_) );
OAI21X1 OAI21X1_22 ( .A(new_wire_25), .B(_94_), .C(_95_), .Y(_11__2_) );
NAND3X1 NAND3X1_6 ( .A(_96_), .B(new_wire_15), .C(new_wire_29), .Y(_97_) );
OAI21X1 OAI21X1_23 ( .A(txd_reg_3_), .B(new_wire_33), .C(_97_), .Y(_98_) );
AOI22X1 AOI22X1_5 ( .A(reset), .B(txd_reg_3_), .C(tx_data[3]), .D(new_wire_31), .Y(_99_) );
OAI21X1 OAI21X1_24 ( .A(new_wire_25), .B(_98_), .C(_99_), .Y(_11__3_) );
NAND3X1 NAND3X1_7 ( .A(_100_), .B(new_wire_15), .C(new_wire_29), .Y(_101_) );
OAI21X1 OAI21X1_25 ( .A(txd_reg_4_), .B(new_wire_33), .C(_101_), .Y(_102_) );
AOI22X1 AOI22X1_6 ( .A(reset), .B(txd_reg_4_), .C(tx_data[4]), .D(new_wire_31), .Y(_103_) );
OAI21X1 OAI21X1_26 ( .A(new_wire_26), .B(_102_), .C(_103_), .Y(_11__4_) );
NAND3X1 NAND3X1_8 ( .A(_104_), .B(new_wire_16), .C(new_wire_30), .Y(_105_) );
OAI21X1 OAI21X1_27 ( .A(txd_reg_5_), .B(new_wire_33), .C(_105_), .Y(_106_) );
AOI22X1 AOI22X1_7 ( .A(reset), .B(txd_reg_5_), .C(tx_data[5]), .D(new_wire_32), .Y(_107_) );
OAI21X1 OAI21X1_28 ( .A(new_wire_26), .B(_106_), .C(_107_), .Y(_11__5_) );
NAND3X1 NAND3X1_9 ( .A(_108_), .B(new_wire_16), .C(new_wire_30), .Y(_109_) );
OAI21X1 OAI21X1_29 ( .A(txd_reg_6_), .B(new_wire_34), .C(_109_), .Y(_110_) );
AOI22X1 AOI22X1_8 ( .A(reset), .B(txd_reg_6_), .C(tx_data[6]), .D(new_wire_32), .Y(_111_) );
OAI21X1 OAI21X1_30 ( .A(new_wire_26), .B(_110_), .C(_111_), .Y(_11__6_) );
OAI21X1 OAI21X1_31 ( .A(_19_), .B(_39_), .C(txd_reg_7_), .Y(_113_) );
OAI21X1 OAI21X1_32 ( .A(_13__bF_buf2), .B(txd_reg_7_), .C(new_wire_26), .Y(_114_) );
AOI22X1 AOI22X1_9 ( .A(_112_), .B(new_wire_32), .C(_114_), .D(_113_), .Y(_11__7_) );
NAND3X1 NAND3X1_10 ( .A(rx_busy), .B(new_wire_19), .C(_34_), .Y(_118_) );
NAND2X1 NAND2X1_12 ( .A(_119_), .B(_120_), .Y(_121_) );
NAND2X1 NAND2X1_13 ( .A(rx_bitcount_3_), .B(rx_bitcount_0_), .Y(_122_) );
NOR2X1 NOR2X1_22 ( .A(_122_), .B(_121_), .Y(_123_) );
NOR2X1 NOR2X1_23 ( .A(rx_count16_1_), .B(rx_count16_0_), .Y(_124_) );
NOR2X1 NOR2X1_24 ( .A(rx_count16_3_), .B(rx_count16_2_), .Y(_125_) );
AND2X2 AND2X2_3 ( .A(_124_), .B(_125_), .Y(_126_) );
NAND2X1 NAND2X1_14 ( .A(_126_), .B(_123_), .Y(_127_) );
NOR3X1 NOR3X1_2 ( .A(_117_), .B(_127_), .C(_118_), .Y(_128_) );
NAND2X1 NAND2X1_15 ( .A(_13__bF_buf3), .B(_128_), .Y(_129_) );
MUX2X1 MUX2X1_2 ( .A(_115_), .B(_116_), .S(new_wire_35), .Y(_5__0_) );
MUX2X1 MUX2X1_3 ( .A(_130_), .B(_131_), .S(new_wire_35), .Y(_5__1_) );
MUX2X1 MUX2X1_4 ( .A(_132_), .B(_133_), .S(new_wire_35), .Y(_5__2_) );
MUX2X1 MUX2X1_5 ( .A(_134_), .B(_135_), .S(new_wire_35), .Y(_5__3_) );
MUX2X1 MUX2X1_6 ( .A(_136_), .B(_137_), .S(new_wire_35), .Y(_5__4_) );
MUX2X1 MUX2X1_7 ( .A(_138_), .B(_139_), .S(new_wire_35), .Y(_5__5_) );
MUX2X1 MUX2X1_8 ( .A(_140_), .B(_141_), .S(new_wire_36), .Y(_5__6_) );
MUX2X1 MUX2X1_9 ( .A(_142_), .B(_143_), .S(new_wire_36), .Y(_5__7_) );
NAND2X1 NAND2X1_16 ( .A(_230_), .B(_144_), .Y(_145_) );
OAI21X1 OAI21X1_33 ( .A(reset), .B(_145_), .C(new_wire_36), .Y(_1_) );
NAND2X1 NAND2X1_17 ( .A(_232_), .B(_144_), .Y(_146_) );
OAI21X1 OAI21X1_34 ( .A(_127_), .B(_118_), .C(_146_), .Y(_147_) );
NAND2X1 NAND2X1_18 ( .A(_13__bF_buf3), .B(_147_), .Y(_148_) );
NOR2X1 NOR2X1_25 ( .A(_128_), .B(_148_), .Y(_6_) );
NOR2X1 NOR2X1_26 ( .A(_149_), .B(_118_), .Y(_150_) );
NAND2X1 NAND2X1_19 ( .A(_151_), .B(_152_), .Y(_153_) );
NOR2X1 NOR2X1_27 ( .A(_121_), .B(_153_), .Y(_154_) );
NOR2X1 NOR2X1_28 ( .A(_123_), .B(_154_), .Y(_155_) );
AOI21X1 AOI21X1_6 ( .A(_117_), .B(_154_), .C(_155_), .Y(_156_) );
OAI21X1 OAI21X1_35 ( .A(uart_rxd2), .B(new_wire_27), .C(_157_), .Y(_158_) );
NAND2X1 NAND2X1_20 ( .A(_13__bF_buf0), .B(_158_), .Y(_159_) );
AOI21X1 AOI21X1_7 ( .A(_150_), .B(_156_), .C(_159_), .Y(_3_) );
AOI21X1 AOI21X1_8 ( .A(uart_rxd2), .B(_157_), .C(new_wire_27), .Y(_161_) );
OAI21X1 OAI21X1_36 ( .A(rx_count16_0_), .B(_161_), .C(_13__bF_buf0), .Y(_162_) );
AOI21X1 AOI21X1_9 ( .A(rx_count16_0_), .B(_160_), .C(_162_), .Y(_4__0_) );
AND2X2 AND2X2_4 ( .A(rx_count16_1_), .B(rx_count16_0_), .Y(_163_) );
OR2X2 OR2X2_2 ( .A(_163_), .B(_124_), .Y(_164_) );
OAI21X1 OAI21X1_37 ( .A(rx_count16_1_), .B(_161_), .C(_13__bF_buf0), .Y(_165_) );
AOI21X1 AOI21X1_10 ( .A(_160_), .B(_164_), .C(_165_), .Y(_4__1_) );
OAI21X1 OAI21X1_38 ( .A(_157_), .B(_163_), .C(_161_), .Y(_167_) );
NAND2X1 NAND2X1_21 ( .A(rx_count16_2_), .B(_163_), .Y(_168_) );
OAI21X1 OAI21X1_39 ( .A(_168_), .B(_118_), .C(_13__bF_buf3), .Y(_169_) );
AOI21X1 AOI21X1_11 ( .A(_167_), .B(_166_), .C(_169_), .Y(_4__2_) );
OAI21X1 OAI21X1_40 ( .A(_170_), .B(_168_), .C(rx_busy), .Y(_171_) );
OAI21X1 OAI21X1_41 ( .A(_168_), .B(_118_), .C(_170_), .Y(_172_) );
NAND2X1 NAND2X1_22 ( .A(_13__bF_buf3), .B(_172_), .Y(_173_) );
AOI21X1 AOI21X1_12 ( .A(_161_), .B(_171_), .C(_173_), .Y(_4__3_) );
NAND2X1 NAND2X1_23 ( .A(rx_bitcount_0_), .B(_126_), .Y(_174_) );
AND2X2 AND2X2_5 ( .A(new_wire_19), .B(_34_), .Y(_177_) );
NAND3X1 NAND3X1_11 ( .A(_13__bF_buf3), .B(_126_), .C(_177_), .Y(_178_) );
OAI21X1 OAI21X1_42 ( .A(reset), .B(_152_), .C(_178_), .Y(_179_) );
AND2X2 AND2X2_6 ( .A(_176_), .B(_179_), .Y(_2__0_) );
NAND2X1 NAND2X1_24 ( .A(_175_), .B(_177_), .Y(_180_) );
OAI21X1 OAI21X1_43 ( .A(_120_), .B(_174_), .C(rx_busy), .Y(_181_) );
OAI21X1 OAI21X1_44 ( .A(_120_), .B(_161_), .C(_181_), .Y(_182_) );
NAND2X1 NAND2X1_25 ( .A(_13__bF_buf0), .B(_182_), .Y(_183_) );
AOI21X1 AOI21X1_13 ( .A(_120_), .B(_180_), .C(_183_), .Y(_2__1_) );
NOR2X1 NOR2X1_29 ( .A(_119_), .B(_184_), .Y(_185_) );
NOR2X1 NOR2X1_30 ( .A(_120_), .B(_174_), .Y(_186_) );
AND2X2 AND2X2_7 ( .A(_160_), .B(_186_), .Y(_187_) );
OAI21X1 OAI21X1_45 ( .A(rx_bitcount_2_), .B(_187_), .C(_13__bF_buf0), .Y(_188_) );
AOI21X1 AOI21X1_14 ( .A(_181_), .B(_185_), .C(_188_), .Y(_2__2_) );
AOI21X1 AOI21X1_15 ( .A(_186_), .B(rx_bitcount_2_), .C(_157_), .Y(_189_) );
OAI21X1 OAI21X1_46 ( .A(_189_), .B(_184_), .C(rx_bitcount_3_), .Y(_190_) );
NAND3X1 NAND3X1_12 ( .A(rx_bitcount_2_), .B(_151_), .C(_187_), .Y(_191_) );
AOI21X1 AOI21X1_16 ( .A(_191_), .B(_190_), .C(reset), .Y(_2__3_) );
NAND2X1 NAND2X1_26 ( .A(rx_busy), .B(_155_), .Y(_192_) );
NOR2X1 NOR2X1_31 ( .A(_192_), .B(_178_), .Y(_193_) );
MUX2X1 MUX2X1_10 ( .A(_131_), .B(_116_), .S(new_wire_37), .Y(_7__0_) );
MUX2X1 MUX2X1_11 ( .A(_133_), .B(_131_), .S(new_wire_37), .Y(_7__1_) );
MUX2X1 MUX2X1_12 ( .A(_135_), .B(_133_), .S(new_wire_37), .Y(_7__2_) );
MUX2X1 MUX2X1_13 ( .A(_137_), .B(_135_), .S(new_wire_37), .Y(_7__3_) );
MUX2X1 MUX2X1_14 ( .A(_139_), .B(_137_), .S(new_wire_37), .Y(_7__4_) );
MUX2X1 MUX2X1_15 ( .A(_141_), .B(_139_), .S(new_wire_37), .Y(_7__5_) );
MUX2X1 MUX2X1_16 ( .A(_143_), .B(_141_), .S(new_wire_38), .Y(_7__6_) );
MUX2X1 MUX2X1_17 ( .A(_117_), .B(_143_), .S(new_wire_38), .Y(_7__7_) );
NAND2X1 NAND2X1_27 ( .A(_13__bF_buf2), .B(new_wire_28), .Y(_194_) );
NOR2X1 NOR2X1_32 ( .A(enable16_counter_0_), .B(new_wire_39), .Y(_0__0_) );
AOI21X1 AOI21X1_17 ( .A(enable16_counter_1_), .B(enable16_counter_0_), .C(reset), .Y(_195_) );
OAI21X1 OAI21X1_47 ( .A(enable16_counter_1_), .B(enable16_counter_0_), .C(_195_), .Y(_0__1_) );
NAND2X1 NAND2X1_28 ( .A(_196_), .B(_22_), .Y(_197_) );
OAI21X1 OAI21X1_48 ( .A(enable16_counter_1_), .B(enable16_counter_0_), .C(enable16_counter_2_), .Y(_198_) );
AOI21X1 AOI21X1_18 ( .A(_197_), .B(_198_), .C(new_wire_39), .Y(_0__2_) );
NAND2X1 NAND2X1_29 ( .A(enable16_counter_3_), .B(_197_), .Y(_199_) );
NAND3X1 NAND3X1_13 ( .A(_13__bF_buf3), .B(new_wire_17), .C(_199_), .Y(_0__3_) );
AOI21X1 AOI21X1_19 ( .A(new_wire_17), .B(enable16_counter_4_), .C(reset), .Y(_200_) );
OAI21X1 OAI21X1_49 ( .A(enable16_counter_4_), .B(new_wire_17), .C(_200_), .Y(_0__4_) );
OR2X2 OR2X2_3 ( .A(new_wire_17), .B(enable16_counter_4_), .Y(_201_) );
OR2X2 OR2X2_4 ( .A(_201_), .B(enable16_counter_5_), .Y(_202_) );
OAI21X1 OAI21X1_50 ( .A(enable16_counter_4_), .B(new_wire_17), .C(enable16_counter_5_), .Y(_203_) );
AOI21X1 AOI21X1_20 ( .A(_202_), .B(_203_), .C(new_wire_39), .Y(_0__5_) );
OR2X2 OR2X2_5 ( .A(_202_), .B(enable16_counter_6_), .Y(_204_) );
OAI21X1 OAI21X1_51 ( .A(enable16_counter_5_), .B(_201_), .C(enable16_counter_6_), .Y(_205_) );
AOI21X1 AOI21X1_21 ( .A(_204_), .B(_205_), .C(new_wire_39), .Y(_0__6_) );
OAI21X1 OAI21X1_52 ( .A(enable16_counter_6_), .B(_202_), .C(enable16_counter_7_), .Y(_207_) );
AOI21X1 AOI21X1_22 ( .A(_207_), .B(_206_), .C(new_wire_39), .Y(_0__7_) );
OAI21X1 OAI21X1_53 ( .A(new_wire_18), .B(_26_), .C(enable16_counter_8_), .Y(_208_) );
NAND2X1 NAND2X1_30 ( .A(_209_), .B(new_wire_19), .Y(_210_) );
AOI21X1 AOI21X1_23 ( .A(_208_), .B(_210_), .C(new_wire_39), .Y(_0__8_) );
OAI21X1 OAI21X1_54 ( .A(enable16_counter_8_), .B(_206_), .C(enable16_counter_9_), .Y(_211_) );
OR2X2 OR2X2_6 ( .A(_210_), .B(enable16_counter_9_), .Y(_212_) );
AOI21X1 AOI21X1_24 ( .A(_212_), .B(_211_), .C(new_wire_40), .Y(_0__9_) );
OAI21X1 OAI21X1_55 ( .A(enable16_counter_9_), .B(_210_), .C(enable16_counter_10_), .Y(_213_) );
OR2X2 OR2X2_7 ( .A(_212_), .B(enable16_counter_10_), .Y(_214_) );
AOI21X1 AOI21X1_25 ( .A(_214_), .B(_213_), .C(new_wire_40), .Y(_0__10_) );
OAI21X1 OAI21X1_56 ( .A(enable16_counter_10_), .B(_212_), .C(enable16_counter_11_), .Y(_215_) );
NAND3X1 NAND3X1_14 ( .A(_28_), .B(_29_), .C(new_wire_20), .Y(_216_) );
AOI21X1 AOI21X1_26 ( .A(_215_), .B(_216_), .C(new_wire_40), .Y(_0__11_) );
NOR2X1 NOR2X1_33 ( .A(enable16_counter_12_), .B(_216_), .Y(_217_) );
OAI21X1 OAI21X1_57 ( .A(_30_), .B(_206_), .C(enable16_counter_12_), .Y(_219_) );
AOI21X1 AOI21X1_27 ( .A(_218_), .B(_219_), .C(new_wire_40), .Y(_0__12_) );
OAI21X1 OAI21X1_58 ( .A(enable16_counter_12_), .B(_216_), .C(enable16_counter_13_), .Y(_220_) );
NAND2X1 NAND2X1_31 ( .A(_221_), .B(_217_), .Y(_222_) );
AOI21X1 AOI21X1_28 ( .A(_222_), .B(_220_), .C(new_wire_40), .Y(_0__13_) );
OAI21X1 OAI21X1_59 ( .A(enable16_counter_13_), .B(_218_), .C(enable16_counter_14_), .Y(_223_) );
NAND2X1 NAND2X1_32 ( .A(_32_), .B(_217_), .Y(_224_) );
AOI21X1 AOI21X1_29 ( .A(_223_), .B(_224_), .C(new_wire_40), .Y(_0__14_) );
OAI21X1 OAI21X1_60 ( .A(enable16_counter_14_), .B(_222_), .C(enable16_counter_15_), .Y(_225_) );
NOR2X1 NOR2X1_34 ( .A(new_wire_41), .B(_225_), .Y(_0__15_) );
AND2X2 AND2X2_8 ( .A(new_wire_34), .B(_226_), .Y(_227_) );
OAI21X1 OAI21X1_61 ( .A(_234_), .B(new_wire_30), .C(_228_), .Y(_229_) );
OAI21X1 OAI21X1_62 ( .A(_229_), .B(_227_), .C(_13__bF_buf2), .Y(_12_) );
DFFPOSX1 DFFPOSX1_1 ( .CLK(new_wire_9), .D(_12_), .Q(_234_) );
DFFPOSX1 DFFPOSX1_2 ( .CLK(new_wire_13), .D(_9_), .Q(_233_) );
DFFPOSX1 DFFPOSX1_3 ( .CLK(new_wire_9), .D(_8__0_), .Q(tx_bitcount_0_) );
DFFPOSX1 DFFPOSX1_4 ( .CLK(new_wire_13), .D(_8__1_), .Q(tx_bitcount_1_) );
DFFPOSX1 DFFPOSX1_5 ( .CLK(new_wire_9), .D(_8__2_), .Q(tx_bitcount_2_) );
DFFPOSX1 DFFPOSX1_6 ( .CLK(new_wire_9), .D(_8__3_), .Q(tx_bitcount_3_) );
DFFPOSX1 DFFPOSX1_7 ( .CLK(new_wire_9), .D(_10__0_), .Q(tx_count16_0_) );
DFFPOSX1 DFFPOSX1_8 ( .CLK(new_wire_9), .D(_10__1_), .Q(tx_count16_1_) );
DFFPOSX1 DFFPOSX1_9 ( .CLK(new_wire_10), .D(_10__2_), .Q(tx_count16_2_) );
DFFPOSX1 DFFPOSX1_10 ( .CLK(new_wire_10), .D(_10__3_), .Q(tx_count16_3_) );
DFFPOSX1 DFFPOSX1_11 ( .CLK(new_wire_10), .D(_11__0_), .Q(txd_reg_0_) );
DFFPOSX1 DFFPOSX1_12 ( .CLK(new_wire_13), .D(_11__1_), .Q(txd_reg_1_) );
DFFPOSX1 DFFPOSX1_13 ( .CLK(new_wire_5), .D(_11__2_), .Q(txd_reg_2_) );
DFFPOSX1 DFFPOSX1_14 ( .CLK(new_wire_7), .D(_11__3_), .Q(txd_reg_3_) );
DFFPOSX1 DFFPOSX1_15 ( .CLK(new_wire_13), .D(_11__4_), .Q(txd_reg_4_) );
DFFPOSX1 DFFPOSX1_16 ( .CLK(new_wire_7), .D(_11__5_), .Q(txd_reg_5_) );
DFFPOSX1 DFFPOSX1_17 ( .CLK(new_wire_13), .D(_11__6_), .Q(txd_reg_6_) );
DFFPOSX1 DFFPOSX1_18 ( .CLK(new_wire_13), .D(_11__7_), .Q(txd_reg_7_) );
DFFPOSX1 DFFPOSX1_19 ( .CLK(new_wire_11), .D(_5__0_), .Q(_231__0_) );
DFFPOSX1 DFFPOSX1_20 ( .CLK(new_wire_11), .D(_5__1_), .Q(_231__1_) );
DFFPOSX1 DFFPOSX1_21 ( .CLK(new_wire_1), .D(_5__2_), .Q(_231__2_) );
DFFPOSX1 DFFPOSX1_22 ( .CLK(new_wire_1), .D(_5__3_), .Q(_231__3_) );
DFFPOSX1 DFFPOSX1_23 ( .CLK(new_wire_1), .D(_5__4_), .Q(_231__4_) );
DFFPOSX1 DFFPOSX1_24 ( .CLK(new_wire_7), .D(_5__5_), .Q(_231__5_) );
DFFPOSX1 DFFPOSX1_25 ( .CLK(new_wire_11), .D(_5__6_), .Q(_231__6_) );
DFFPOSX1 DFFPOSX1_26 ( .CLK(new_wire_7), .D(_5__7_), .Q(_231__7_) );
DFFPOSX1 DFFPOSX1_27 ( .CLK(new_wire_7), .D(_1_), .Q(_230_) );
DFFPOSX1 DFFPOSX1_28 ( .CLK(new_wire_7), .D(_6_), .Q(_232_) );
DFFPOSX1 DFFPOSX1_29 ( .CLK(new_wire_14), .D(_3_), .Q(rx_busy) );
DFFPOSX1 DFFPOSX1_30 ( .CLK(new_wire_3), .D(_4__0_), .Q(rx_count16_0_) );
DFFPOSX1 DFFPOSX1_31 ( .CLK(new_wire_3), .D(_4__1_), .Q(rx_count16_1_) );
DFFPOSX1 DFFPOSX1_32 ( .CLK(new_wire_3), .D(_4__2_), .Q(rx_count16_2_) );
DFFPOSX1 DFFPOSX1_33 ( .CLK(new_wire_8), .D(_4__3_), .Q(rx_count16_3_) );
DFFPOSX1 DFFPOSX1_34 ( .CLK(new_wire_3), .D(_2__0_), .Q(rx_bitcount_0_) );
DFFPOSX1 DFFPOSX1_35 ( .CLK(new_wire_3), .D(_2__1_), .Q(rx_bitcount_1_) );
DFFPOSX1 DFFPOSX1_36 ( .CLK(new_wire_3), .D(_2__2_), .Q(rx_bitcount_2_) );
DFFPOSX1 DFFPOSX1_37 ( .CLK(new_wire_4), .D(_2__3_), .Q(rx_bitcount_3_) );
DFFPOSX1 DFFPOSX1_38 ( .CLK(new_wire_11), .D(_7__0_), .Q(rxd_reg_0_) );
DFFPOSX1 DFFPOSX1_39 ( .CLK(new_wire_11), .D(_7__1_), .Q(rxd_reg_1_) );
DFFPOSX1 DFFPOSX1_40 ( .CLK(new_wire_11), .D(_7__2_), .Q(rxd_reg_2_) );
DFFPOSX1 DFFPOSX1_41 ( .CLK(new_wire_12), .D(_7__3_), .Q(rxd_reg_3_) );
DFFPOSX1 DFFPOSX1_42 ( .CLK(new_wire_1), .D(_7__4_), .Q(rxd_reg_4_) );
DFFPOSX1 DFFPOSX1_43 ( .CLK(new_wire_12), .D(_7__5_), .Q(rxd_reg_5_) );
DFFPOSX1 DFFPOSX1_44 ( .CLK(new_wire_12), .D(_7__6_), .Q(rxd_reg_6_) );
DFFPOSX1 DFFPOSX1_45 ( .CLK(new_wire_8), .D(_7__7_), .Q(rxd_reg_7_) );
DFFPOSX1 DFFPOSX1_46 ( .CLK(new_wire_4), .D(uart_rxd), .Q(uart_rxd1) );
DFFPOSX1 DFFPOSX1_47 ( .CLK(new_wire_4), .D(uart_rxd1), .Q(uart_rxd2) );
DFFPOSX1 DFFPOSX1_48 ( .CLK(new_wire_1), .D(_0__0_), .Q(enable16_counter_0_) );
DFFPOSX1 DFFPOSX1_49 ( .CLK(new_wire_1), .D(_0__1_), .Q(enable16_counter_1_) );
DFFPOSX1 DFFPOSX1_50 ( .CLK(new_wire_2), .D(_0__2_), .Q(enable16_counter_2_) );
DFFPOSX1 DFFPOSX1_51 ( .CLK(new_wire_8), .D(_0__3_), .Q(enable16_counter_3_) );
DFFPOSX1 DFFPOSX1_52 ( .CLK(new_wire_14), .D(_0__4_), .Q(enable16_counter_4_) );
DFFPOSX1 DFFPOSX1_53 ( .CLK(new_wire_14), .D(_0__5_), .Q(enable16_counter_5_) );
DFFPOSX1 DFFPOSX1_54 ( .CLK(new_wire_5), .D(_0__6_), .Q(enable16_counter_6_) );
DFFPOSX1 DFFPOSX1_55 ( .CLK(new_wire_5), .D(_0__7_), .Q(enable16_counter_7_) );
DFFPOSX1 DFFPOSX1_56 ( .CLK(new_wire_2), .D(_0__8_), .Q(enable16_counter_8_) );
DFFPOSX1 DFFPOSX1_57 ( .CLK(new_wire_5), .D(_0__9_), .Q(enable16_counter_9_) );
DFFPOSX1 DFFPOSX1_58 ( .CLK(new_wire_2), .D(_0__10_), .Q(enable16_counter_10_) );
DFFPOSX1 DFFPOSX1_59 ( .CLK(new_wire_5), .D(_0__11_), .Q(enable16_counter_11_) );
DFFPOSX1 DFFPOSX1_60 ( .CLK(new_wire_5), .D(_0__12_), .Q(enable16_counter_12_) );
DFFPOSX1 DFFPOSX1_61 ( .CLK(new_wire_6), .D(_0__13_), .Q(enable16_counter_13_) );
DFFPOSX1 DFFPOSX1_62 ( .CLK(new_wire_6), .D(_0__14_), .Q(enable16_counter_14_) );
DFFPOSX1 DFFPOSX1_63 ( .CLK(new_wire_6), .D(_0__15_), .Q(enable16_counter_15_) );
BUFX2 BUFX2_1_sized_sized ( .A(_13_), .Y(_13__bF_buf0) );
INVX4 INVX2_1_sized_sized_sized ( .A(tx_bitcount_1_), .Y(_15_) );
INVX4 INVX2_2_sized_sized_sized ( .A(tx_bitcount_3_), .Y(_16_) );
INVX1 INVX1_1_sized_sized ( .A(new_wire_15), .Y(_19_) );
INVX4 INVX2_3_sized_sized_sized ( .A(tx_bitcount_0_), .Y(_20_) );
INVX1 INVX1_2_sized_sized ( .A(tx_wr), .Y(_41_) );
INVX4 INVX2_4_sized_sized_sized ( .A(_233_), .Y(_44_) );
INVX1 INVX1_3_sized_sized ( .A(new_wire_25), .Y(_50_) );
INVX4 INVX2_5_sized_sized_sized ( .A(tx_bitcount_2_), .Y(_55_) );
INVX4 INVX2_6_sized_sized_sized ( .A(new_wire_21), .Y(_66_) );
INVX1 INVX1_4_sized_sized ( .A(tx_count16_3_), .Y(_78_) );
INVX1 INVX1_5_sized_sized ( .A(txd_reg_1_), .Y(_84_) );
INVX1 INVX1_6_sized_sized ( .A(txd_reg_2_), .Y(_88_) );
INVX1 INVX1_7_sized_sized ( .A(txd_reg_3_), .Y(_92_) );
INVX1 INVX1_8_sized_sized ( .A(txd_reg_4_), .Y(_96_) );
INVX1 INVX1_9_sized_sized ( .A(txd_reg_5_), .Y(_100_) );
INVX1 INVX1_10_sized_sized ( .A(txd_reg_6_), .Y(_104_) );
INVX1 INVX1_11_sized_sized ( .A(txd_reg_7_), .Y(_108_) );
INVX1 INVX1_12_sized_sized ( .A(tx_data[7]), .Y(_112_) );
INVX1 INVX1_13_sized_sized ( .A(_231__0_), .Y(_115_) );
INVX1 INVX1_14_sized_sized ( .A(rxd_reg_0_), .Y(_116_) );
INVX1 INVX1_15_sized_sized ( .A(uart_rxd2), .Y(_117_) );
INVX1 INVX1_16_sized_sized ( .A(rx_bitcount_2_), .Y(_119_) );
INVX4 INVX2_7_sized_sized_sized ( .A(rx_bitcount_1_), .Y(_120_) );
INVX1 INVX1_17_sized_sized ( .A(_231__1_), .Y(_130_) );
INVX1 INVX1_18_sized_sized ( .A(rxd_reg_1_), .Y(_131_) );
INVX1 INVX1_19_sized_sized ( .A(_231__2_), .Y(_132_) );
INVX1 INVX1_20_sized_sized ( .A(rxd_reg_2_), .Y(_133_) );
INVX1 INVX1_21_sized_sized ( .A(_231__3_), .Y(_134_) );
INVX1 INVX1_22_sized_sized ( .A(rxd_reg_3_), .Y(_135_) );
INVX1 INVX1_23_sized_sized ( .A(_231__4_), .Y(_136_) );
INVX1 INVX1_24_sized_sized ( .A(rxd_reg_4_), .Y(_137_) );
INVX1 INVX1_25_sized_sized ( .A(_231__5_), .Y(_138_) );
INVX1 INVX1_26_sized_sized ( .A(rxd_reg_5_), .Y(_139_) );
INVX1 INVX1_27_sized_sized ( .A(_231__6_), .Y(_140_) );
INVX1 INVX1_28_sized_sized ( .A(rxd_reg_6_), .Y(_141_) );
INVX1 INVX1_29_sized_sized ( .A(_231__7_), .Y(_142_) );
INVX1 INVX1_30_sized_sized ( .A(rxd_reg_7_), .Y(_143_) );
INVX1 INVX1_31_sized_sized ( .A(rx_ack), .Y(_144_) );
INVX1 INVX1_32_sized_sized ( .A(_126_), .Y(_149_) );
INVX1 INVX1_33_sized_sized ( .A(rx_bitcount_3_), .Y(_151_) );
INVX1 INVX1_34_sized_sized ( .A(rx_bitcount_0_), .Y(_152_) );
INVX4 INVX2_8_sized_sized_sized ( .A(rx_busy), .Y(_157_) );
INVX1 INVX1_35_sized_sized ( .A(_118_), .Y(_160_) );
INVX1 INVX1_36_sized_sized ( .A(rx_count16_2_), .Y(_166_) );
INVX1 INVX1_37_sized_sized ( .A(rx_count16_3_), .Y(_170_) );
INVX1 INVX1_38_sized_sized ( .A(_174_), .Y(_175_) );
INVX1 INVX1_39_sized_sized ( .A(_161_), .Y(_184_) );
INVX1 INVX1_40_sized_sized ( .A(enable16_counter_2_), .Y(_196_) );
INVX1 INVX1_41_sized_sized ( .A(new_wire_19), .Y(_206_) );
INVX1 INVX1_42_sized_sized ( .A(enable16_counter_8_), .Y(_209_) );
INVX1 INVX1_43_sized_sized ( .A(_217_), .Y(_218_) );
INVX1 INVX1_44_sized_sized ( .A(enable16_counter_13_), .Y(_221_) );
INVX1 INVX1_45_sized_sized ( .A(txd_reg_0_), .Y(_226_) );
INVX1 INVX1_46_sized_sized ( .A(_68_), .Y(_228_) );
BUFX2 BUFX2_2_sized_sized ( .A(_230_), .Y(rx_avail) );
BUFX2 BUFX2_3_sized_sized ( .A(_231__0_), .Y(rx_data[0]) );
BUFX2 BUFX2_4_sized_sized ( .A(_231__1_), .Y(rx_data[1]) );
BUFX2 BUFX2_5_sized_sized ( .A(_231__2_), .Y(rx_data[2]) );
BUFX2 BUFX2_6_sized_sized ( .A(_231__3_), .Y(rx_data[3]) );
BUFX2 BUFX2_7_sized_sized ( .A(_231__4_), .Y(rx_data[4]) );
BUFX2 BUFX2_8_sized_sized ( .A(_231__5_), .Y(rx_data[5]) );
BUFX2 BUFX2_9_sized_sized ( .A(_231__6_), .Y(rx_data[6]) );
BUFX2 BUFX2_10_sized_sized ( .A(_231__7_), .Y(rx_data[7]) );
BUFX2 BUFX2_11_sized_sized ( .A(_232_), .Y(rx_error) );
BUFX2 BUFX2_12_sized_sized ( .A(_233_), .Y(tx_busy) );
BUFX2 BUFX2_13_sized_sized ( .A(_234_), .Y(uart_txd) );
BUFX2 new_buffer_1_sized_sized ( .A(clk_bF_buf6), .Y(new_wire_1) );
BUFX2 new_buffer_2_sized_sized ( .A(clk_bF_buf6), .Y(new_wire_2) );
BUFX2 new_buffer_3_sized_sized ( .A(clk_bF_buf5), .Y(new_wire_3) );
BUFX2 new_buffer_4_sized_sized ( .A(clk_bF_buf5), .Y(new_wire_4) );
BUFX2 new_buffer_5_sized_sized ( .A(clk_bF_buf4), .Y(new_wire_5) );
BUFX2 new_buffer_6_sized_sized ( .A(clk_bF_buf4), .Y(new_wire_6) );
BUFX2 new_buffer_7_sized_sized ( .A(clk_bF_buf3), .Y(new_wire_7) );
BUFX2 new_buffer_8_sized_sized ( .A(clk_bF_buf3), .Y(new_wire_8) );
BUFX2 new_buffer_9_sized_sized ( .A(clk_bF_buf2), .Y(new_wire_9) );
BUFX2 new_buffer_10_sized_sized ( .A(clk_bF_buf2), .Y(new_wire_10) );
BUFX2 new_buffer_11_sized_sized ( .A(clk_bF_buf1), .Y(new_wire_11) );
BUFX2 new_buffer_12_sized_sized ( .A(clk_bF_buf1), .Y(new_wire_12) );
BUFX2 new_buffer_13_sized_sized ( .A(clk_bF_buf0), .Y(new_wire_13) );
BUFX2 new_buffer_14_sized_sized ( .A(clk_bF_buf0), .Y(new_wire_14) );
BUFX2 new_buffer_15_sized_sized ( .A(_18_), .Y(new_wire_15) );
BUFX2 new_buffer_16_sized_sized ( .A(_18_), .Y(new_wire_16) );
BUFX2 new_buffer_17_sized_sized ( .A(_23_), .Y(new_wire_17) );
BUFX2 new_buffer_18_sized_sized ( .A(_23_), .Y(new_wire_18) );
BUFX2 new_buffer_19_sized_sized ( .A(_27_), .Y(new_wire_19) );
BUFX2 new_buffer_20_sized_sized ( .A(_27_), .Y(new_wire_20) );
BUFX2 new_buffer_21_sized_sized ( .A(_35_), .Y(new_wire_21) );
BUFX2 new_buffer_22_sized_sized ( .A(_35_), .Y(new_wire_22) );
BUFX2 new_buffer_23_sized_sized ( .A(_38_), .Y(new_wire_23) );
BUFX2 new_buffer_24_sized_sized ( .A(_38_), .Y(new_wire_24) );
BUFX2 new_buffer_25_sized_sized ( .A(_42_), .Y(new_wire_25) );
BUFX2 new_buffer_26_sized_sized ( .A(_42_), .Y(new_wire_26) );
BUFX2 new_buffer_27_sized_sized ( .A(_45_), .Y(new_wire_27) );
BUFX2 new_buffer_28_sized_sized ( .A(_45_), .Y(new_wire_28) );
BUFX2 new_buffer_29_sized_sized ( .A(_48_), .Y(new_wire_29) );
BUFX2 new_buffer_30_sized_sized ( .A(_48_), .Y(new_wire_30) );
BUFX2 new_buffer_31_sized_sized ( .A(_69_), .Y(new_wire_31) );
BUFX2 new_buffer_32_sized_sized ( .A(_69_), .Y(new_wire_32) );
BUFX2 new_buffer_33_sized_sized ( .A(_83_), .Y(new_wire_33) );
BUFX2 new_buffer_34_sized_sized ( .A(_83_), .Y(new_wire_34) );
BUFX2 new_buffer_35_sized_sized ( .A(_129_), .Y(new_wire_35) );
BUFX2 new_buffer_36_sized_sized ( .A(_129_), .Y(new_wire_36) );
BUFX2 new_buffer_37_sized_sized ( .A(_193_), .Y(new_wire_37) );
BUFX2 new_buffer_38_sized_sized ( .A(_193_), .Y(new_wire_38) );
BUFX2 new_buffer_39_sized_sized ( .A(_194_), .Y(new_wire_39) );
BUFX2 new_buffer_40_sized_sized ( .A(_194_), .Y(new_wire_40) );
BUFX2 new_buffer_41_sized_sized ( .A(_194_), .Y(new_wire_41) );
endmodule
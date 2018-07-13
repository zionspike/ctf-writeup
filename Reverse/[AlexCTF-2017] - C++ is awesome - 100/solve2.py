
init_string = "L3t_ME_T3ll_Y0u_S0m3th1ng_1mp0rtant_A_{FL4G}_W0nt_b3_3X4ctly_th4t_345y_t0_c4ptur3_H0wev3r_1T_w1ll_b3_C00l_1F_Y0u_g0t_1t"

flag = ""

for x in [5, 54, 101, 7, 39, 38, 45, 1, 3, 0, 13, 86, 1, 3, 101, 3, 45, 22, 2, 21, 3, 101, 0, 41, 68, 68, 1, 68, 43]:
	flag = flag + init_string[x]

print "Flag: " + flag




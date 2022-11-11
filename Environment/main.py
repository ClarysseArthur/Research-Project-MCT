from Intersection import Lane, Approach, Intersection, Exit, Trafficlight

# Exit N
exit_n_r = Lane([0], None, True, None)
exit_n = Exit(0, [exit_n_r])

# Exit E
exit_e_r = Lane([0], None, True, None)
exit_e_l = Lane([0], None, True, None)
exit_e = Exit(1, [exit_e_r, exit_e_l])

# Exit S
exit_s_r = Lane([0], None, True, None)
exit_s = Exit(2, [exit_s_r])

# Exit W
exit_w_r = Lane([0], None, True, None)
exit_w_l = Lane([0], None, True, None)
exit_w = Exit(3, [exit_w_r, exit_w_l])

# Approach N
traffic_light_r = Trafficlight(0, 10, 10, [1], 0, 1, 2)
traffic_light_l = Trafficlight(1, 10, 10, [0, 2], 0, 1, 2)

lane_r = Lane([1], traffic_light_r, False, [exit_w_r])
lane_l = Lane([0, 2], traffic_light_l, False, [exit_s_r, exit_e_l])

approach_n = Approach(0, [lane_r, lane_l], 90)

# Approach E
traffic_light_r = Trafficlight(2, 10, 10, [0, 1], 0, 1, 2)
traffic_light_m = Trafficlight(3, 10, 10, [0], 0, 1, 2)
traffic_light_l = Trafficlight(4, 10, 10, [2], 0, 1, 2)

lane_r = Lane([0, 1], traffic_light_r, False, [exit_n_r, exit_w_r])
lane_m = Lane([0], traffic_light_m, False, [exit_w_l])
lane_l = Lane([2], traffic_light_l, False, [exit_s_r])

approach_e = Approach(1, [lane_r, lane_m, lane_l], 0)

# Approach S
traffic_light_r = Trafficlight(5, 10, 10, [0, 1], 0, 1, 2)
traffic_light_l = Trafficlight(6, 10, 10, [2], 0, 1, 2)

lane_r = Lane([0, 1], traffic_light_r, False, [exit_e_r, exit_n_r])
lane_l = Lane([2], traffic_light_l, False, [exit_w_l])

approach_s = Approach(2, [lane_r, lane_l], 270)

# Approach W
traffic_light_r = Trafficlight(7, 10, 10, [0, 1], 0, 1, 2)
traffic_light_m = Trafficlight(8, 10, 10, [0], 0, 1, 2)
traffic_light_l = Trafficlight(9, 10, 10, [2], 0, 1, 2)

lane_r = Lane([0, 1], traffic_light_r, False, [exit_s_r, exit_e_r])
lane_m = Lane([0], traffic_light_m, False, [exit_e_l])
lane_l = Lane([2], traffic_light_l, False, [exit_n_r])

approach_w = Approach(3, [lane_r, lane_m, lane_l], 180)



# Intersection
intersection = Intersection([approach_n, approach_e, approach_s, approach_w], [exit_n, exit_e, exit_s, exit_w])
intersection.generate_traffic(1000)
print(intersection.get_cars_per_lane())
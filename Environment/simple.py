from Intersection import Lane, Approach, Intersection, Exit, Trafficlight, TrafficLightGroup

exit_n_r = Lane([0], None, True, None)
exit_n = Exit(0, [exit_n_r])

exit_e_r = Lane([0], None, True, None)
exit_e = Exit(1, [exit_e_r])

exit_s_r = Lane([0], None, True, None)
exit_s = Exit(2, [exit_s_r])

exit_w_r = Lane([0], None, True, None)
exit_w = Exit(3, [exit_w_r])

traffic_light_n_r = Trafficlight(0, [0, 1, 2], 0, 1, 2)
lane_n_r = Lane([0, 1, 2], traffic_light_n_r, False, [exit_w_r])
lane_n_l = Lane([0, 1, 2], traffic_light_n_r, False, [exit_s_r])
lane_n_m = Lane([0, 1, 2], traffic_light_n_r, False, [exit_e_r])
lane_n_mm = Lane([0, 1, 2], traffic_light_n_r, False, [exit_e_r])

traffic_light_e_r = Trafficlight(1, [0, 1, 2], 0, 1, 2)
lane_e_r = Lane([0, 1, 2], traffic_light_e_r, False, [exit_n_r])
lane_e_l = Lane([0, 1, 2], traffic_light_e_r, False, [exit_w_r])
lane_e_m = Lane([0, 1, 2], traffic_light_e_r, False, [exit_s_r])

traffic_light_s_r = Trafficlight(2, [0, 1, 2], 0, 1, 2)
lane_s_r = Lane([0, 1, 2], traffic_light_s_r, False, [exit_e_r])
lane_s_l = Lane([0, 1, 2], traffic_light_s_r, False, [exit_n_r])
# lane_s_m = Lane([0, 1, 2], traffic_light_s_r, False, [exit_w_r])

traffic_light_w_r = Trafficlight(3, [0, 1, 2], 0, 1, 2)
lane_w_r = Lane([0, 1, 2], traffic_light_w_r, False, [exit_s_r])

approach_n = Approach(0, [lane_n_r, lane_n_l, lane_n_m, lane_n_mm], 90)
approach_e = Approach(1, [lane_e_r, lane_e_l, lane_e_m], 0)
approach_s = Approach(2, [lane_s_r, lane_s_l], 270)
approach_w = Approach(3, [lane_w_r], 180)

traffic_light_group_ns = TrafficLightGroup([traffic_light_n_r, traffic_light_s_r])
traffic_light_group_ew = TrafficLightGroup([traffic_light_e_r, traffic_light_w_r])

intersection = Intersection([approach_n, approach_e, approach_s, approach_w], [exit_n, exit_e, exit_s, exit_w], [traffic_light_group_ns, traffic_light_group_ew])
intersection.generate_traffic(100)

print(intersection.get_cars_per_lane())

intersection.close()
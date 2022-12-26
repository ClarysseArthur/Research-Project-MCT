from Intersection import Lane, Approach, Intersection, Exit, Trafficlight, TrafficLightGroup
import random
import time

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
traffic_light_n_r = Trafficlight(0, [1], 0, 1, 2)
traffic_light_n_l = Trafficlight(1, [0, 2], 0, 1, 2)

lane_n_r = Lane([1], traffic_light_n_r, False, [exit_w_r])
lane_n_l = Lane([0, 2], traffic_light_n_l, False, [exit_s_r, exit_e_l])

approach_n = Approach(0, [lane_n_r, lane_n_l], 90)

# Approach E
traffic_light_e_r = Trafficlight(2, [0, 1], 0, 1, 2)
traffic_light_e_m = Trafficlight(3, [0], 0, 1, 2)
traffic_light_e_l = Trafficlight(4, [2], 0, 1, 2)

lane_e_r = Lane([0, 1], traffic_light_e_r, False, [exit_n_r, exit_w_r])
lane_e_m = Lane([0], traffic_light_e_m, False, [exit_w_l])
lane_e_l = Lane([2], traffic_light_e_l, False, [exit_s_r])

approach_e = Approach(1, [lane_e_r, lane_e_m, lane_e_l], 0)

# Approach S
traffic_light_s_r = Trafficlight(5, [0, 1], 0, 1, 2)
traffic_light_s_l = Trafficlight(6, [2], 0, 1, 2)

lane_s_r = Lane([0, 1], traffic_light_s_r, False, [exit_e_r, exit_n_r])
lane_s_l = Lane([2], traffic_light_s_l, False, [exit_w_l])

approach_s = Approach(2, [lane_s_r, lane_s_l], 270)

# Approach W
traffic_light_w_r = Trafficlight(7, [0, 1], 0, 1, 2)
traffic_light_w_m = Trafficlight(8, [0], 0, 1, 2)
traffic_light_w_l = Trafficlight(9, [2], 0, 1, 2)

lane_w_r = Lane([0, 1], traffic_light_w_r, False, [exit_s_r, exit_e_r])
lane_w_m = Lane([0], traffic_light_w_m, False, [exit_e_l])
lane_w_l = Lane([2], traffic_light_w_l, False, [exit_n_r])

approach_w = Approach(3, [lane_w_r, lane_w_m, lane_w_l], 180)

traffic_light_group_ns_s = TrafficLightGroup([traffic_light_n_r, traffic_light_n_l, traffic_light_s_r, traffic_light_s_l])
traffic_light_group_ew_s = TrafficLightGroup([traffic_light_e_r, traffic_light_e_m, traffic_light_w_r, traffic_light_w_m])
traffic_light_group_ew_l = TrafficLightGroup([traffic_light_e_l, traffic_light_w_l])

# Intersection
intersection = Intersection([approach_n, approach_e, approach_s, approach_w], [exit_n, exit_e, exit_s, exit_w], [traffic_light_group_ns_s, traffic_light_group_ew_s, traffic_light_group_ew_l])
intersection.generate_traffic(100)

# intersection.render()

action_space = [0, 1, 2, 3]

for x in range(100):
    print(intersection.step(random.choice(action_space)))

print(intersection.close())
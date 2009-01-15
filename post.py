clearance = 5
rapid_down_to_height = 2
final_depth = -0.1
tool_diameter = 3
spindle(7000)
feedrate(100)
tool_change(1)
k1 = kurve.new()
kurve.add_point(k1, 0, -13, -6, 0, 0)
kurve.add_point(k1, 0, -4, 4, 0, 0)
kurve.add_point(k1, 0, 11, 0, 0, 0)
kurve.add_point(k1, 0, 29, 2, 0, 0)
profile(k1, 'left', tool_diameter/2, clearance, rapid_down_to_height, final_depth)
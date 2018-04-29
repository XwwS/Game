import pygal
from die import Die

die = Die()

results = []
for roll_num in range(50000):
	first_value = die.roll()
	second_value = die.roll()
	results.append(first_value+second_value)

# 分析结果
frequencies = []
for value in range(2, 2*die.num_side):
	frequency = results.count(value)
	frequencies.append(frequency / 50000)

print (frequencies)
# # 对结果进行可视化
# hist = pygal.Bar()

# hist.title = "The Results"
# hist.x_labels = list(range(2, 2*die.num_side))
# hist.x_title = 'Results'
# hist.y_title = "Frequency of Result"

# hist.add("D6D6", frequencies)
# hist.render_to_file('die_visual.svg')

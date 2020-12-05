# -*- coding: utf-8 -*-
""" 
    @author  : dingyaru
    @version : 
    @time    : 2020/12/5 10:00
    @function: 移出某一类并将其他类前移，现在要移除的是门这个类。
"""
import os
import numpy as np

np.set_printoptions(suppress=True)
labels_path = r'G:\xiamen-project-train-data-3\labels'
count = 0
for file in os.listdir(labels_path):
	# for file in os.listdir(os.path.join(labels_path, f)):  # train val
	data = ''
	with open(os.path.join(labels_path, file), 'r+') as labels_file:
		strs = labels_file.readlines()
		labels_list = []
		for line in strs:
			print('line', line)
			line_str = ''
			if int(line.split()[0]) != 32:
				if int(line.split()[0]) < 32:
					data += line
				elif int(line.split()[0]) > 32:
					print(line)
					strs_1_5 = '%s ' % (int(line.split()[0]) - 1)
					for i in range(5):
						if i != 0:
							strs_1_5 += line.split()[i] + ' '
					data += strs_1_5 + '\n'
		print(data)
	with open(os.path.join(labels_path, file), 'w+') as labels_file:
		labels_file.writelines(data)
	if not os.path.getsize(os.path.join(labels_path, file)):
		os.remove(os.path.join(labels_path, file))
		count += 1
		print('删除的图片个数：', count)

#!#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# Создано SotGE Ltd.
# Автор: Сорокин Максим Евгеньевич


import sys
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def run(arg):
	img = Image.open("../upload/"+arg)
	img = img.convert('L')

	plt.imshow((np.asarray(img) > 200) * 1.0)
	plt.show()

	img.save("../upload/"+arg)
	
	print(arg)


if __name__ == "__main__":
	arg = sys.argv[1]
	run(arg)

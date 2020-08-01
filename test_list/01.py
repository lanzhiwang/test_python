#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time


big_list = range(1000000)

big_dict = {}
for key in big_list:
    big_dict[key] = None

start_time = time.time()
for _ in range(1000000):
    target = random.randint(0, 1000000)
    print target in big_list
end_time = time.time()

print end_time - start_time

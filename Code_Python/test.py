"""
Filters for time series.

Copyright (c) 2020 Gabriele Gilardi

ToDo:
- in comments write what filters do
- is necessary to copy X for Y untouched?
- decide default values in functions
- check conditions on P and N
- why lag plot gives errors
- fix plotting function
- example for alpha-beta-gamma using variable sigma as in financial time series
  (see Ehler)
- example using noisy multi-sine-waves
- synt: boot, paper Vinod (as a class?)
- vectors must be ( .., 1)
- reduce the vector diff by one and pass initial value
  (with zero/one as default)
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

import filters as flt
import synthetic as syn

# Read data to filter
if len(sys.argv) != 2:
    print("Usage: python test.py <data_file>")
    sys.exit(1)
data_file = sys.argv[1] + '.csv'

# Read data from a csv file
data = np.loadtxt(data_file, delimiter=',')
n_samples = data.shape[0]
data = data.reshape(n_samples, -1)

np.random.seed(1294404794)

# spx = flt.Filter(data)

# res, bb, aa = spx.SincFunction(2, 50)
# print(bb)
# print(aa)
# utl.plot_frequency_response(bb, aa)
# utl.plot_lag_response(bb, aa)
# sigma_x = 0.1
# sigma_v = 0.1 * np.ones(n_samples)
# res = spx.Kalman(sigma_x=sigma_x, sigma_v=sigma_v, dt=1.0, abg_type="abg")
# alpha = 0.5
# beta = 0.005
# gamma = 0.0
# Yc, Yp = spx.ABG(alpha=alpha, beta=beta, gamma=gamma, dt=1.0)
# signals = (spx.data[:, 0], Yc[:, 0], Yp[:, 0])
# utl.plot_signals(signals, 0, 50)

# t, f = utl.synthetic_wave([1., 2., 3.], A=None, PH=None, num=30)
# plt.plot(t,f)
# plt.show()
aa = np.array([
        [ 0.8252,  0.2820],
        [ 1.3790,  0.0335],
        [-1.0582, -1.3337],
        [-0.4686,  1.1275],
        [-0.2725,  0.3502],
        [ 1.0984, -0.2991],
        [-0.2779,  0.0229],
        [ 0.7015, -0.2620],
        [-2.0518, -1.7502],
        [-0.3538, -0.2857],
        [-0.8236, -0.8314],
        [-1.5771, -0.9792],
        [ 0.5080, -1.1564]])
# synt_aa = utl.synthetic_series(data, False)
# plt.plot(synt_aa)
# plt.plot(data)
# plt.show()
print(data[0:10, :])
bb = syn.value2diff(data, mode='V')
print(bb[0:10, :])
bb[0, 0] = 1399.48
cc = syn.diff2value(bb, mode='V')
print(cc[0:10, :])
from matplotlib.pylab import *
from numpy import *
import time

ts = time.time()
x = linspace(0, 2 * pi, 256)
y = sin(x)


def factorizer(value):
    factor_number = 0
    y_len = len(value)

    while y_len != 1:
        factor_number += 1
        y_len = y_len / 2
        if y_len < 1:
            print('{:^170}'.format('ERROR: number of data is not factorizable only by 2'))
            print('Time take for the process: ', time.time() - ts)
            exit()

    return factor_number


def bit_reverser(dataset):
    dataset = list(dataset)
    new_dataset = [0 for _ in range(len(dataset))]
    index_len = factorizer(dataset)

    for i in dataset:
        binary_index = bin(dataset.index(i))[2:]
        while not len(binary_index) == index_len:
            binary_index = '0' + binary_index

        new_index = int(binary_index[::-1], 2)
        new_dataset[new_index] = i

    return new_dataset


def fast_fourier_transform(fx):
    shuffled_dataset = array(bit_reverser(fx))
    pwr = 0
    pwr_1 = factorizer(fx)

    while not pwr_1 == 0:
        pwr += 1
        rows_number = 2 ** pwr_1
        elements_number = 2 ** pwr
        twiddle_factor = array([])
        shuffled_dataset = shuffled_dataset.reshape(int(rows_number), int(shuffled_dataset.size / rows_number))
        new_dataset = array([])
        dummy_new_dataset = []

        for i in range(elements_number):
            t_factor = exp(1j * 2 * pi * i / elements_number)
            twiddle_factor = concatenate((twiddle_factor, [t_factor]))
        twiddle_factor = twiddle_factor.reshape(2, int(twiddle_factor.size / 2))

        for i in range(0, shuffled_dataset.shape[0], 2):
            for j in range(twiddle_factor.shape[0]):
                dummy_new_dataset.append(shuffled_dataset[i] + shuffled_dataset[i + 1] * twiddle_factor[j])
                new_dataset = array(dummy_new_dataset)

        shuffled_dataset = new_dataset
        pwr_1 -= 1

    return shuffled_dataset.reshape(1, shuffled_dataset.size)


Ck = fast_fourier_transform(y)
mode_sqr = real(Ck * conj(Ck) / (y.size ** 2))

inv_Ck = fast_fourier_transform(conj(Ck)[0]) / len(y)

fig, axs = plt.subplots(2)
axs[0].plot(x, real(mode_sqr[0]))
axs[0].set_xlabel("x")
axs[0].set_ylabel("|C(k)|\u00b2")
axs[0].set_title("C(k)|\u00b2 vs x")
axs[1].plot(x, real(inv_Ck[0]))
axs[1].set_xlabel("x")
axs[1].set_ylabel("inv Ck")
axs[1].set_title("inv Ck vs x")
print('Time take for the process: ', time.time() - ts)
show()

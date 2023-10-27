import numpy as np
import pandas as pd

from typing import Union, Tuple
from ft_visualiser.waveform import Waveform


class FourierTransform:

    _DATA_COLUMNS = ["f", "polar", "x'_(real)", "x'_(imag)", "mag", "phase", "cm_(real)", "cm_(imag)"]

    def __init__(self, x: Union[np.array, Waveform]):
        """

        :param x:
        """

        if type(x) is Waveform:
            self._x = x.data

        self._N = len(self._x) - 1

        array = np.zeros(shape=(self._N, len(self._DATA_COLUMNS)))
        array[:, 0] = np.arange(0, self._N)  # Frequency range [k]
        polar_data = [None] * self._N

        for index, k in enumerate(array[:, 0]):
            X, polar_data[index] = self.compute_ft(k=k)
            array[index, 2] = X.real
            array[index, 3] = X.imag

        # Calculate frequency magnitude and phase
        array[:, 4] = abs(np.sqrt(array[:, 2] ** 2, array[:, 3] ** 2))
        array[:, 5] = np.arctan(array[:, 3] / array[:, 2])

        self._df = pd.DataFrame(data=array, columns=self._DATA_COLUMNS)
        self._df.polar = polar_data

    @property
    def x(self) -> np.array:
        return self._x

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    def compute_ft(self, k) -> Tuple[np.array, np.array]:
        """

        :param k:
        :return:
        """

        X: complex = 0
        polar_data: np.array = np.zeros(shape=(self._N, 2))
        for n in range(self._N):
            polar = self._x[n, 1] * np.exp(2j * np.pi * k * n / self._N)
            polar_data[n, :] = [polar.real, polar.imag]
            X += polar

        return X, polar_data

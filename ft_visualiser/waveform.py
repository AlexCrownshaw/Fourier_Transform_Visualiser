from typing import Union

import numpy as np


class Waveform:

    def __init__(self, freq: float, amp: float = 1, phase: float = 0, offset: float = 1, time: float = 1, size: int = 1e3,  base: str = "cos"):
        """

        :param freq:
        :param amp:
        :param phase:
        :param time:
        :param size:
        :param base:
        """

        self._BASE_FUNCS = {"sin": self._sin,
                            "cos": self._cos}

        if base not in self._BASE_FUNCS.keys():
            raise Exception(f"ERROR: Invalid base type. Choose from {self._BASE_FUNCS.keys()}")

        self._freq = freq
        self._amp: float = amp
        self._phase: float = phase
        self._offset: float = offset
        self._time: float = time
        self._size: int = int(size)
        self._base: str = base

        self._data: np.array = np.zeros(shape=(self._size, 2))
        self._data[:, 0] = np.round(np.arange(0, self._time, self._time / self._size), 3)

        self._BASE_FUNCS[self._base]()

    @property
    def freq(self) -> float:
        return self._freq

    @property
    def amp(self) -> float:
        return self._amp

    @property
    def phase(self) -> float:
        return self._phase

    @property
    def time(self) -> float:
        return self._time

    @property
    def size(self) -> float:
        return self._size

    @property
    def base(self) -> str:
        return self._base

    @property
    def data(self) -> np.array:
        return self._data

    """ BASE FUNCTIONS START """

    def _sin(self) -> None:
        """
        x(t) = Acos(ωt + φ)
        :return:
        """

        self._data[:, 1] = self._amp * np.sin(2 * np.pi * self._freq * self._data[:, 0] + self._phase) + self._offset

    def _cos(self) -> None:
        """
        x(t) = Acos(ωt + φ)
        :return:
        """

        self._data[:, 1] = self._amp * np.cos(2 * np.pi * self._freq * self._data[:, 0] + self._phase) + self._offset

    """ BASE FUNCTIONS STOP """

    def add(self, data: Union[object, np.array]) -> None:
        """

        :param data:
        :return:
        """

        if type(data) is Waveform:
            data = data.data[:, 1]

        self._data[:, 1] = self._data[:, 1] + data

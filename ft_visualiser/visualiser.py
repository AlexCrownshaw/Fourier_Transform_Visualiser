import os
import sys
import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import gridspec

from ft_visualiser.fourier_transform import FourierTransform


class Visualiser:

    def __init__(self, ft: FourierTransform, path: str = None):
        """

        :param ft:
        """

        self._df = ft.df
        self._x = ft.x

        if path is None:
            self._path = os.path.dirname(sys.argv[0])
        else:
            self._path = path

    def animate(self, show: bool = True, save: bool = False) -> None:
        """

        :param show:
        :param save:
        :return:
        """

        frames = int(len(self._df) / 2)

        fig = plt.figure(figsize=(16, 8))
        gs = gridspec.GridSpec(2, 2, width_ratios=[2.5, 1])
        ax_wf = fig.add_subplot(gs[0])
        ax_wf_pl = fig.add_subplot(gs[1], projection='polar')
        ax_ft = fig.add_subplot(gs[2])
        ax_ft_pl = fig.add_subplot(gs[3])

        self.plot_waveform(ax=ax_wf, show=False)
        self.plot_polar_waveform(ax=ax_wf_pl, show=False)
        ax_ft = self.plot_ft(k_range=[0, 1], ax=ax_ft, show=False)
        ax_ft_pl = self.plot_ft_polar(k_index=0, ax=ax_ft_pl, show=False)

        anim = animation.FuncAnimation(fig=fig, func=self._update_frame, frames=frames,
                                       fargs=(ax_ft, ax_ft_pl), interval=50, blit=False)

        if save:
            writer_gif = animation.PillowWriter(fps=60)
            file_path = os.path.join(self._path, f"FT_visualiser_{str(time.strftime('%d-%m-%y_%H-%M-%S'))}.gif")
            anim.save(filename=file_path, writer=writer_gif)

        if show:
            plt.show()

    def _update_frame(self, num: int, ax_ft: plt.axes, ax_ft_pl: plt.axes) -> list:
        """

        :param num:
        :param ax_ft:
        :param ax_ft_pl:
        :return:
        """

        k_index = num * 2
        k_range = [0, k_index]

        plt.sca(ax_ft)
        plt.cla()
        ax_ft = self.plot_ft(k_range=k_range, ax=ax_ft, show=False)

        plt.sca(ax_ft_pl)
        plt.cla()
        ax_ft_pl = self.plot_ft_polar(k_index=k_index, ax=ax_ft_pl, show=False)

        return [ax_ft, ax_ft_pl]

    def plot_waveform(self, ax: plt.axes = None, show: bool = True, save: bool = False) -> plt.axes:
        """

        :param ax:
        :param show:
        :param save:
        :return:
        """

        if ax is None:
            fig, ax = plt.subplots()

        ax.plot(self._x[:, 0], self._x[:, 1])
        ax.set_title("Waveform [x(t)]")
        ax.set_xlabel("t")
        ax.set_ylabel("x")
        ax.grid()

        if save:
            plt.savefig(os.path.join(self._path, f"waveform_{str(time.strftime('%d-%m-%y_%H-%M-%S'))}.png"))

        if show:
            plt.show()

        return ax

    def plot_polar_waveform(self, ax: plt.axes = None, show: bool = True, save: bool = False) -> plt.axes:
        """

        :param ax:
        :param show:
        :param save:
        :return:
        """

        if ax is None:
            plt.Figure()
            ax = plt.subplot(111, projection='polar')

        rad = np.arange(0, 2 * np.pi, 2 * np.pi / len(self._x[:, 0]))

        plt.sca(ax)
        plt.polar(rad, self._x[:, 1])
        ax.set_title("Polar Waveform [x(t)]")
        ax.grid()

        if save:
            plt.savefig(os.path.join(self._path, f"polar_waveform_{str(time.strftime('%d-%m-%y_%H-%M-%S'))}.png"))

        if show:
            plt.show()

        return ax

    def plot_ft(self, k_range: list = None, ax: plt.axes = None, show: bool = True, save: bool = False) -> plt.axes:
        """

        :param k_range:
        :param ax:
        :param show:
        :param save:
        :return:
        """

        if ax is None:
            fig, ax = plt.subplots()

        if k_range is None:
            k_range = [0, len(self._df)]

        ax.plot(self._df.f.iloc[k_range[0]: k_range[1]], self._df.mag.iloc[k_range[0]: k_range[1]])

        ax.set_title("Fourier Transform (Mag)")
        ax.set_xlabel("f [Hz]")
        ax.set_ylabel("x'")
        ax.grid()

        if save:
            plt.savefig(os.path.join(self._path, f"FT_{str(time.strftime('%d-%m-%y_%H-%M-%S'))}.png"))

        if show:
            plt.show()

        return ax

    def plot_ft_polar(self, k_index: int, ax: plt.axes = None, show: bool = True, save: bool = False) -> plt.axes:
        """

        :param k_index:
        :param ax:
        :param show:
        :param save:
        :return:
        """

        if ax is None:
            fig, ax = plt.subplots()

        ax.plot(self._df.polar.iloc[k_index][:, 0], self._df.polar.iloc[k_index][:, 1], linewidth=0.1)
        ax.plot(sum(self._df.polar.iloc[k_index][:, 0]) / len(self._df.polar.iloc[k_index][:, 0]),
                sum(self._df.polar.iloc[k_index][:, 1]) / len(self._df.polar.iloc[k_index][:, 1]),
                marker="x", label="CoM")
        ax.quiver(0, 0, self._df["x'_(real)"].iloc[k_index], self._df["x'_(imag)"].iloc[k_index],
                  label=f"mag={round(self._df.mag.iloc[k_index], 3)}, phase={round(self._df.phase.iloc[k_index], 3)}")

        ax.set_title(f"Fourier Transform (polar real/imag - f={self._df.f.iloc[k_index]})")
        ax.set_xlabel("real")
        ax.set_ylabel("imag")
        ax.legend(loc="upper left")
        ax.grid()

        if save:
            plt.savefig(os.path.join(self._path, f"FT_polar_{str(time.strftime('%d-%m-%y_%H-%M-%S'))}.png"))

        if show:
            plt.show()

        return ax

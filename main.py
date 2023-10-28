from ft_visualiser.waveform import Waveform
from ft_visualiser.fourier_transform import FourierTransform
from ft_visualiser.visualiser import Visualiser

""" PARAMETERS START """
FREQ1 = 10  # Hz
FREQ2 = 100
SAVE_PATH = r"C:\Dev\Fourier_Transform_Visualiser\Solutions"
""" PARAMETERS STOP """


def main():
    w1 = Waveform(freq=FREQ1)
    w2 = Waveform(freq=FREQ2)
    w1.add(data=w2)

    ft = FourierTransform(x=w1)

    vis = Visualiser(ft=ft, path=SAVE_PATH)
    vis.plot_waveform(save=True)
    vis.plot_polar_waveform(save=True)
    vis.plot_ft(save=True)
    vis.plot_ft_polar(k_index=10, save=True)
    vis.plot_ft_polar(k_index=100, save=True)
    vis.animate()


if __name__ == "__main__":
    main()

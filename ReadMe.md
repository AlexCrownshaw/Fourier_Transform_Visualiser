# Fourier Transform Visualiser
This project allows users to create their own complex time domain waveforms before converting to the frequency domain
using a discrete Fourier transform. This project also includes a visualiser module which can create animated gifs showing
the complex components of each frequency bin, offering some insight to the inner workings of the Fourier transform

## Installation
```commandline
pip install git+https://github.com/AlexCrownshaw/Fourier_Transform_Visualiser.git@master
```

## Clone
```commandline
git clone https://github.com/AlexCrownshaw/Fourier_Transform_Visualiser.git
```

## Usage Example
The following example creates a complex waveform made up of two sine waves at 10Hz and 100Hz. 
```python
from ft_visualiser import Waveform
from ft_visualiser import FourierTransform
from ft_visualiser import Visualiser

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
```

![alt text](https://github.com/AlexCrownshaw/Fourier_Transform_Visualiser/blob/master/Solutions/Animation_Still.png "Animation_Still")
![alt text](https://github.com/AlexCrownshaw/Fourier_Transform_Visualiser/blob/master/Solutions/FT_polar_28-10-23_12-18-21.png "FT_Polar")
![alt text](https://github.com/AlexCrownshaw/Fourier_Transform_Visualiser/blob/master/Solutions/FT_polar_28-10-23_12-18-26.png "FT_Polar")
![alt text](https://github.com/AlexCrownshaw/Fourier_Transform_Visualiser/blob/master/Solutions/FT_28-10-23_12-18-15.png "FT")

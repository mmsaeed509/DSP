### install Dependencies:

```bash
pip install -r lib.txt
```

### Problem 1 [Fourier Transform]- *`5pts`*

- [1] Generate a *`1`* sec digital signal from your microphone pronouncing your name and save it as an uncompressed wav audio `Rec.wav` file. You can use [**`Audacity`**](https://www.audacityteam.org/) or any other external software to generate the wav audio file.
- [2] Apply all-the-points FFT and plot its magnitude part. [*`2 pts`* for FFT code + `1 pts` for the plot]
- [3] Apply the inverse FFT. Compare it to the original audio by listening to both. [*`1 pts`* for inverse FFT code + *`1 pts`* for the generation of original audio back correctly]


### Problem 2 [Convolution and LTI system] – *`5pts`*

Write a program that calculates `y[n] = x[n]*h[n]` (this is not simple multiplication; it is the convolution between x and h), where `y[n]` is *`598`* samples, `x[n]` is *`500`* samples, and `h[n]` is *`99`* samples.

- [1] Generate an impulse response, `h[n]`, according to the algorithm below. This filter kernel is called a **`low-pass windowed-sinc`** filter. When convolved with an input signal, this filter passes sinusoids that have fewer than *`25`* cycles in *`500`* samples, and blocks sinusoids with a higher frequency. Make a plot of this signal. [*`1 pts`* for the plot of `h(n)`]

```python
for i = 0 to 98
     h[i] = 0.31752 * sin(0.314159 * (i-49.00001)) / (i-49.00001)
     h[i] = h[i] * (0.54 - 0.46 * cos(0.0641114 * i))
```
- [2] Test your program by convolving `h[n]` with the signal described below. [*`1 pts`* for the convolution code]

- [3] What should the output of your program be in response to this signal? Why? [*`1 pts`* for the convolution output and explanation] `x[n]` = *`1`* for `n` = *`0`* , `x[n]` = *`0`* otherwise

- [4] Generate a more complicated test signal, `x[n]`, that consists of two sinusoids added together. The first sinusoid will have an amplitude of *`1`*, and make *`6`* complete cycles in the *`500`* samples. The second sinusoid will have an amplitude of *`0.5`* and make *`44`* complete cycles in the *`500`* samples. Make of plot of this signal. [*`1 pts`* for the convolution output]

- [5] Test your convolution program by filtering the signal you created in *`4`*, with the filter kernel you created in *`2`*. Plot this signal. Has the filter passed the lower frequency signal, while blocking the higher frequency signal? Comment on the results of the convolution. [*`1 pts`* for the comment]


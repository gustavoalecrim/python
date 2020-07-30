from progressbar import *
def example1():
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=20000000).start()
    for i in range(2000000):
        pbar.update(10*i+1)
    pbar.finish()
example1()
raw_input()

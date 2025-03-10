from IV_plot import *
from Tm_plot import *

def total_plot(x):
    plt.figure(figsize=(20, 10))
    plt.suptitle(x[24:], fontsize=20, weight='bold')
    plt.subplots_adjust(hspace=0.3)

    tm_plot(x)
    iv_plot(x)

    plt.show()

def save_plot(x):
    plt.figure(figsize=(20, 10))
    plt.suptitle(x[24:], fontsize=20, weight='bold')
    plt.subplots_adjust(hspace=0.3)

    tm_plot(x)
    iv_plot(x)

    plt.savefig('./res/png_files/'+x[24:57]+'.png')
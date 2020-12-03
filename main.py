from coefficient import newploy
from evaluation import neweva,neweva2
import math
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def main():
    f = lambda x: 1/(1+25*x**2)
    in_x = np.array(range(21))
    in_x2 = -1 + 0.1*in_x
    coe = newploy(0, in_x2, f)
    y = f(0.985)
    y_pred = neweva(coe,in_x2,0.985)
    f3 = lambda x: np.cos((2*x+1)/(2*(20+1))*math.pi)
    in_x3 = f3(in_x)
    coe2 = newploy(0, in_x3, f)
    y_pred2 = neweva(coe2,in_x3,0.985)
    print('actual value: '+str(y))
    print('prediction 1:' + str(y_pred))
    print('prediction 2: '+ str(y_pred2))
    print('error1: ' + str(np.abs(y-y_pred)))
    print('error rate 1: ' + str(np.abs(y-y_pred/y*100))+ '%')
    print('error2: ' + str(np.abs(y-y_pred2)))
    print('error rate 2: ' + str(np.abs(y-y_pred2/y*100))+ '%')

    x_intmp = -1+0.01*np.array(range(200))
    x_intmp2 = -0.8+0.01*np.array(range(160))

    f_lamb1 = lambda x: eval(neweva2(coe,in_x2))
    f_lamb2 = lambda x: eval(neweva2(coe2,in_x3))
    fig, (ax1, ax2,ax3) = plt.subplots(3)
    plt.subplots_adjust(hspace=2)
    fig.suptitle('function graph')
    ax1.plot(x_intmp,list(map(f_lamb1, x_intmp)),'g')
    ax1.plot(x_intmp,list(map(f, x_intmp)),'r')
    ax1.title.set_text('Uniformly spaced nodes')

   
    ax2.plot(x_intmp2,list(map(f_lamb1, x_intmp2)),'g')
    ax2.plot(x_intmp2,list(map(f, x_intmp2)),'r')
    ax2.title.set_text('Uniformly spaced nodes (cut the tail and head)')
    
    ax3.plot(x_intmp,list(map(f_lamb2, x_intmp)),'g')
    ax3.plot(x_intmp,list(map(f, x_intmp)),'r')
    ax3.title.set_text('Cosine spaced nodes')
    plt.show()
main()
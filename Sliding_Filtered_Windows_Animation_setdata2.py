'''
Created on Jan 26, 2014

@author: c3h3
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

L = 10
n = 2048
t2 = np.linspace(0,L,n+1)
t = t2[:-1]
k = (2*np.pi/L)*np.fft.fftfreq(n,1.0/n)
ks = np.fft.ifftshift(k)

S = (3*np.sin(2*t) + 0.5*np.tanh(0,5*(t-3)) + 0.28*np.exp(-(t-4)**2) \
     + 1.5*np.sin(5*t) + 4*np.cos(3*(t-6)**2))/10 + (t/20)**3

fig, (sig_and_win, sig_conv_win, win_freq) = plt.subplots(ncols=1,nrows=3)

sig_and_win.set_ylim([-1.25, 1.25])
sig_and_win.set_xlim([min(t), max(t)])
sig_conv_win.set_ylim([-1.25, 1.25])
sig_conv_win.set_xlim([min(t), max(t)])
win_freq.set_xlim([-50, 50])
win_freq.set_ylim([0, 1.25])


sig_line, win_line = sig_and_win.plot([],[],"k",[],[],"m")
sig_conv_win_line, = sig_conv_win.plot([],[],"k")
win_freq_line, = win_freq.plot([],[],"k")


print "sig_and_win = ",sig_and_win
print "sig_line, win_line = ",sig_line, win_line
print "sig_line..get_xydata(), win_line.get_xydata() = ",sig_line.get_xydata(), win_line.get_xydata()
print "sig_conv_win_line = ",sig_conv_win_line
print "win_freq_line = ",win_freq_line



#fig, (sig, win, sig_conv_win, win_freq) = plt.subplots(ncols=1,nrows=4)
#
#sig.set_ylim([-1.25, 1.25])
#win.set_ylim([-1.25, 1.25])
#sig_conv_win.set_ylim([-1.25, 1.25])
#win_freq.set_xlim([-50, 50])
#win_freq.set_ylim([0, 1.25])
#
#
# 
#sig.plot([],[],"k")
#win.plot([],[],"m")
#sig_conv_win.plot([],[],"k")
#win_freq.plot([],[],"k")
#
#
width = 1
slides = np.arange(0,10,0.1)

def init():
    sig_line.set_data([],[])
    win_line.set_data([],[])
    sig_conv_win_line.set_data([],[])
    win_freq_line.set_data([],[])
    
   
def update(n): 
    f = np.exp(-width*(t-slides[n])**2)
    Sf = np.prod(np.c_[f,S],axis=1)
    Sft = np.fft.fft(Sf)
    
    sig_line.set_data([t],[S])
    win_line.set_data([t],[f])
    sig_conv_win_line.set_data([t],[Sf])
    win_freq_line.set_data([ks],[np.abs(np.fft.fftshift(Sft))/max(np.abs(np.fft.fftshift(Sft)))])
    
    


anim = animation.FuncAnimation(fig, update, init_func=init, frames=len(slides), blit=True)
#
## # anim.save can be called in a  few different ways, some which might or might not work
## # on different platforms and with different versions of matplotlib.
## #anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'], writer=animation.FFMpegWriter())
## #anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
#
##anim.save('animation.mp4', fps=20, writer="ffmpeg", codec="libx264")

anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'], writer=animation.FFMpegWriter())
plt.close(fig)



#
##width = 1
##slides = np.arange(0,10,0.1)
###for i in range(len(slides)):
###    f = np.exp(-width*(t-slides[i])**2)
###    Sf = np.prod(np.c_[f,S],axis=1)
###    Sft = np.fft.fft(Sf)
###    
###    
###    sig_and_win.set_data(t,S,"k",t,f,"m")
###    sig_conv_win.set_data(t,Sf,"k")
###    win_freq.set_data(ks,np.abs(np.fft.fftshift(Sft))/max(np.abs(np.fft.fftshift(Sft))),"k")
##
##
##
##def init():
##    sig_and_win.plot([],[],"k",[],[],"m")
##    sig_conv_win.plot([],[],"k")
##    win_freq.plot([],[],"k")
##    
##def update(n): 
##    f = np.exp(-width*(t-slides[n])**2)
##    Sf = np.prod(np.c_[f,S],axis=1)
##    Sft = np.fft.fft(Sf)
##    
##    sig_and_win.set_data(t,S,"k",t,f,"m")
##    sig_conv_win.set_data(t,Sf,"k")
##    win_freq.set_data(ks,np.abs(np.fft.fftshift(Sft))/max(np.abs(np.fft.fftshift(Sft))),"k")
##
##
##anim = animation.FuncAnimation(fig, update, init_func=init, frames=len(slides), blit=True)
##
### # anim.save can be called in a  few different ways, some which might or might not work
### # on different platforms and with different versions of matplotlib.
### #anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'], writer=animation.FFMpegWriter())
### #anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
##anim.save('animation.mp4', fps=20, writer="ffmpeg", codec="libx264")
##
##plt.close(fig)
#
##     # update the line data
##     pendulum1.set_data([0 ,x1], [0 ,y1])
##     pendulum2.set_data([x1,x2], [y1,y2])
#
#    
##    plt.subplot(3,1,1)
##    plt.plot(t,S,"k",t,f,"m")
##    plt.ylim(-1.25, 1.25)
##    
##    plt.subplot(3,1,2)
##    plt.plot(t,Sf,"k")
##    plt.ylim(-1.25, 1.25)
##    
##    plt.subplot(3,1,3)
##    plt.plot(ks,np.abs(np.fft.fftshift(Sft))/max(np.abs(np.fft.fftshift(Sft))),"k")
##    plt.xlim(-50, 50)
##    
##    plt.draw()
##    plt.pause(0.01)
##    plt.clf()


if __name__ == '__main__':
    pass
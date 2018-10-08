import matplotlib.pyplot as plt
from matplotlib import gridspec
import random
plt.rcParams['font.sans-serif']=['SimHei']

fig = plt.figure(figsize=(8,6),facecolor='white')
gs = gridspec.GridSpec(2,1,height_ratios=[4,2])

ax1 = plt.subplot(gs[0])
ax1.set_title('图表1',loc='center',color='r')
x = [i for i in range(0,50)]
y = [random.randint(1,100) for i in range(0,50)]
ax1.plot(x,y,label='线1',color='b',linestyle='--',lw=1,alpha=0.5)

y2 = [random.randint(1,100) for i in range(0,50)]
ax1.plot(x,y2,label='线2',color='r',ls='-',lw=1,alpha=1)

#ax1.grid(color='r',ls='--',lw=1,alpha=0.5)
ax1.xaxis.grid(color='r',ls='--',lw=1,alpha=0.5)
ax1.legend(loc='upper',)

ax2 = plt.subplot(gs[1])

plt.subplots_adjust(hspace=0.5)

plt.show()
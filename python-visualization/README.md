# Matplotlib
> save image from remote client application
~~~python
import matplotlib.pyplot as plt
# plt.switch_backend('agg')
~~~
## 1. Bar chart
[Frequncy_Distplot.png](./images/barchart/Frequency_Distplot.png)
~~~python
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
h = [1,2,3,4,5,6]
plt.bar(
    x=np.arange(6), 
    height=h,
    tick_label=['0-20','21-40','41-60','61-80','81-100','101-'], 
    width=0.2,
    align='center',
    label='first bar chart')
plt.legend()
plt.xlabel('# of Training Instance')
plt.ylabel('# of User/Product')
# plt.show()
plt.gcf().savefig('Frequency_Distplot.png')
~~~

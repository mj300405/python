import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

arr1=np.random.normal(size=100, loc=0, scale=1)
arr2=np.random.binomial(size=100, n=10, p=0.3)
arr3=np.random.poisson(size=100, lam=0.3)
arr4=np.random.uniform(size=100, low=0.3, high=0.9)
arr5=np.random.logistic(size=100, loc=0, scale=1)
arr6=np.random.multinomial(size=100, n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6]) #dice throw
arr7=np.random.exponential(size=100, scale=1)
arr8=np.random.chisquare(size=100, df=1)
arr9=np.random.rayleigh(size=100, scale=1)
arr10=np.random.pareto(a=1, size=100)
arr11=np.random.zipf(a=2, size=100)


sns.displot(data=arr1, label='Normal', kind='kde')
plt.show()

sns.displot(data=arr2, label='Binomial (Bernouli)', kind='hist')
plt.show()

sns.displot(data=arr3, label='Poisson', kde=True)
plt.show()

sns.displot(data=arr4, label='uniform', kind='kde' )
plt.show()

sns.displot(data=arr5, label='logistic', kind='kde')
plt.show()

sns.displot(data=arr6, label='multinomial', kind='hist', kde=True)
plt.show()

sns.displot(data=arr7, label='exponential', kind='kde')
plt.show()

sns.displot(data=arr8, label='chisquare', kind='kde')
plt.show()

sns.displot(data=arr9, label='rayleight', kind='kde')
plt.show()

sns.displot(data=arr10, label='pareto', kind='hist', kde=True)
plt.show()

sns.displot(data=arr11[arr11<50], label='zipf', kind='hist', kde=True)
plt.show()
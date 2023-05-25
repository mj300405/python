import matplotlib.pyplot as plt
import numpy as np


xpoints=np.array([0,6])
ypoints=np.array([0,250])
plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, 'o')
plt.show()

###############################################################################

xpoints1=np.array([1,2,4,8])
ypoints1=np.array([1,9,3,27])
plt.plot(xpoints1,ypoints1, marker='o')
plt.show()

###############################################################################

ypoints2=np.array([1,6,2,7,5,3])
plt.plot(ypoints2)
plt.show()

###############################################################################

plt.plot(xpoints1,ypoints1, 'c*:', ms=15, mec='hotpink', mfc='#4CAF50')
plt.show()

################################################################################

plt.plot(xpoints1,ypoints1, linestyle='dotted', color='cyan', linewidth=10)
plt.show()

###############################################################################

x1=np.array([1,2,3,4,5])
x2=np.array([1,2,3,4,5])
y1=np.array([5,1,8,2,3])
y2=np.array([4,1,7,5,2])
plt.plot(y1)
plt.plot(y2)
plt.show()

###############################################################################

plt.plot(x1,y1,x2,y2)
plt.show()

###############################################################################
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title('Sports Watch Data')
plt.xlabel('Average Pulse')
plt.ylabel('Calories Burnage')
plt.show()

###############################################################################

plt.plot(x, y, 'co-', ms=3)
font1={'family':'monospace', 'color':'#E34A6F', 'size':20}
font2={'family':'serif', 'color':'hotpink', 'size':15}
plt.title('Sports Watch Data', fontdict=font1, loc='left')
plt.xlabel('Average Pulse', fontdict=font2)
plt.ylabel('Calories Burnage', fontdict=font2)
plt.grid(axis='both')
plt.show()

###############################################################################

plt.plot(x, y, color='hotpink', linestyle='-', linewidth=2, marker='D', markersize='4')
plt.grid(color='cyan', linestyle='-.', linewidth=0.5)
plt.show()

##############################################################################
x=np.array([0,1,2,3])
y=np.array([3,7,5,1])
plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title('Sales')

x=np.array([0,1,2,3])
y=np.array([3,5,7,9])
plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.title('Income')

x=np.array([0,1,2,3])
y=np.array([9,8,7,6])
plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title('Outcome')

x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2, 3, 4)
plt.plot(x,y)
plt.title('Profit')

x=np.array([0,1,2,3])
y=np.array([3,7,1,1])
plt.subplot(2, 3, 5)
plt.plot(x,y)
plt.title('Quantity')

x=np.array([0,1,2,3])
y=np.array([6,5,4,5])
plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.title('Earning')

plt.suptitle('My Shop')
plt.show()
############################################################################

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x,y)

plt.show()

###########################################################################

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x,y, color=colors)
plt.show()

###########################################################################
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes=10*np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, cmap='winter', s=sizes, alpha=0.5)
plt.colorbar()
plt.show()

##########################################################################

x=np.array(['A', 'B', 'C', 'D'])
y=np.array([6,2,9,7])

plt.bar(x,y, width=0.05)
plt.show()

x=np.array(['A', 'B', 'C', 'D'])
y=np.array([6,2,9,7])

plt.barh(x,y, color='#4CAF50', height=0.2)
plt.show()

#########################################################################

x=np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()


#########################################################################

y=np.array([10,45,15,25,5])
mylabels=np.array(['appple', 'banana', 'cherry', 'Papaya', 'Watermelon'])
myexplode=np.array([0.2,0,0,0,0])
mycolors=np.array(['#BA7BA1', '#C28CAE', '#D0ABA0', '#DEC4A1', '#EDCF8E'])

plt.pie(y, labels=mylabels, startangle=90, explode=myexplode, colors=mycolors)
plt.legend(title='Fruits')
plt.show()
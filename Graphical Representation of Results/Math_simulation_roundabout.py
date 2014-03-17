import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

file = open("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Software\Roundabout\graphical out\simulation_roundabout.txt")
lines=file.readlines()
data = lines

def get_rate_of_car_creation():
    #file = open("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Software\simulation.txt")
    #lines=file.readlines()
    global data
    rate_car_creation = float(data[3])
    rate_car_creation10 = rate_car_creation * 10
    int_rate_car_creation10=int(rate_car_creation10)

    return int_rate_car_creation10  
    
def get_simulation_time():
    #file = open("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Software\simulation.txt")
    #lines=file.readlines()
    global data
    simulation_time=data[1]
    int_simulation_time=int(simulation_time)
    return int_simulation_time  
    
def get_coordinate(coordinate_number):
    # i = coordinate_number
    print ("I is equal to: ") , coordinate_number
    index_x = (4+(1800*(coordinate_number)))
    index_y = (5+(1800*(coordinate_number)))
    #xy=np.zeros((2,100), dtype=np.int)
    xy=np.zeros((900,2))
    current_number_of_cars=get_current_carnumber(coordinate_number)
    print ("Current number of Cars: ") , current_number_of_cars    
    #file = open("C:\Users\Alexander\Dropbox\St Georges\Mathematics\Exploration\Software\simulation.txt")
    #lines=file.readlines()
    global data
    for n in range(current_number_of_cars):
        xy[n,0]=data[index_x+(2*n)]
        xy[n,1]=data[index_y+(2*n)]
    return xy
    
def _update_plot(i,fig,scat):
    xy = get_coordinate(i)
    print ("Data: ")
    print xy[:30,:2]
    scat.set_offsets(([xy[:,:2]]))
    c = np.ones((900,1))
    scat._sizes = 157 * c[:,0]
    #scat.set_offsets(([xy[0,0],xy[1,0]],[xy[0,1],xy[1,1]],[xy[0,2],xy[1,2]]))  
    return scat,  
    
def get_current_carnumber(i):
    rate_car_creation10 = get_rate_of_car_creation()
    n=0
    while ((n*rate_car_creation10) <= (i)):
        n=n+1
    return n   
    
    
frame_number =  int(get_simulation_time())*10   
fig = plt.figure()
xy=np.zeros((900,2))
ax = fig.add_subplot(111)
ax.set_xlim([0, 630])
ax.set_ylim([-10, 287])
scat=plt.scatter(xy[:,0],xy[:,1])
anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig, scat),
                              frames = frame_number , interval =10, blit=True, repeat=False)                             
plt.show()                  
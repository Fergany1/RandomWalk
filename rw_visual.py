import matplotlib.pyplot as plt

from random_walk import RandomWalk

"""Keep making new walks , as long as the program is active"""
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig ,ax = plt.subplots()
    
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values , rw.y_values , c=point_numbers , cmap = plt.cm.Blues ,
        edgecolors='none', s =1 )

    # Set equal scaling
    ax.set_aspect('equal')

    # Emphasize the start and last points
    ax.scatter(0 , 0 , c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1] , rw.y_values[-1] , c='red', edgecolors='none', s=100)
    
    # Remove The axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # plt.savefig('RandomWalk/images/rw_1_plot.png' , bbox_inches='tight')

    plt.show()
    
    
    keep_running = input("Make Another Walk ? (Y/N)")
    if keep_running.lower() == 'N' or keep_running.lower() == 'n' or keep_running.lower() == 'No':
        break 

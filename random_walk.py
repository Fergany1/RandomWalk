from random import choice

class RandomWalk:
    """A Class to generate random walks"""
    def __init__(self , num_points = 5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points
        
        # All walks starts from 0
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """Calculate all the points of the walk"""
        
        # Keep taking steps until the walk reaches the desired num
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go and how far to go
            x_step = self.get_step()
            y_step = self.get_step()
            
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the next position
            new_x = self.x_values[-1] + x_step 
            new_y = self.y_values[-1] + y_step
            
            # Append the new position to the walk
            self.x_values.append(new_x)
            self.y_values.append(new_y)
            
    def get_step(self):
        """calculate a single step in the walk"""
        
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4 , 5, 6, 7, 8])
        step = direction * distance
        
        return step
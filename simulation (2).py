
import physics
import Vectors
physics.dict0 = [0,1]

# simulation object
G=1
physics.pointMass = ("planet" ,1, Vectors.vector(0,0,0))
physics.pointMass = ("sat" ,0.00002, Vectors.vector(2,0,0) , Vectors.vector(0,10,0))

#planet = physics.dict0[0] # the first body which i make it as a creation so it takes zero as an index
sat = physics.dict0[1]
# simulation output
file_name = "sat_results.csv"

file_handle = open(file_name , "w")

# Simulation of body moves with regular velocity

#objects = []
#print (objects)
#object0 = physics.pointMass ("object1" ,1, Vectors.vector(0,0,1) , Vectors.vector(0,0,1))
#print (objects)
#objects.append (object0)

quit()  # we do not need to make run for the next lines
# simulation iteration

time =0
time_step= 1/60
simulation_time = 10
while time <= simulation_time :
    time += time_step
    physics.EulersMethodStep (time_step)
    
    # gravity loop
    for object_i in physics.dict0:
        physics.Gravity_i (G , physics.dict0 , object_i)
    
    # numerical solution
    physics.EulersMethodStep (time_step)
    
    # output
    output =sat.position
    x ,y ,z = output.x , output.y , output.z
    output = str(x) + "," + str(y) + "," + str(z) + "\n"
    print(output)
   
    for object in physics.dict0 :
        print (object)
   

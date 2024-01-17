##local_and_global_variables_doesnt_effect_each_other
x=20
y=10
def mul (x,y):
    return (x*y)
mul (4,5)
##to_change_the_local_and_global_variables
z=[]
def adding_element(m):
    z.append(m)
z
adding_element(3)
z
adding_element(5)
adding_element(7)
z
import numpy as np

beta = 1 # EMPIRICAL CONSTANT, FIND FROM MECHANICHAL
width = 1 #from mechanical
height_MEMS = 1 #mechanical
height_GOLD = 2
dist_to_MEMS = 1

def convert(alpha, L_TOF):
  v1 = np.array([width/2,height_MEMS])

  r_p = (height_MEMS-height_GOLD-np.tan(2*alpha)*width)/(np.tan(beta)-np.tan(2*alpha))
  z_p = height_MEMS-np.tan(2*alpha)*width+np.tan(2*alpha)*r_p
  v2_abs = np.sqrt((width-r_p)**2+(height_MEMS-z_p)**2)
  v3_abs = L_TOF-(dist_to_MEMS+v2_abs)

  v2 = v2_abs*np.array([np.cos(2*alpha),np.sin(2*alpha)])
  v3 = v3_abs*np.array([np.cos(2*(beta-alpha)),np.sin(2*(beta-alpha))])
  v = v1+v2+v3
  return v[0],v[1]


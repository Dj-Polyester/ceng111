"I have prepared some testcases for you to use. You can add or edit the way you want. I'm open to the feedbacks and if you want to contribute, feel free to contract me."""
from random import*
def get_data():
#1)Two Li atoms' attraction. One of them is moving with a velocity hizx to the other one:
#	x=400.
#	y=500.
#	hizx=10.
#	return [100,.025,[1.,250.,135.,12.+hizx,0.],[1.,250.-(62.5*(3.**.5)),322.5,-6.+hizx,6.*(3**.5)],[1.,250.+(62.5*(3.**.5)),322.5,-6.+hizx,-6.*(3**.5)],[250.,250.,260.,0.+hizx,0.],[1.,250.+x,135.+y,12.,0.],[1.,250.-(62.5*(3.**.5))+x,322.5+y,-6.,6.*(3**.5)],[1.,250.+(62.5*(3.**.5))+x,322.5+y,-6.,-6.*(3**.5)],[250.,250.+x,260.+y,0.,0.]]
#2)A simple solar system. Sun,planet and a moon:
#	distance=float(randint(470,600))
#	return [3.,.025,[1500.,200.,distance,0.,0.],[150.,200.,100.,3.,0.],[10.,200.,50.,6.,0.]]
#3)A planet and a moon:
	m=100.
	r=100.
	v=10.
	return [100,.025,[1.,250.,135.,12.,0.],[250.,250.,260.,0.,0.]]

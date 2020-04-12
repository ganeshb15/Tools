  
# Importing Image from PIL package  
from PIL import Image 
      
# creating a image object 
def ColorThreshold(InputImage,RThreshold,GThreshold,BThreshold,sx,sy,b1,w):
	f = open("demofile2.txt", "w")
	
	image = Image.open(InputImage)  
  
	width, height = image.size 
 
	i=0
	k=0
	for x in range(height): 
		for y in range(width): 
			cordinate = x1, y1 = y,x
			r,g,b=image.getpixel(cordinate)
			k=k+1
			if not(r<RThreshold and g<GThreshold and b<BThreshold )and(x%sx==0 and y%sy==0):
				image.putpixel((y, x), (255, 255, 255, 255))								 
			else:
				image.putpixel((y, x), (0, 0, 0, 255))				
			if x%sx==0 and y%sy==0:
				if r<RThreshold and g<GThreshold and b<BThreshold:
					f.write(str(b1))
				else: 
					f.write(str(w))
		if x%sx==0:
			f.write("\n") 
				

  
	#image.show() 
	im1 = image.save("geeks.bmp")
	f.close()

#ColorThreshold('287256.bmp',100,100,150,5,5)

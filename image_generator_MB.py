from PIL import Image

input_mb = int(input("Enter generated MB: "))

#Because 1mpx of RGBA white image without compression is 4 MB file size
#Method GetImageSize check whether the input is the exponent of 4
# if it is the method returnes the tuple of 1000px*exponent X 1000px*exponent
#If no method returnes image which has 500px X (output*500)px file size which is usable when output can't be divided by 4 or at least 2
#THe algorithm should be improved by finding the way to create the more than 500 px side images for non exponents of 4 sizes
def GetImageSize(mb):
	tmp = 1
	count = 0
	while tmp < mb:
		print(tmp)
		print(count)
		tmp *= 4
		count += 1;
	if (tmp == mb):
		return (1000*count,1000*count)
	return (500,mb*500)

#0,25 mpx (or 500x500 px) is 1 MB!
im = Image.new("RGBA", GetImageSize(input_mb),color="white")
im.save("image"+str(input_mb)+"mb.png", dpi=(300,300), compress_level=0)

#Windows specific script
#Or maybe some python3.7 specific script
#The problem is that trying launching "ImageGenerator --mpx 32" on another system (WIN 10, Python 3.7) causes type Error in GetImageSizeForMpx method
#Method returnes tuple with one float number like (3000, 10666.66) and on another system (GNU\Linux, Python 2.7 maybe) it behaves as expected and
#returnes (3000,10666) 
from PIL import Image
import argparse

def main(inp):
	if (args.mb is not None):
		print("***Creating image with {} MB***".format(inp))
		im = Image.new("RGBA", GetImageSizeForMb(args.mb), color="white")
		im.save("image"+str(args.mb)+"mb.png", dpi=(300,300), compress_level=0)
	elif(args.mpx is not None):
		print("***Creating image with {}  MPX***".format(inp))
		im = Image.new("RGB", GetImageSizeForMpx(args.mpx),0)
		im.save("image"+str(args.mpx)+"mpx.jpg")

#Method to obtain desirable MPX image
#We search if the mpx can be obtain by multiply one number (like 1000x1000). If not we just setting width to 3000
def GetImageSizeForMpx(n):
    p = n
    for x in range(0,n):
        p = p-1
        if ((p*p) == n):
            return (p*1000,p*1000)
            break
        elif (p==1):
            return (3000, int(n*1000000/3000))

#Because 1mpx of RGBA white image without compression is 4 MB file size
#Method GetImageSize check whether the input is the exponent of 4
# if it is the method returnes the tuple of 1000px*exponent X 1000px*exponent
#If no method returnes image which has 500px X (output*500)px file size which is usable when output can't be divided by 4 or at least 2
#THe algorithm should be improved by finding the way to create the more than 500 px side images for non exponents of 4 sizes
def GetImageSizeForMb(mb):
	tmp = 1
	count = 0
	while tmp < mb:
		tmp *= 4
		count += 1;
	if (tmp == mb):
		return (1000*count,1000*count)
	return (500,mb*500)
 
if __name__=="__main__":
	parser = argparse.ArgumentParser(description="Generate MB driven or MPX driven image file")
	parser.add_argument("--mb", type=int)
	parser.add_argument("--mpx", type=int)
	args = parser.parse_args()
	if args.mb:
		main(args.mb)
	elif args.mpx:
		main(args.mpx)
else:
	print("Error: the right format is '-mb 1' or '-mpx 1'")	

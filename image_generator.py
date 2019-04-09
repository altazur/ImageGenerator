from PIL import Image

input_mpx = int(input("Enter generated mpx: "))

def ImageSize(n):
    p = n
    for x in range(0,n):
        p = p-1
        if ((p*p) == n):
            return (p*1000,p*1000)
            break
        elif (p==1):
            return (3000, n*1000000/3000)

im = Image.new("RGB", ImageSize(input_mpx), 0)
im.save("image"+str(input_mpx)+"mpx.jpg")


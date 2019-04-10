from PIL import Image

input_mb = int(input("Enter generated MB (only even numbers)\n*Not even numbers results in -1 MB: "))

def MbToMpx(n):
    if (n%2==0): return n/2
    return int(n/2)

def ImageSize(n):
    p = n
    for x in range(0,n):
        print('*')
        p = p-1
        if ((p*p) == n):
            return (p*1000,p*1000)
            break
        elif (p==1):
            return (3000, n*1000000/3000)

#2 MB = 1 MPX here
# or 1 MB = 0,5 MPX
#i hope
im = Image.new("I", ImageSize(MbToMpx(input_mb)), 0)
im.save("image"+str(input_mb)+"mb.png", dpi=(300,300), compress_level=0)

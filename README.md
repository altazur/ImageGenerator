***Image Generator***

There are two independent scripts:
1. image_generator.MB.py - creates an image file with specific MB
2. image_generator.py - creates an image file with specific MPX value

Also there is an independent python based app "ImageGenerator.py" which takes console string arguments to create MPX or MB image files.
*There is a executable "ImageGenerator" compiled using pyinstaller for GNU\Linux with puthon 2.7
How to use "ImageGenerator":
ImageGenerator --mb 4 // creates a 4mb image inside current folder
ImageGenerator --mpx 4 // creates a 4mpx image inside current folder
Created images has info about like "4mpx" and so on

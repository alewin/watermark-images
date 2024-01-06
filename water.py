import sys, os
from PIL import Image, ImageDraw,ImageFont


def load_args():
    img_logo = sys.argv[3]
    position = sys.argv[4]
    if "." in sys.argv[1] :
        img_input = sys.argv[1]
        img_output = sys.argv[2]
        watermark_logo_image(img_input,img_output,img_logo,position)
    else :
        folder_input = sys.argv[1]
        folder_output = sys.argv[2]
        watermark_logo_images(folder_input,folder_output,img_logo,position)
        

def usage():
    print(" ----------------------------Logo---------------------------------")
    print("| Usage: wi.py input.jpg output.jpg logo.png position            |")
    print("| Usage: wi.py /folder_input /folder_output logo.png position    |")
    print(" ----------------------------Text--------------------------------")
    print("| Usage: wi.py input.jpg output.jpg 'text text' position         |")
    print("| Usage: wi.py /folder_input /folder_output 'some text' position |")
    print(" ----------------------------------------------------------------")
    print("| position = topleft/topright/center/bottomleft/bottomright      |")
    print(" -----------------------------------------------------------------")

def get_position(logo,image,pos):
    if pos == "topleft": return (0,0)
    if pos == "bottomleft": return (0, image.size[1] - logo.size[1])
    if pos == "topright": return (image.size[0] - logo.size[0] ,0)
    if pos == "bottomright": return (image.size[0] - logo.size[0] , image.size[1] - logo.size[1])
    if pos == "center": return ( (image.size[0] - logo.size[0])/2 ,( image.size[1] - logo.size[1])/2 )


#watermark_logo_image(input,output,logo,position)
def watermark_logo_image(i,o,l,p):
    logo  = Image.open(l)
    image = Image.open(i)
    image.paste(logo, get_position(logo,image,p),logo)
    image.save(o)

def watermark_logo_images(i,o,l,p):
    count = 0
    files = os.listdir(i)
    extenstions = ['png', 'bmp', 'jpg', 'gif', 'jpeg']
    for file in files:
         if any(file.endswith(ext) for ext in extenstions):
             watermark_logo_image(i + '/' + file, o + '/' + file, l, p)
             print("Processing %s %d of %d" %(file, count,len(files)))
             count+=1


if(len(sys.argv) < 4): 
    usage()
else: 
    try:
        load_args()
        print("Watermark successfully added")
    except Exception: 
        print('Error, please read "Usage"')
        usage()
        print('Error, please read "Usage"')

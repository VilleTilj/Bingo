from PIL import Image
filen = r'ball.png'
img = Image.open(filen)
img.save('icon.ico',format = 'ICO', sizes=[(32,32)])
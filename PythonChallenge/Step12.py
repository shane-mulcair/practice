from PIL import Image
imold = Image.open("C:\\Users\\mulcas4\\PycharmProjects\\PythonChallenge\\resources\\house.jpg")
w,h=imold.size
pix1=imold.load()
odd=even=Image.new(imold.mode,(w,h))
for i in range(imold.size[0]):
    for j in range(imold.size[1]):
        if(i%2==0 and j%2==0):
            even.putpixel((i/2,j/2),imold.getpixel((i,j)))
        elif i % 2 == 0 and j % 2 == 1:
            odd.putpixel((i / 2, (j - 1) / 2), imold.getpixel((i, j)))
        elif i % 2 == 1 and j % 2 == 0:
            even.putpixel(((i - 1) / 2, j / 2), imold.getpixel((i, j)))
        else:
            odd.putpixel(((i - 1) / 2, (j - 1) / 2), imold.getpixel((i, j)))

even.save("C:\\Users\\mulcas4\\PycharmProjects\\PythonChallenge\\resources\\even.jpg")
odd.save("C:\\Users\\mulcas4\\PycharmProjects\\PythonChallenge\\resources\\odd.jpg")

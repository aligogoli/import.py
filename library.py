
username= input("login:>>")

password= int(input('password:'))
if password == 1234 and username=="admin":
    print('welcome')
    

 # from pytube import YouTube
 # yt = YouTube('https://youtu.be/84-FuyviX1s')

    import aspose.words as aw
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)

    builder.insert_image(input("Input.png:"))

    doc.save("C:/Users/ali/Desktop/Output.pdf")
    from PIL import Image

    img = Image.open(input('test.jpg:'))
    imgGray = img.convert('L')
    imgGray.save('C:/Users/ali/Desktop/test_gray.jpg')
   
    

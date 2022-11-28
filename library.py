

username= input("login:>>")

password= int(input('password:'))
if password != 1234 or username!="admin":
    print('wrong')
elif password == 1234 or username =="admin":
    print('run')


    a =('1.You Tube downloader')
    b = ('2.image to pdf')
    c =('3.convert image to black and white') 
    i = ([a],[b],[c])
    print(i)
    for this_one in i :
        
        
        choice =  int(input('please enter your program number for run:'))
        if choice ==1:
          from pytube import YouTube
     
          yt = YouTube('https://youtu.be/9FL3xBDW-po')
          print(yt)
        elif choice ==2:
         import aspose.words as aw
 
         doc = aw.Document()
         builder = aw.DocumentBuilder(doc)

         builder.insert_image=(input("Input.png:"))

         doc.save("C:/Users/ali/Desktop/Output.pdf")
    
           
        
      
        elif  choice ==3:
         from PIL import Image


         img= Image.open(input('test.jpg:'))
         imgGray = img.convert('L')
         imgGray.save('C:/Users/ali/Desktop/test_gray.jpg')

         
      
        
      

      
        
    

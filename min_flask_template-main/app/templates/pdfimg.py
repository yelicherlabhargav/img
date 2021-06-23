from pdf2image import convert_from_path
pages = convert_from_path('./TCP.pdf', poppler_path=r"C:\Users\sunny\Downloads\Release-21.03.0 (1)\poppler-21.03.0\Library\bin")
count = 0
for page in pages:
     count +=1
     page.save('TCP'+'.jpg', 'JPEG')
     break
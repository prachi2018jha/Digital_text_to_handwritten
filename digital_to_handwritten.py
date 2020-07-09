from PIL import Image
#Width of the sheet : 5800
#height of the sheet: 6555
sheet=Image.open("sheet.png")
x,y=0,0
f=0
print(sheet.width,sheet.height)
def write_on_page(character):
    global x,y,sheet,pg
    if character=='\n':
        pass
    else:
        photo=Image.open("handwritten/%s" % character)
        sheet.paste(photo,(x,y))
        size=photo.width
        x+=size
        del photo
def sentence_to_letter(sentence):
    global x ,y,sheet,pg
    sentence=sentence.split(' ')
    for word in sentence:
        if (x+ len(word) >4300 and y> 5600):  #according to the size of the sheet 
            sheet.save('%sout.png'%pg)
            sheet1=Image.open('sheet.png')
            sheet=sheet1
            x,y=0,0
            pg+=1

        if x + len(word) > 4300: #less than the width of the sheet
            x=0
            y+=370

        for character in word:
            if character=='#':
                x=0
                y+=390      
            elif character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*()-+={[']}:;<>?/" :
                if character.isupper():
                    character+='up.png'
                elif character.islower():
                    character+='.png'
                elif character=='*':
                    character='asterisk.png'
                elif character==',':
                    character='comma.png'
                elif character==':':
                    character='colon.png'
                elif character=='<':
                    character='ango.png'
                elif character=='>':
                    character='angc.png'
                elif character==".":
                    character='fulls.png'
                elif character=='?':
                    character='qmark.png'
                elif character=='/':
                    character='sslash.png'
                else:
                    character+='.png'
                write_on_page(character)
        write_on_page('space.png')

pg=0
with open('test.txt','r') as file:
    data=file.read().replace('\n','')

sentence_to_letter(data)
#to save the last sheet
sheet.save('%sout.png'%pg)
sheet1=Image.open('sheet.png')
sheet=sheet1
pg+=1
sheet_list=[]
for i in range(0,pg):
    sheet_list.append('%sout.png' %i)
#ANOTHER APPROACH TO CREATE THE PDF (USING FPDF) HAS BEEN COMMENTED
# cover = Image.open(sheet_list[0])
# width, height =cover.size
#  #5000,6500
# pdf = FPDF(unit="pt", format=[width, height])
# for i in range(0, pg):
#     pdf.add_page()
#     print("55")
#     pdf.image(sheet_list[i],0,0)
#     print("Adding")
# pdf.output("output.pdf", "F")
def pdf_creation(PNG_FILE, flag=False):
    rgba = Image.open(PNG_FILE)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split()[3])  # paste using alpha channel as mask
    rgb.save('output.pdf',append=flag) 

#First create a pdf file if not created
pdf_creation(sheet_list.pop(0))

#Converting the sheets into pdf 
for PNG_FILE in sheet_list:
    pdf_creation(PNG_FILE, flag=True)



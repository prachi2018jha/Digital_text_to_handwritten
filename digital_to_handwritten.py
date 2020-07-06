from PIL import Image
from fpdf import FPDF
sheet=Image.open("sheet.png")
x,y=0,0
f=0
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
        if (x+ len(word) >5150 and y> 6000):  #5100
            sheet.save('%sout.png'%pg)
            sheet1=Image.open('sheet.png')
            sheet=sheet1
            x,y=0,0
            pg+=1

        if x + len(word) > 4300:#4960 is the size of sheet
            x=0
            y+=370

        for character in word:
            if character=='#':
                x=0
                y+=370
                    
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

# with open('output.pdf','w') as file:
#     pass
# length=len(data)
# n=length//440
# if n==0:
#     one_page=[data]
#     print(length ,n)
# else:
#     one_page=[data[i:i+500] for i in range(0,length,500)]
#     print(length,n)
# for i in range(0,len(one_page)):
#     sentence_to_letter(one_page[i])
#     write_on_page('\n')
    # sheet.save('%sout.png'%pg)
    # sheet1=Image.open('sheet.png')
    # sheet=sheet1
    # x,y=0,0
    # pg+=1
# sheet_list=[]
# for i in range(0,len(one_page)):
#     sheet_list.append('%sout.png' %i)
# cover = Image.open(sheet_list[0])
# width, height = 5000,6500
# pdf = FPDF(unit="pt", format=[width, height])
# for i in range(0, len(sheet_list)):
#     pdf.add_page()
#     pdf.image(sheet_list[i], 0, 0)
# pdf.output("output.pdf", "F")



import qrcode

img = qrcode.make('https://brownsurfing.com/')

type(img)

img.save('qrcode.png')
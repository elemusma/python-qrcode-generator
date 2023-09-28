import qrcode

img = qrcode.make('https://latinowebstudio.com/')

type(img)

img.save('latinowebstudio.png')
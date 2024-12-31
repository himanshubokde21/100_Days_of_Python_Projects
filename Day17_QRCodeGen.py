import qrcode 

def generate_qrcode(data, filename):
  qr = qrcode.QRCode(version=1, box_size=10, border=5)
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill_color='gray', back_color='white')
  img.save(filename)
  img.show()
  
if __name__ == '__main__':
  data = input('Enter URL: ')
  filename = 'qrcode_image.png'
  generate_qrcode(data, filename)

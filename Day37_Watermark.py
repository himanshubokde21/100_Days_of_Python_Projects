from PIL import Image, ImageDraw, ImageFont

def add_watermark(in_img_path, out_img_path, watermark_text):

    in_img = Image.open(in_img_path)
    in_img = in_img.convert('RGBA')
    width, height = in_img.size

    overlay = Image.new('RGBA', in_img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    watermark_color_pattern = (255, 255, 255, 30)

    for i in range(0, width + height, 50):
        draw.line([(0, height - i), (i, height)], fill=watermark_color_pattern, width=5)

    font_size = 150
    font = ImageFont.truetype('arial.ttf', font_size)

    bbox = font.getbbox(watermark_text) 
    text_width = bbox[2] - bbox[0]  
    text_height = bbox[3] - bbox[1]  

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    watermark_color_text = (255, 255, 255, 80)

    draw.text((x, y), watermark_text, fill=watermark_color_text, font=font)  # Corrected: Fixed syntax here

    watermark_img = Image.alpha_composite(in_img, overlay)

    watermark_img.save(out_img_path) 

if __name__ == '__main__':
    in_img_path = 'data/img.png' 
    out_img_path = 'output_image.png'
    watermark_text = 'Watermark'

    add_watermark(in_img_path, out_img_path, watermark_text)

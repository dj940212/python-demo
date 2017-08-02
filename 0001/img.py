from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('test.jpg').convert('RGBA')

txt = Image.new('RGBA', base.size, (255,255,255,0))

d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((10,10), "Hello", font=None, fill=(255,255,255,255))
# draw text, full opacity
d.text((10,60), "World", font=None, fill=(255,255,255,255))

out = Image.alpha_composite(base, txt)

out.show()

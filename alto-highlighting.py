import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import os
import re
import glob

# Input files should be JPEG, RGB color mode
# JPEG & XML files should be placed in the same directory
# JPEG & XML filename should be same
# Coordinated handled "mm10"

# Creating Output directories
filepath = input(" Enter the JPEG File path: ")
output_directory = "Highlighted"
word_directory = "Word"
line_directory = "Line"
block_directory = "Block"
image_directory = "Image"
margin_directory = "Margin"
printspace_directory = "Printspace"

out = filepath + "/" + output_directory + "/"
word = filepath + "/" + output_directory + "/" + "/" + word_directory + "/"
line = filepath + "/" + output_directory + "/" + "/" + line_directory + "/"
block = filepath + "/" + output_directory + "/" + "/" + block_directory + "/"
imagedir = filepath + "/" + output_directory + "/" + "/" + image_directory + "/"
margin = filepath + "/" + output_directory + "/" + "/" + margin_directory + "/"
printspace = filepath + "/" + output_directory + "/" + "/" + printspace_directory + "/"

print(" \n Highlighting Files: ")
print(" \n ************************************* ")

if os.path.exists(out):
    pass
else:
    os.mkdir(out)

if os.path.exists(word):
    pass
else:
    os.mkdir(word)

if os.path.exists(line):
    pass
else:
    os.mkdir(line)

if os.path.exists(block):
    pass
else:
    os.mkdir(block)

if os.path.exists(imagedir):
    pass
else:
    os.mkdir(imagedir)

if os.path.exists(margin):
    pass
else:
    os.mkdir(margin)

if os.path.exists(printspace):
    pass
else:
    os.mkdir(printspace)

for fname in glob.glob(filepath + "/" + "*.jpg"):
	name = os.path.basename(fname)
	splitname = os.path.splitext(name)[0]
	Image.MAX_IMAGE_PIXELS = 933120000
	image = Image.open(filepath + "/" + splitname + ".jpg")
	if image.mode == "L":
		image = image.convert("RGB")
		img_dpi = str(image.info['dpi'])
		patn = re.sub(r"[\(\)]", "", img_dpi)
		sp = patn.split(",")[0]
		dpi_val = round(float(sp))
		output = fname
		image.save(output, dpi=(dpi_val,dpi_val), quality=90)
		image.close()


# Highlighting String Coordinates
for fname in glob.glob(filepath + "/" + "*.xml"):
	name = os.path.basename(fname)
	splitname = os.path.splitext(name)[0]
	filename = str("\"")+ fname + str("\"")
	print(" Word:" + filename)
	tree = ET.parse(filepath + "/" + name)
	root = tree.getroot()
	Image.MAX_IMAGE_PIXELS = 933120000
	image = Image.open(filepath + "/" + splitname + ".jpg")
	img_dpi = str(image.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))
	draw = ImageDraw.Draw(image, "RGBA")
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}String"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	output = word + "String" + "_" + splitname + "_" + "light" + ".jpg"
	image.save(output, dpi=(dpi_val,dpi_val), quality=90)
	image.close()


# Highlighting Line Coordinates
for fname in glob.glob(filepath + "/" + "*.xml"):
	name = os.path.basename(fname)
	splitname = os.path.splitext(name)[0]
	filename = str("\"")+ fname + str("\"")
	print(" Line:" + filename)
	tree = ET.parse(filepath + "/" + name)
	root = tree.getroot()
	Image.MAX_IMAGE_PIXELS = 933120000
	image = Image.open(filepath + "/" + splitname + ".jpg")
	img_dpi = str(image.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))
	draw = ImageDraw.Draw(image, "RGBA")
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}TextLine"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	output = line + "TextLine" + "_" + splitname + "_" + "light" + ".jpg"
	image.save(output, dpi=(dpi_val,dpi_val), quality=90)
	image.close()



# Highlighting Block Coordinates
for fname in glob.glob(filepath + "/" + "*.xml"):
	name = os.path.basename(fname)
	splitname = os.path.splitext(name)[0]
	filename = str("\"")+ fname + str("\"")
	print(" Block:" + filename)
	tree = ET.parse(filepath + "/" + name)
	root = tree.getroot()
	Image.MAX_IMAGE_PIXELS = 933120000
	image = Image.open(filepath + "/" + splitname + ".jpg")
	img_dpi = str(image.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))
	draw = ImageDraw.Draw(image, "RGBA")
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}TextBlock"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	output = block + "TextBlock" + "_" + splitname + "_" + "light" + ".jpg"
	image.save(output, dpi=(dpi_val,dpi_val), quality=90)
	image.close()


# Highlighting Image (ComposedBlock) Coordinates
for fname in glob.glob(filepath + "/" + "*.xml"):
	name = os.path.basename(fname)
	splitname = os.path.splitext(name)[0]
	filename = str("\"")+ fname + str("\"")
	print(" Image:" + filename)
	tree = ET.parse(filepath + "/" + name)
	root = tree.getroot()
	Image.MAX_IMAGE_PIXELS = 933120000
	image = Image.open(filepath + "/" + splitname + ".jpg")
	img_dpi = str(image.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))
	draw = ImageDraw.Draw(image, "RGBA")
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}ComposedBlock"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	output = imagedir + "Image" + "_" + splitname + "_" + "light" + ".jpg"
	image.save(output, dpi=(dpi_val,dpi_val), quality=90)
	image.close()


# Highlighting Margin Coordinates
for fname in glob.glob(filepath + "/" + "*.xml"):
	name = os.path.basename(fname)
	splitname = os.path.splitext(name)[0]
	filename = str("\"")+ fname + str("\"")
	print(" Margin:" + filename)
	tree = ET.parse(filepath + "/" + name)
	root = tree.getroot()
	Image.MAX_IMAGE_PIXELS = 933120000
	image = Image.open(filepath + "/" + splitname + ".jpg")
	img_dpi = str(image.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))
	draw = ImageDraw.Draw(image, "RGBA")
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}TopMargin"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}LeftMargin"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}RightMargin"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}BottomMargin"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	output = margin + "margin" + "_" + splitname + "_" + "light" + ".jpg"
	image.save(output, dpi=(dpi_val,dpi_val), quality=90)
	image.close()


# Highlighting PrintSpace Coordinates
for fname in glob.glob(filepath + "/" + "*.xml"):
	name = os.path.basename(fname)
	splitname = os.path.splitext(name)[0]
	filename = str("\"")+ fname + str("\"")
	print(" PrintSpace:" + filename)
	tree = ET.parse(filepath + "/" + name)
	root = tree.getroot()
	Image.MAX_IMAGE_PIXELS = 933120000
	image = Image.open(filepath + "/" + splitname + ".jpg")
	img_dpi = str(image.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))
	draw = ImageDraw.Draw(image, "RGBA")
	for coord in root.iter(f"{{http://www.loc.gov/standards/alto/ns-v3#}}PrintSpace"):
		x = int(coord.get('HPOS'))
		a = ((x/10)*dpi_val/25.4)
		y = int(coord.get('VPOS'))
		b = ((y/10)*dpi_val/25.4)
		width = int(coord.get('WIDTH'))
		width1 = ((width/10)*dpi_val/25.4)
		height = int(coord.get('HEIGHT'))
		height1 = ((height/10)*dpi_val/25.4)
		fill_color = (200, 100, 0, 127)
		outline_width = 0
		draw.rectangle([a, b, a + width1, b + height1], fill=fill_color, width=outline_width)
	output = printspace + "PrintSpace" + "_" + splitname + "_" + "light" + ".jpg"
	image.save(output, dpi=(dpi_val,dpi_val), quality=90)
	image.close()


print(" \n ************************************* ")
print(" \n Coordinates Highlighting Completed\n\n")

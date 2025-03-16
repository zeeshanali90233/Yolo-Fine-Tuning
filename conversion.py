import xml.etree.ElementTree as ET
import os

# Load XML file
xml_file = "annotations.xml"  # Change this to your file path
tree = ET.parse(xml_file)
root = tree.getroot()

output_dir = "yolo_annotations"
os.makedirs(output_dir, exist_ok=True)

for image in root.findall("image"):
    image_name = image.get("name")
    width = int(image.get("width"))
    height = int(image.get("height"))
    yolo_lines = []

    for box in image.findall("box"):
        label = box.get("label")
        xtl, ytl, xbr, ybr = float(box.get("xtl")), float(box.get("ytl")), float(box.get("xbr")), float(box.get("ybr"))

        # Convert to YOLO format (normalized values)
        x_center = ((xtl + xbr) / 2) / width
        y_center = ((ytl + ybr) / 2) / height
        bbox_width = (xbr - xtl) / width
        bbox_height = (ybr - ytl) / height

        class_id = 0  # Change this according to your dataset labels
        yolo_lines.append(f"{class_id} {x_center} {y_center} {bbox_width} {bbox_height}")
    # Save to YOLO format file
    txt_filename = os.path.join(output_dir, f"{os.path.splitext(image_name)[0]}.txt")
    with open(txt_filename, "w") as f:
        f.write("\n".join(yolo_lines))

print("Conversion completed! Check the 'yolo_annotations' folder.")

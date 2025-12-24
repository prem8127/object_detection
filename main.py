import torch
import torchvision
from torchvision.transforms import functional as F
from PIL import Image, ImageDraw, ImageFont
import os
from config import CONFIDENCE_THRESHOLD, COCO_LABELS

# Create folders if not exist
os.makedirs("images", exist_ok=True)
os.makedirs("output", exist_ok=True)

def load_model():
    print("Loading high-accuracy Faster R-CNN model...")
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn_v2(
        weights="DEFAULT"
    )
    model.eval()
    return model

def detect_objects(model, image_path):
    print(f"\nProcessing: {image_path}")

    image = Image.open(image_path).convert("RGB")
    image_tensor = F.to_tensor(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image_tensor)[0]

    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()

    detections = 0

    for box, label, score in zip(
        outputs["boxes"], outputs["labels"], outputs["scores"]
    ):
        if score < CONFIDENCE_THRESHOLD:
            continue

        x1, y1, x2, y2 = map(int, box)
        class_name = COCO_LABELS[label]

        text = f"{class_name} {score:.2f}"

        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
        draw.rectangle([x1, y1 - 22, x1 + len(text) * 9, y1], fill="red")
        draw.text((x1 + 4, y1 - 20), text, fill="white", font=font)

        print(f" ✓ {class_name} ({score:.2f})")
        detections += 1

    print(f"Total detections: {detections}")
    return image

def main():
    model = load_model()

    images = [
        f for f in os.listdir("images")
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
    ]

    if not images:
        print("⚠️ No images found in images/ folder")
        return

    for img_name in images:
        input_path = os.path.join("images", img_name)
        output_path = os.path.join("output", f"detected_{img_name}")

        try:
            result = detect_objects(model, input_path)
            result.save(output_path)
            print(f"Saved → {output_path}")
        except Exception as e:
            print(f"Error: {e}")

    print("\n🎉 Detection complete!")

if __name__ == "__main__":
    main()

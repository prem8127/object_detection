# Object Detection Project

A beginner-friendly Python project for detecting objects in images using PyTorch and pre-trained models.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Add Images
Place your images in the `images/` folder (supports .jpg, .jpeg, .png, .bmp)

### 3. Run Detection
```bash
python main.py
```

### 4. Check Results
Find detected images in the `output/` folder with red bounding boxes

## ⚙️ Configuration

Edit `config.py` to adjust:
- `CONFIDENCE_THRESHOLD`: Change detection sensitivity (0.5 = 50% confidence)

## 📦 What Objects Can Be Detected?

The model recognizes 80+ object types including:
- **People & Animals**: person, dog, cat, bird, horse, etc.
- **Vehicles**: car, truck, bus, bicycle, motorcycle, etc.
- **Indoor Items**: chair, couch, tv, laptop, book, etc.
- **Food**: pizza, sandwich, apple, banana, etc.

## 🛠️ Troubleshooting

**No images found?**
- Make sure images are in the `images/` folder
- Check file format (.jpg, .jpeg, .png, .bmp)

**Low detection accuracy?**
- Lower `CONFIDENCE_THRESHOLD` in config.py (try 0.5)
- Use higher quality/resolution images

**Installation errors?**
- Update pip: `pip install --upgrade pip`
- Try: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu`# image-detection-234567890

---

## 👤 Author

**Prem Sagar**  
🎓 B.Tech – Computer Science  
📍 India  

🔗 GitHub: https://github.com/prem8127  

💡 Interests: Artificial Intelligence, Machine Learning, Computer Vision, Deep Learning  

📫 Open to internships, projects, and learning opportunities.

---

## 📜 License

This project is licensed under the **MIT License**.  
© 2025 Prem Sagar. All rights reserved.

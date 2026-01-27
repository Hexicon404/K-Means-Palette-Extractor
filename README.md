# K-Means Palette Extractor 

### 🎨 Extracts dominant color palettes from images using K-Means clustering (OpenCV + scikit-learn)

A Python-based computer vision tool that quantifies aesthetic data. It uses **K-Means Clustering (Unsupervised Learning)** to analyze pixel distributions in image datasets and extract mathematically dominant color palettes in real-time.

**Designed for:** Automated Brand Analysis, UI/UX Design Systems, and Aesthetic Quantization.

## 🛠 Tech Stack
- **Core:** Python 3.9+
- **Computer Vision:** OpenCV (`cv2`) for high-performance image processing.
- **Machine Learning:** Scikit-Learn (`KMeans`) for unsupervised cluster detection.
- **Data Visualization:** Matplotlib & NumPy for generating centroid charts.

## ⚡️ Key Features
- **Smart Centroid Detection:** Identifies the "true" dominant colors, ignoring noise.
- **Batch Processing:** Can analyze entire directories of high-res images in seconds.
- **Hex & RGB Extraction:** Exports precise color codes for design implementation.
- **Visual Analytics:** Auto-generates pie charts and swatch kits.

## 🚀 Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

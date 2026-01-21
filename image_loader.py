from pathlib import Path
from typing import Optional
import cv2
import numpy as np
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class ImageLoader:
    def __init__(self, image_dir: str, max_size: int = 300):
        self.image_dir = Path(image_dir)
        self.max_size = max_size
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
        
    def load_images(self) -> list[np.ndarray]:
        if not self.image_dir.exists():
            raise FileNotFoundError(f"Directory not found: {self.image_dir}")
        
        images = []
        image_files = [f for f in self.image_dir.iterdir() 
                      if f.suffix.lower() in self.supported_formats]
        
        if not image_files:
            raise ValueError(f"No valid images found in {self.image_dir}")
        
        logger.info(f"Found {len(image_files)} images")
        
        for img_path in image_files:
            img = self._load_single_image(img_path)
            if img is not None:
                images.append(img)
        
        logger.info(f"Successfully loaded {len(images)} images")
        return images
    
    def _load_single_image(self, img_path: Path) -> Optional[np.ndarray]:
        try:
            img = cv2.imread(str(img_path))
            if img is None:
                raise ValueError("OpenCV failed to load image")
            
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            resized = self._resize_image(img_rgb)
            return resized
            
        except Exception as e:
            logger.warning(f"Skipping {img_path.name}: {str(e)}")
            return None
    
    def _resize_image(self, img: np.ndarray) -> np.ndarray:
        h, w = img.shape[:2]
        if max(h, w) > self.max_size:
            scale = self.max_size / max(h, w)
            new_w, new_h = int(w * scale), int(h * scale)
            return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
        return img

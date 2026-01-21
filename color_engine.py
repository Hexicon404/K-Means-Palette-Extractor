import numpy as np
from sklearn.cluster import KMeans
from typing import Tuple
import logging

logger = logging.getLogger(__name__)


class ColorEngine:
    def __init__(self, n_colors: int = 5, random_state: int = 42):
        self.n_colors = n_colors
        self.random_state = random_state
    
    def extract_palette(self, images: list[np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
        pixels = self._aggregate_pixels(images)
        logger.info(f"Clustering {len(pixels):,} pixels into {self.n_colors} colors")
        
        kmeans = KMeans(
            n_clusters=self.n_colors,
            random_state=self.random_state,
            n_init=10,
            max_iter=300
        )
        kmeans.fit(pixels)
        
        centroids = kmeans.cluster_centers_.astype(int)
        labels = kmeans.labels_
        proportions = np.bincount(labels) / len(labels)
        
        sorted_indices = np.argsort(proportions)[::-1]
        return centroids[sorted_indices], proportions[sorted_indices]
    
    def _aggregate_pixels(self, images: list[np.ndarray]) -> np.ndarray:
        all_pixels = []
        for img in images:
            pixels = img.reshape(-1, 3)
            all_pixels.append(pixels)
        return np.vstack(all_pixels)
    
    @staticmethod
    def rgb_to_hex(rgb: np.ndarray) -> str:
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    
    def get_palette_dict(self, centroids: np.ndarray, proportions: np.ndarray) -> dict:
        return {
            self.rgb_to_hex(centroid): float(proportion)
            for centroid, proportion in zip(centroids, proportions)
        }

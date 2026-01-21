import pandas as pd
from pathlib import Path
import logging
from image_loader import ImageLoader
from color_engine import ColorEngine
from visualizer import visualize_palette, create_color_swatches

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def main(image_dir: str = "images", n_colors: int = 5) -> None:
    logger.info("=== K-Means Palette Extractor: Engine Initialized ===")
    
    loader = ImageLoader(image_dir=image_dir, max_size=300)
    images = loader.load_images()
    
    engine = ColorEngine(n_colors=n_colors)
    centroids, proportions = engine.extract_palette(images)
    
    palette_dict = engine.get_palette_dict(centroids, proportions)
    
    logger.info("\nTop 5 Colors:")
    for hex_code, prop in palette_dict.items():
        logger.info(f"  {hex_code}: {prop*100:.2f}%")
    
    df = pd.DataFrame({
        'hex_code': list(palette_dict.keys()),
        'proportion': list(palette_dict.values()),
        'r': centroids[:, 0],
        'g': centroids[:, 1],
        'b': centroids[:, 2]
    })
    
    output_csv = "color_palette.csv"
    df.to_csv(output_csv, index=False)
    logger.info(f"\nData saved: {output_csv}")
    
    visualize_palette(centroids, proportions, output_path="color_palette.png")
    create_color_swatches(centroids, output_path="color_swatches.png")
    
    logger.info("\n=== Complete ===")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract dominant colors from images")
    parser.add_argument("--dir", type=str, default="images", help="Image directory")
    parser.add_argument("--colors", type=int, default=5, help="Number of colors to extract")
    
    args = parser.parse_args()
    
    try:
        main(image_dir=args.dir, n_colors=args.colors)
    except Exception as e:
        logger.error(f"Failed: {e}")
        raise

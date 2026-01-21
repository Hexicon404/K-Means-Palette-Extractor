import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def visualize_palette(
    centroids: np.ndarray,
    proportions: np.ndarray,
    output_path: str = "color_palette.png",
    dpi: int = 150
) -> None:
    
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')
    
    colors_normalized = centroids / 255.0
    
    wedges, texts, autotexts = ax.pie(
        proportions,
        colors=colors_normalized,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 11, 'weight': 'bold', 'color': 'white'}
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_path_effects([
            plt.matplotlib.patheffects.withStroke(linewidth=2, foreground='black')
        ])
    
    legend_labels = [
        f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}" 
        for c in centroids
    ]
    ax.legend(
        wedges,
        legend_labels,
        title="Hex Codes",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=10
    )
    
    ax.set_title("Top 5 Dominant Colors", fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"Visualization saved: {output_path}")


def create_color_swatches(
    centroids: np.ndarray,
    output_path: str = "color_swatches.png",
    dpi: int = 150
) -> None:
    
    fig, axes = plt.subplots(1, len(centroids), figsize=(12, 2.5), facecolor='white')
    
    if len(centroids) == 1:
        axes = [axes]
    
    for ax, color in zip(axes, centroids):
        ax.imshow([[color / 255.0]])
        ax.axis('off')
        hex_code = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
        ax.set_title(hex_code, fontsize=12, weight='bold', pad=10)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"Color swatches saved: {output_path}")

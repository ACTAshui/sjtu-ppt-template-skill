"""Shared Matplotlib style helpers for SJTU PPT scientific charts."""

from __future__ import annotations

from pathlib import Path


SJTU_PPT_PALETTE = {
    "blue": "#004098",
    "red": "#C8161E",
    "gold": "#BD9F68",
    "ink": "#172033",
    "body": "#3A4658",
    "muted": "#6B778A",
    "teal": "#2A9D8F",
    "orange": "#E69F00",
    "purple": "#7B61A8",
}


def apply_sjtu_ppt_style(plt, *, font_family: str = "Microsoft YaHei") -> None:
    """Apply a restrained SJTU/Nature-like style to a Matplotlib pyplot module."""
    plt.rcParams.update(
        {
            "figure.dpi": 160,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.04,
            "font.family": "sans-serif",
            "font.sans-serif": [
                font_family,
                "DengXian",
                "Source Han Sans SC",
                "Noto Sans CJK SC",
                "Arial",
                "DejaVu Sans",
            ],
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "axes.linewidth": 0.8,
            "axes.edgecolor": SJTU_PPT_PALETTE["ink"],
            "axes.labelcolor": SJTU_PPT_PALETTE["ink"],
            "xtick.color": SJTU_PPT_PALETTE["body"],
            "ytick.color": SJTU_PPT_PALETTE["body"],
            "grid.color": "#D7E2F0",
            "grid.linewidth": 0.5,
            "grid.alpha": 0.55,
            "legend.frameon": False,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def ppt_figure_size(kind: str = "wide") -> tuple[float, float]:
    """Return practical Matplotlib figure sizes for 16:9 PPT slides."""
    sizes = {
        "wide": (7.2, 4.05),
        "half": (4.7, 3.1),
        "square": (4.2, 4.2),
        "tall": (4.2, 5.4),
    }
    return sizes.get(kind, sizes["wide"])


def save_ppt_figure(fig, output_base: str | Path, *, transparent: bool = False) -> dict[str, str]:
    """Save PNG and PDF copies for PPT insertion and future regeneration."""
    base = Path(output_base)
    base.parent.mkdir(parents=True, exist_ok=True)
    png = base.with_suffix(".png")
    pdf = base.with_suffix(".pdf")
    fig.savefig(png, transparent=transparent)
    fig.savefig(pdf, transparent=transparent)
    return {"png": str(png), "pdf": str(pdf)}

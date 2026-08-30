import matplotlib.pyplot as plt
import seaborn as sns

# Paleta
COUNTRY_COLORS = {
    "Mexico": "#2E86AB",
    "Brazil": "#E76F51",
    "Colombia": "#F4A261",
    "Uruguay": "#6A4C93",
    "Chile": "#2A9D8F",
    "World": "#264653"
}

def set_project_style():
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        font_scale=1.1
    )

    plt.rcParams.update({
        "figure.figsize": (12, 6),
        "figure.dpi": 120,
        "axes.titlesize": 16,
        "axes.titleweight": "bold",
        "axes.labelsize": 12,
        "axes.labelweight": "normal",
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "legend.title_fontsize": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.autolayout": True
    })

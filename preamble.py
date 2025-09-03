# preamble.py (compatible IPython nuevos y antiguos)

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# --- display y set_matplotlib_formats con retrocompatibilidad ---
try:
    # Ubicación moderna (IPython >= 8 con matplotlib_inline)
    from matplotlib_inline.backend_inline import set_matplotlib_formats
except Exception:
    try:
        # Ubicación antigua (algunas versiones)
        from IPython.display import set_matplotlib_formats  # puede no existir
    except Exception:
        set_matplotlib_formats = None

# display sigue estando en IPython.display
from IPython.display import display

# Asegura backend inline si estás en Jupyter
try:
    from IPython import get_ipython
    ip = get_ipython()
    if ip is not None:
        ip.run_line_magic("matplotlib", "inline")
except Exception:
    pass

# Intenta fijar formatos (como tenías: pdf y png). Si no, usa fallback.
if set_matplotlib_formats is not None:
    try:
        set_matplotlib_formats('pdf', 'png')
    except TypeError:
        # Algunas versiones aceptan solo un conjunto; usamos retina como buena calidad
        set_matplotlib_formats('retina')
else:
    # Fallback si no existe el helper: configura vía %config o sube DPI
    try:
        if ip is not None:
            ip.run_line_magic("config", "InlineBackend.figure_formats = {'png'}")
    except Exception:
        pass
    mpl.rcParams["figure.dpi"] = 150

# --- tu configuración de estilo ---
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['image.cmap'] = "viridis"
plt.rcParams['image.interpolation'] = "none"
plt.rcParams['savefig.bbox'] = "tight"
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['legend.numpoints'] = 1

# mglearn + cycler (con pequeño guard por si falta mglearn)
try:
    import mglearn
    from cycler import cycler
    plt.rc('axes', prop_cycle=(
        cycler('color', mglearn.plot_helpers.cm_cycle.colors) +
        cycler('linestyle', ['-', '-', "--", (0, (3, 3)), (0, (1.5, 1.5))])
    ))
except Exception:
    # Si mglearn no está, deja el ciclo por defecto y sigue
    pass

# --- opciones de numpy/pandas ---
np.set_printoptions(precision=3, suppress=True)
pd.set_option("display.max_columns", 8)
pd.set_option('display.precision', 2)

__all__ = ['np', 'display', 'plt', 'pd']

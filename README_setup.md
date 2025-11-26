# Setup Python environment for this project

This file shows two recommended ways to create a Python environment that is compatible with TensorFlow (use Python 3.10). Follow either the `venv` (Option A) or `conda` (Option B) instructions.

---

**Quick check — current interpreter**

Run these in PowerShell to see your current Python versions:

```powershell
python --version
pip --version
py -0p
```

If your default interpreter is Python 3.13 or 3.14, TensorFlow wheels will not be available. Create an environment with Python 3.10 instead.

**Option A — Use a venv (Windows PowerShell)**

1. Ensure Python 3.10 is installed. If you have multiple Python versions, use the launcher `py -3.10`.
2. Create and activate a venv in the repository:

```powershell
py -3.10 -m venv .venv_tf
.\.venv_tf\Scripts\Activate.ps1
```

3. Upgrade pip and install packages:

```powershell
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

4. Register an IPython kernel for VS Code / Jupyter:

```powershell
pip install ipykernel
python -m ipykernel install --user --name tf --display-name "Python (tf)"
```

5. In VS Code open the notebook (`src/numpy.ipynb`) and select the kernel named "Python (tf)", then restart the kernel.

**Option B — Use Conda (recommended if you already have Conda/Miniconda)**

1. Create and activate a Conda environment with Python 3.10:

```powershell
conda create -n tf python=3.10 -y
conda activate tf
```

2. Upgrade pip and install packages:

```powershell
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

3. Register the kernel (optional but convenient):

```powershell
pip install ipykernel
python -m ipykernel install --user --name tf --display-name "Python (tf)"
```

4. In VS Code select the environment's interpreter or the kernel "Python (tf)" for the notebook and restart the kernel.

---

**requirements.txt**

The repository includes a `requirements.txt` for convenience. It contains the minimal packages required for the notebook:

- `numpy`
- `tensorflow`
- `ipykernel`

If you need a specific TensorFlow build (GPU), follow TensorFlow's official instructions to install the matching CUDA/cuDNN versions.

**Troubleshooting**

- If `pip` still cannot find `tensorflow`, confirm you're using Python 3.10 or 3.11 and that Windows is 64-bit.
- Upgrade `pip`, `setuptools`, and `wheel` first: `python -m pip install --upgrade pip setuptools wheel`.
- If you prefer a pinned version, update `requirements.txt` (for example `tensorflow==2.12.0`) — but only pin after confirming compatibility.

---

If you want, I can walk you through running either set of commands step-by-step in your PowerShell session.

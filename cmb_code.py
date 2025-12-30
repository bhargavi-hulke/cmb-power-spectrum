
import numpy as np
import matplotlib.pyplot as plt
from classy import Class

# Initialize the CLASS solver
model = Class()

# --- MODEL 1: High Density Universe ---
model.set({
    'omega_b': 0.02700,
    'omega_cdm': 0.1500,
    'h': 0.70,
    'output': 'tCl, lCl',
    'lensing': 'yes'
})
model.compute()
cl1 = model.lensed_cl(2500)
ll1 = cl1['ell'][2:]
clTT1 = cl1['tt'][2:]

# --- MODEL 2: Standard Density Universe ---
model.set({
    'omega_b': 0.021,
    'omega_cdm': 0.110,
    'h': 0.650,
    'output': 'tCl, lCl',
    'lensing': 'yes'
})
model.compute()
cl2 = model.lensed_cl(2500)
ll2 = cl2['ell'][2:]
clTT2 = cl2['tt'][2:]

# --- Visualization ---
plt.figure(figsize=(10, 6))
plt.plot(ll1, ll1*(ll1+1.)/2./np.pi * clTT1, label='Model 1: High Density')
plt.plot(ll2, ll2*(ll2+1.)/2./np.pi * clTT2, label='Model 2: Standard Density', linestyle='--')

ax = plt.gca()
ax.set_xscale('log')
plt.xlabel(r'Multipole $\ell$ (Scale of mode)')
plt.ylabel(r'$\frac{\ell(\ell + 1)}{2\pi} C_{\ell}$ (Power in mode)')
plt.title('Comparison of CMB Temperature Power Spectra')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

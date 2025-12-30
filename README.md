# CMB Power Spectrum Analysis with CLASS

This project utilizes the **CLASS** (Cosmic Linear Anisotropy Solving System) Boltzmann solver to simulate and analyze the **Cosmic Microwave Background (CMB)**. It compares different cosmological models to show how the "fingerprint" of the universe changes based on its fundamental composition.

---

## 🌌 About the Science

The CMB is the primordial light that has permeated the universe since it was only 380,000 years old. 

### The Process of Recombination
As the early universe expanded, it cooled. Once the temperature dropped to approximately **3000 Kelvin**, electrons combined with protons to form neutral hydrogen atoms in a process known as **"recombination"**. This event liberated the photons, allowing them to stream freely through space for the first time, making the universe transparent. 



### The Evidence: CMB & Fluctuations
This primordial glow is the evidence of the Big Bang. While it looks like a smooth glow at about **2.725 K**, there are tiny temperature differences (anisotropies) of about one part in 100,000. These small fluctuations show where the early universe had slightly different densities, which later grew into galaxies and galaxy clusters.

---

## 📈 The Angular Power Spectrum

To study these differences, we use a graph called the **Angular Power Spectrum**. This graph reveals a characteristic pattern of **"acoustic peaks,"** which serves as a unique fingerprint of the universe's fundamental composition and geometry.

---

### Input Parameters
The spectrum is determined by these fundamental cosmological parameters:
* **$\Omega_b$ (Baryon Density):** The density of ordinary matter.
* **$\Omega_{cdm}$ (Cold Dark Matter Density):** The density of invisible dark matter.
* **$H_0$ ($h$):** The Hubble constant, representing the expansion rate.
* **$\tau$:** Reionization optical depth.
* **$n_s$:** Scalar spectral index (the "tilt" of the initial fluctuations).
* **$A_s$:** Amplitude of primordial fluctuations.

The code uses `classy` to compare a **High Density Model** against a **Standard Model**.
### Prerequisites
```bash
pip install numpy matplotlib
pip install classy
# Ensure CLASS (classy) is installed in your environment
```
---

## 📊 Results & Interpretation
The comparison of the two models reveals how the "Cosmic Recipe" changes the sky:
The First Peak ($\ell \approx 200$): In Model 1, the higher density and expansion rate shift the peak and change its amplitude. The position of this peak is a standard ruler for the curvature of space.
Baryon Loading: By increasing omega_b, the odd-numbered peaks (1st, 3rd) become enhanced relative to the even-numbered peaks.
The Damping Tail: At very high $\ell$ (small angular scales), the power drops off. This is Silk Damping, where photon diffusion "washes out" the fluctuations in the early plasma.

Standard Angular Power Spectrum:
![My Analysis Result](cmb_plot1.png)

Angular Power Spectrum after corresponding parameter changes:
![My Analysis Result](cmb_plot2.png)

---

## About the Project
This project was developed to provide a visual and computational bridge between theoretical cosmology and numerical simulation. By using the CLASS Boltzmann solver, the project allows students and researchers to see the immediate physical consequences of varying the "Cosmic Recipe." I used this code for analysis of the power spectrum, when the parameters are changed, as a part of my project report under the mentoring program of REYES,UC Berkeley. It helped me explore the Early Universe and strengthen my knowledge in this field. 

##  Acknowledgments
* This work was completed under the mentorship of **REYES Program at UC Berkeley**.
* Special thanks to my mentors for their guidance in exploring the physics of the Early Universe.

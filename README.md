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



### Input Parameters
The spectrum is determined by these fundamental cosmological parameters:
* **$\Omega_b$ (Baryon Density):** The density of ordinary matter.
* **$\Omega_{cdm}$ (Cold Dark Matter Density):** The density of invisible dark matter.
* **$H_0$ ($h$):** The Hubble constant, representing the expansion rate.
* **$\tau$:** Reionization optical depth.
* **$n_s$:** Scalar spectral index (the "tilt" of the initial fluctuations).
* **$A_s$:** Amplitude of primordial fluctuations.

---

## 💻 Implementation (Python)

The following code uses `classy` to compare a **High Density Model** against a **Standard Model**.

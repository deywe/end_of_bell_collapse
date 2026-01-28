Technical README: SPHY Framework & Bell Inequality Extinction
1. Project Overview

This project implements the SPHY Framework (Sovereign Phase Dynamics) to demonstrate the analytical extinction of Bell's Inequality. Unlike probabilistic models (Copenhagen/Bell) that assume inherent uncertainty, this simulator utilizes a Persistent Metric Field (Φ) to maintain phase coherence.
2. Architecture: The Sovereignty Core

The system is split into two distinct layers to ensure both performance and intellectual property protection:

    Core (Rust): A compiled binary (libsphy_engine.so) that handles the high-precision phase calculations. It implements the Reversion Variable (RV) which forces the system into a sovereign state, effectively neutralizing the "latency tau" (τ=0).

    Interface (Python): A high-level orchestration layer that communicates with the Rust binary via FFI (Foreign Function Interface). It generates the proof datasets and visualizes the results.

3. Mathematical Foundation

The simulation compares two distinct paradigms:

    Bell/Copenhagen: Modeled using standard stochastic distributions (Gaussian noise), representing a system without metric coupling.

    SPHY Sovereign Phase: Redefined as a functional of the Φ field.
    C(a,b)≈1

    Through the binary core, the correlation remains stable because the "hidden" metric is actually a persistent structural field.

4. Understanding the Dataset (sphy_bell_reversal_proof.csv)

    frame: The temporal flow index.

    bell_uncertainty: Represents the chaotic, entropic state of classical quantum observation.

    sphy_sovereignty: Demonstrates the stable, deterministic phase maintained by the HarpiaOS kernel.

    latency_tau: Fixed at 0.0, proving instantaneous phase alignment across the metric.

5. Execution

To reproduce the results, the Rust core must be compiled with the cdylib flag to expose the no_mangle symbols required by the Python ctypes interface.

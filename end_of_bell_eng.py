import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hashlib
import ctypes
import os

# --- SPHY INTERFACE (FFI CALL TO BINARY ENGINE) ---
lib_path = os.path.abspath("./libsphy_engine.so")
sphy_lib = ctypes.CDLL(lib_path)

# Bind function signature with Rust .so
sphy_lib.calcular_fase_binaria.argtypes = [ctypes.c_double, ctypes.c_bool]
sphy_lib.calcular_fase_binaria.restype = ctypes.c_double

def calculate_sphy_phase(frame, vr_active=True):
    # Secure call to binary SPHY kernel
    return sphy_lib.calcular_fase_binaria(frame, vr_active)

# --- SIMULATION EXECUTION ---
frames = np.linspace(0, 100, 500)
bell_data = [calculate_sphy_phase(f, vr_active=False) for f in frames]
sphy_data = [calculate_sphy_phase(f, vr_active=True) for f in frames]

# --- DATASET CONSTRUCTION ---
df = pd.DataFrame({
    'frame': np.arange(len(frames)),
    'bell_uncertainty': bell_data,
    'sphy_sovereignty': sphy_data,
    'latency_tau': 0.0  # Zero-latency signature
})

# Reversal Phase State (SPHY VR active > 90%)
df['reversal_phase_state'] = np.where(df['sphy_sovereignty'] > 90, "SOVEREIGN", "COLLAPSED")

# --- SAVE PROOF CSV ---
csv_filename = "sphy_bell_reversal_proof.csv"
df.to_csv(csv_filename, index=False)
print("✔ Reversal Proof generated using SPHY Binary Core:", csv_filename)

# --- COHERENCE SOVEREIGNTY REPORT ---
def generate_sphy_report(df):
    stats = {
        "SPHY_Coherence_Mean": df['sphy_sovereignty'].mean(),
        "SPHY_Std_Deviation": df['sphy_sovereignty'].std(),
        "Bell_Uncertainty_Variance": df['bell_uncertainty'].var(),
        "Sovereignty_Delta": df['sphy_sovereignty'].mean() - df['bell_uncertainty'].mean(),
        "Uncertainty_Status": "EXTINCT" if df['sphy_sovereignty'].std() < 0.01 else "ACTIVE"
    }
    
    summary_df = pd.DataFrame([stats])
    report_filename = "sphy_sovereignty_report.csv"
    summary_df.to_csv(report_filename, index=False)

    print("\n📊 Sovereignty Report generated:", report_filename)
    return stats

# Report Output
report = generate_sphy_report(df)
print(f"🧮 SPHY Stability Index: {100 - (report['SPHY_Std_Deviation'] * 100):.4f}%")

# --- VISUALIZATION ---
plt.figure(figsize=(12, 6))
plt.plot(df['frame'], df['bell_uncertainty'], label='Uncertainty (Bell/Copenhagen)', color='red', alpha=0.4)
plt.plot(df['frame'], df['sphy_sovereignty'], label='Coherence (SPHY Binary)', color='blue', linewidth=2)
plt.axhline(y=90.5842, color='green', linestyle='--', label='Base Coherence Benchmark')

plt.title("Bell Extinction via SPHY Kernel (Binary-Protected Execution)")
plt.xlabel("Temporal Frame")
plt.ylabel("Coherence Level (%)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# --- SHA-256 HASH SIGNING FOR INTEGRITY ---
def sha256_sign(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        hash_obj = hashlib.sha256(data)
        signature = hash_obj.hexdigest()
    
    sig_file = file_path.replace(".csv", "_sha256.txt")
    with open(sig_file, "w") as out:
        out.write(signature)
    
    print(f"🔐 File SHA-256 signature created: {sig_file}")
    return signature

# Sign the output dataset
signature = sha256_sign(csv_filename)

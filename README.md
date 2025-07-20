# Chakravyuh
Chakravyuh 🛡️ is a military-grade encryption and intrusion response system featuring chaotic AES encryption, system fingerprint logging, IP-tracking decoy triggers, VPN scrambling, and adaptive countermeasures. Built for red teams, honeypots, and cyber defense simulations.
# Chakravyuh 🛡️
A military-grade encryption, intrusion detection, and decoy-trigger system designed for cyber defense, deception, and threat response in high-security environments.

---

## 🔥 Features

- 🔐 **Chaotic AES-CFB Encryption**
  - Unpredictable key generation using logistic map
- 🕵️ **Intrusion Detection**
  - Device fingerprinting (OS, MAC, CPU, hostname)
  - Logged in tamper-resistant format
- 🎭 **Decoy Web Trap**
  - `decoy.html` sends intruder's IP to a webhook upon access
- 🧠 **Adaptive Response**
  - Optionally scrambles VPN to expose real IP
  - Optional reverse shell trigger
- 🔒 **Tamper Logging**
  - Secure logs of all system events and triggers

---

## 🚀 Getting Started

### 1. **Install Requirements**
```bash
pip install pycryptodome requests

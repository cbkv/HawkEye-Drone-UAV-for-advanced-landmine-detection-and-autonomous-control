# 🚁 Flight Modes – HawkEye Drone

This document explains the flight modes used in the HawkEye Drone system.

---

## 📌 1. Stabilize Mode

* Manual control with auto-leveling
* Pilot controls throttle, roll, pitch, yaw
* Used for testing and manual flying

---

## 📌 2. AltHold Mode

* Maintains constant altitude
* Pilot controls horizontal movement
* Useful for stable hovering

---

## 📌 3. Loiter Mode (GPS Required)

* Holds position using GPS
* Automatic stabilization
* Used for scanning specific areas

---

## 📌 4. Guided Mode

* Controlled via scripts or Ground Control Station
* Used for autonomous navigation
* Important for AI-based mission control

---

## 📌 5. Auto Mode (Mission Mode)

* Executes pre-defined waypoints
* Fully autonomous flight
* Used for landmine scanning missions

---

## 📌 6. RTL (Return to Launch)

* Drone returns to home location
* Triggered on low battery or failsafe
* Ensures safety

---

## 🎯 Recommended Modes for This Project

| Purpose        | Mode      |
| -------------- | --------- |
| Testing        | Stabilize |
| Hover scanning | Loiter    |
| AI control     | Guided    |
| Full mission   | Auto      |
| Emergency      | RTL       |

---

## ⚠️ Safety Notes

* Always calibrate sensors before flight
* Ensure GPS lock before using Loiter/Auto
* Monitor battery voltage
* Test in open area first

---

## 🧠 Project Usage

In HawkEye Drone:

* **Auto Mode** → Executes scanning path
* **Guided Mode** → AI-based control from Raspberry Pi
* **RTL Mode** → Emergency return

---

# 🚁 HawkEye Drone – UAV for Advanced Landmine Detection

## 📌 Overview

HawkEye Drone is an **AI-powered autonomous UAV system** designed to detect landmines safely and efficiently. It combines **thermal imaging, metal detection, and machine learning** to identify both metallic and non-metallic mines.

---

## ❗ Problem Statement

Landmines continue to pose a serious threat in post-conflict regions, causing thousands of casualties every year.

* Traditional methods are **slow and dangerous**
* Cannot detect **non-metallic mines effectively**
* Thermal detection affected by **environmental conditions**

---

## 💡 Proposed Solution

A **dual-detection UAV system** that integrates:

* 🔍 Metal Detection (Hardware)
* 🌡️ Thermal Imaging (Software)
* 🧠 AI/ML for pattern recognition
* 📍 GPS-based mapping

👉 As shown in the system architecture, the drone uses Pixhawk for flight control and Raspberry Pi for onboard AI processing.

---

## ⚙️ Key Features

* 🚁 Autonomous flight using Pixhawk
* 🔥 Thermal image-based detection
* 🧲 Metal sensor-based detection
* 🧠 AI-powered classification
* 📡 Real-time GPS tracking
* 🚧 Obstacle avoidance
* ⚡ Instant alerts

---

## 🏗️ System Architecture

The system consists of:

### Hardware

* Drone frame + motors
* Pixhawk flight controller
* Metal detector sensor
* Thermal camera
* GPS module
* Raspberry Pi

### Software

* OpenCV (image processing)
* TensorFlow / ML model
* MAVLink communication
* Mission Planner (GCS)

---

## 🔬 How It Works

1. Drone follows autonomous flight path
2. Metal sensor scans ground
3. Thermal camera captures heat patterns
4. Raspberry Pi processes data using AI
5. Landmine detected → GPS location logged
6. Alert generated in real-time

---

## 📊 Results

* Detects both metallic & non-metallic mines
* Reduces human risk
* Works across different terrains

---

## 📈 Advantages

* Safe & non-invasive
* Covers large areas quickly
* AI improves detection accuracy
* Works in harsh environments

---

## ⚠️ Limitations

* Battery constraints
* Environmental noise
* Initial setup cost

---

## 🎯 Future Scope

* GPR & LiDAR integration
* Fully autonomous swarm drones
* Cloud-based monitoring system
* Deployment in real-world demining

---

## 👨‍💻 Team

**Agile Avengers – R.M.D Engineering College**

* Krishna Vishwa
* Jaibalaji S.T
* (Add others)

---

## 📜 License

This project is under development and may include patent-pending components.

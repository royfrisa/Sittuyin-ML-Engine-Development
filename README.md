# Sittuyin ML Engine & Play/Learn Platform

> A web platform and machine learning engine mainly for preserving, learning, and playing **Sittuyin**, a traditional chess variant from Myanmar.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)]()

---

## About The Project

Sittuyin is a strategic board game deeply loved in Myanmar, yet largely underrepresented in the digital and tech spaces. And I'm trying to make a attempt at changing it.

**Sittuyin ML Engine** is a portfolio initiative designed to bridge traditional culture with modern artificial intelligence and web development as I'm both learning and building the same time.

### Why This Project?
* **Cultural Preservation:** One thing I've realized while I'm researching about this project is there isn't enough resources and tools that will bring this game to a global audience. So this is going to be my attempt trying to get the Sittuyin into a global IT built space.

* **Applied Machine Learning:** I'm using 64 int array currently but slowly moving to bitboard representations, Minimax search, and Convolutional Neural Networks (CNNs) to a complex, asymmetric opening/setup game structure (hopefully)
* **Full-Stack Engineering:** I'm trying to consume much knowledge and information as possible about building a end-to-end ecosys interactive learning and playing platform.

## Key Features & User Journey

* **Play vs. AI:** Challenge a trained Sittuyin engine locally or online.

* **Interactive Learning Hub:** I'll be uploading Step-by-step guides and clear and easy to understand tutorials for beginners to Sittuyin. Did I mentioned Sittuyin is a Burmese variant of the Chess we all know and play at some point? 

* **Engine Training Pipeline:** Automated data collection from web data and self-play data generation to continuously improve the ML model's evaluation function.

## Roadmap & MVP Scope

Hopefully, I want to deliver a quality portfolio piece that benefits the Sittuyin interests. 

The project follows a phased rollout:

### Phase 1: MVP (Current Focus)
- [x] Core Sittuyin game rules and board validation logic.
- [ ] Usable web frontend to play offline/local turns.
- [ ] Initial rule-based / Minimax AI opponent.
- [ ] Interactive "Learn Sittuyin" section.

### Phase 2: ML & Data Enhancement
- [ ] Implement bitboard data structures for performance optimization.
- [ ] Train a Convolutional Neural Network (CNN) / heuristic evaluation hybrid model.
- [ ] Self-play data generation pipelines.

### Phase 3: Future Scale
- [ ] User profiles and matchmaking system for online Player vs. Player.
- [ ] Advanced telemetry and match history recording for continuous model training.

---

## Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript / MD Web Framework
* **Backend & Engine:** Python, NumPy, Bitboards, Minimax Algorithm, PyTorch/TensorFlow (CNN)
* **API / Communication:** REST / WebSockets for engine communication

## Getting Started (Local Development)

*(Instructions for setting up the development environment will be updated as the repository matures.)*

```bash
# Clone the repository
git clone [https://github.com/royfrisa/Sittuyin-ML-Engine-Development.git](https://github.com/royfrisa/Sittuyin-ML-Engine-Development.git)

# Navigate to project directory
cd Sittuyin-ML-Engine-Development
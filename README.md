# Manim Math Animation Project

A project for creating mathematical animations using Manim.

## Setup Instructions

### 1. Install Python
- Download Python 3.10+ from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running Animations

To render a scene:
```bash
manim -pql scene.py BasicScene
```

**Flags:**
- `-p`: Preview the animation after rendering
- `-ql`: Quality low (faster rendering)
- `-qh`: Quality high (better quality, slower)

## Available Scenes

- `BasicScene`: Simple text animation
- `MathScene`: Mathematical equation example
- `GeometryScene`: Geometric shapes demonstration

## Usage

Run any scene with:
```bash
manim -pql scene.py SceneName
```

Replace `SceneName` with any of the available scenes.
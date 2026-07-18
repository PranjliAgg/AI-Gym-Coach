# 🏋️CoachFit AI - Your Real-time AI Gym Coach

An AI-powered real-time fitness coach that uses **computer vision, pose estimation, and LLM-based voice guidance** to analyze workouts, count repetitions, and provide personalized feedback like a virtual personal trainer.

## ✨ Features

- 🎥 **Real-time Exercise Tracking**
  - Live pose detection using computer vision
  - Tracks body movements and exercise patterns through webcam input

- 🔢 **Automatic Rep Counting**
  - Counts repetitions for multiple exercises with 90%+ accuracy
  - Maintains workout progress and set tracking

- 🧍 **Form Analysis**
  - Evaluates exercise posture using body landmarks
  - Provides feedback on incorrect movement patterns

- 🤖 **AI Voice Coaching**
  - LLM-powered workout guidance
  - Real-time feedback and motivation using voice synthesis

- 📊 **Workout Analytics**
  - Stores workout history
  - Tracks reps, sets, duration, and exercise performance

- 🔐 **User Authentication**
  - Personalized workout sessions
  - Secure user data management

---

## 🏋️ Supported Exercises

Currently supported:

- Squats
- Push-ups
- Biceps Curls
- Shoulder Press
- Lunges

---

## 🛠️ Tech Stack

### Computer Vision & AI
- Python
- OpenCV
- MediaPipe Pose Estimation
- Groq LLM API
- gTTS (Text-to-Speech)

### Application
- Streamlit
- Streamlit WebRTC
- SQLite

### Development
- Git & GitHub
- Object-Oriented Python Architecture

---

## ⚙️ How It Works

```
Webcam Input
      ↓
Pose Detection (MediaPipe)
      ↓
Exercise-specific Analysis
      ↓
Rep Counting + Form Evaluation
      ↓
LLM-based Coaching Feedback
      ↓
Voice Guidance
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Gym-Coach.git
cd AI-Gym-Coach
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

Start the Streamlit app:

```bash
streamlit run main.py
```

The application will open in your browser.

---


## 🎯 Future Improvements

- 📱 Mobile-friendly interface
- 📈 Advanced workout analytics dashboard
- 🏃 More exercise support
- 🧠 Personalized workout recommendations
- 🗣️ More natural AI coaching conversations

---

⭐ If you found this project interesting, consider starring the repository!

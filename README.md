# 🎓 Online Quiz System (Python Tkinter) 🚀-
# 🎓 Online Quiz System (Python Tkinter) 🚀

A comprehensive desktop application built with Python's **Tkinter** library, featuring a multi-window interface, custom graphics, and automated scoring systems.

---

## 🛠 Project Workflow

### 1. 🔐 Login Page (Customized Interface)
The system starts with a professional and sleek **Login Window**.
* **🖼️ Customized Design:** It features a custom-designed workspace background image to provide a modern aesthetic.
* **✍️ User Entry:** The student is prompted to enter their **Name** and **Student ID** using interactive placeholder-styled fields.
* **🖱️ Action:** Clicking the **Login** button authenticates the session and launches the main dashboard.

---

### 2. 🏠 Main Dashboard (Personalized Welcome)
Once logged in, the student is greeted by a personalized **Main Dashboard**.
* **✨ Visuals:** This window uses a customized educational background (classroom theme) to set the mood for learning.
* **👤 Personalization:** It dynamically displays the student's specific **Name** and **ID**.
* **▶️ Action:** The student clicks the **"Start Quiz"** button to proceed to the quiz categories.

---

### 3. 🎯 Quiz Selection Window
A dual-pane navigation window that allows the student to choose their assessment path.
* **🎨 UI Design:** The screen is split into two clear sections with custom icons and a dark-themed layout.
* **📚 Options:** Users can choose between two distinct modes:
    * **MCQs QUIZ:** Multiple Choice Questions for quick testing.
    * **WRITTEN QUIZ:** Subjective/Theory Questions for detailed answers.
* **🔘 Selection:** Large, interactive buttons like **"Attempt MCQs"** make the selection process seamless.

---

### 4. 📝 MCQs Quiz Session
If the student chooses MCQs, the interactive testing engine begins.
* **🖥️ Interface:** Questions appear one at a time on a clean, distraction-free black background.
* **🔘 Interaction:** Options are presented with radio buttons for quick selection.
* **⚙️ Logic:** The student selects an answer and clicks **"Next"**. The system tracks the score accurately in the background.

---

### 5. 🏆 MCQs Final Result
Upon answering the final question, the system instantly processes the data.
* **📊 Output:** An informative **Result Popup** appears, displaying the final score (e.g., `MCQs Score: 4 / 5`). ✅

---

### 6. ⌨️ Written Quiz Session
The **Written Quiz** provides a platform for detailed subjective answers.
* **📑 Structure:** Academic questions (e.g., "Define OOP") are displayed with dedicated **Multi-line Text Areas**.
* **🖋️ Action:** Students can type their detailed explanations and click the green **"Submit"** button when finished.

---

### 7. 📈 Written Marks Calculation
Once submitted, the system validates the response entries.
* **🔔 Output:** A final **Result Message Box** is triggered, showing the total marks achieved based on the input (e.g., `Written Marks: 10 / 15`). 🎖️

---

## 🖼️ Graphics & UI

> [!IMPORTANT]  
> All background images in this project (Login, Dashboard, and Quiz Selection) have been **custom-created and resized** to ensure a high-quality, professional user experience.

---

### 🚀 How to Run
1. Ensure you have Python installed.
2. Install the required library:
  
   pip install Pillow

# LeetCode DSA Intuition Helper Chrome Extension

A beautiful Chrome extension and Python backend that fetches LeetCode problem descriptions and uses Google Gemini to generate clear, well-formatted intuition and complexity explanations for any LeetCode problem.

---

## Features

- **One-click intuition:** Just click the extension on any LeetCode problem page—no need to enter the problem slug.
- **Automatic detection:** The extension auto-detects the problem slug from the URL.
- **Modern UI:** Inspired by premium algorithm analyzers, with a dark gradient, accent colors, and card-based layout.
- **Gemini-powered:** Uses Google Gemini to generate detailed brute force and optimal solution explanations, with time and space complexity.
- **Markdown formatting:** Output is rendered with bold, italic, and lists for easy reading.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/leetcode-dsa-intuition-helper.git
cd leetcode-dsa-intuition-helper
```

### 2. Backend Setup

#### a. Install Python dependencies

```bash
pip install -r requirements.txt
```
If `requirements.txt` is missing, install manually:
```bash
pip install flask flask-cors google-generativeai requests html2text python-dotenv
```

#### b. Configure your Gemini API Key

- Create a `.env` file in the project root:
  ```
  GEMINI_API_KEY=your_gemini_api_key_here
  ```
- You can get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

#### c. Run the backend

```bash
python gemini_backend.py
```
- The backend will start on `http://localhost:5000`.

---

### 3. Chrome Extension Setup

#### a. Load the extension in Chrome

1. Open Chrome and go to `chrome://extensions/`.
2. Enable **Developer mode** (top right).
3. Click **Load unpacked** and select the project folder.

#### b. Using the extension

1. Go to any LeetCode problem page (e.g., `https://leetcode.com/problems/add-two-numbers/`).
2. Click the extension icon in your browser.
3. Click **Get Intuition & Complexity**.
4. Wait for the Gemini-generated intuition to appear, beautifully formatted.

---

## Customization

- **Icons:** Replace `icon16.png`, `icon48.png`, and `icon128.png` with your own PNG icons for a professional look.
- **Styling:** The popup UI is easily customizable via `popup.html` and its `<style>` section.
- **Backend deployment:** To use the extension outside your local machine, deploy the backend to a cloud service and update the backend URL in `popup.js`.

---

## Troubleshooting

- **Failed to fetch:** Make sure the backend is running and accessible at `http://localhost:5000`.
- **CORS errors:** The backend is configured to allow all origins. If you still see CORS issues, restart the backend.
- **No intuition or error from Gemini:** Check your API key and backend logs for errors.
- **Firewall/Antivirus:** Ensure nothing is blocking connections to `localhost:5000`.
- **Not on a LeetCode problem page:** The extension only works on URLs like `https://leetcode.com/problems/<slug>/`.

---

## License

MIT

---

**Enjoy building your DSA intuition with the power of Gemini and a beautiful Chrome extension!**

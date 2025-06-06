# LeetCode DSA Intuition Helper Chrome Extension

This project provides a Chrome extension and a Python backend that fetches LeetCode problem descriptions and uses Google Gemini to generate intuition and complexity explanations for any LeetCode problem.

---

## Features
- Enter any LeetCode problem slug (e.g., `two-sum`, `add-two-numbers`) in the extension popup.
- Instantly get intuition and complexity for brute force and optimal solutions, powered by Gemini.

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
  ```env
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
1. Click the extension icon in your browser.
2. Enter a LeetCode problem slug (e.g., `two-sum`).
3. Click **Get Intuition & Complexity**.
4. Wait for the Gemini-generated intuition to appear.

---

## Troubleshooting
- **Failed to fetch**: Make sure the backend is running and accessible at `http://localhost:5000`.
- **CORS errors**: The backend is configured to allow all origins. If you still see CORS issues, restart the backend.
- **No intuition or error from Gemini**: Check your API key and backend logs for errors.
- **Firewall/Antivirus**: Ensure nothing is blocking connections to `localhost:5000`.

---

## Customization
- You can further style the popup or add features (e.g., auto-detecting the slug from the current tab).
- To deploy the backend, use a cloud service and update the extension's backend URL in `popup.js`.

---

## License
MIT 
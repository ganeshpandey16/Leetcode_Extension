function formatMarkdownToHTML(text) {
    // Bold: **text**
    text = text.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>');
    // Italic: *text*
    text = text.replace(/\*(.*?)\*/g, '<i>$1</i>');
    // Numbered lists: 1. text\n 2. text
    text = text.replace(/^(\d+)\. (.*)$/gm, '<b>$1.</b> $2');
    // Bullet lists: * text
    text = text.replace(/^\* (.*)$/gm, '<ul><li>$1</li></ul>');
    // Replace double newlines with <br><br>
    text = text.replace(/\n\n/g, '<br><br>');
    // Replace single newlines with <br>
    text = text.replace(/\n/g, '<br>');
    // Merge adjacent <ul>s
    text = text.replace(/<\/ul>\s*<ul>/g, '');
    return text;
}

document.getElementById('fetchBtn').addEventListener('click', async () => {
    document.getElementById('result').innerHTML = 'Fetching intuition using Gemini...';
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (!tabs || !tabs[0] || !tabs[0].url) {
            document.getElementById('result').innerHTML = 'Unable to detect the current tab URL.';
            return;
        }
        const url = tabs[0].url;
        const match = url.match(/^https:\/\/leetcode\.com\/problems\/([a-z0-9\-]+)\//);
        if (!match) {
            document.getElementById('result').innerHTML = 'Not on a LeetCode problem page!';
            return;
        }
        const slug = match[1];
        fetch('http://localhost:5000/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ slug })
        })
        .then(res => res.json())
        .then(data => {
            if (data.intuition) {
                document.getElementById('result').innerHTML = formatMarkdownToHTML(data.intuition);
            } else if (data.error) {
                document.getElementById('result').innerHTML = 'Error: ' + data.error;
            } else {
                document.getElementById('result').innerHTML = 'No intuition received from backend.';
            }
        })
        .catch(err => {
            document.getElementById('result').innerHTML = 'Error contacting backend: ' + err.message;
        });
    });
}); 
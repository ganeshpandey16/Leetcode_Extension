// Content script for LeetCode DSA Intuition Helper
function getLeetCodeProblem() {
    const titleElem = document.querySelector('h1[data-cy="question-title"]');
    const descElem = document.querySelector('.content__u3I1.question-content__JfgR');
    if (titleElem && descElem) {
        return {
            title: titleElem.innerText.trim(),
            description: descElem.innerText.trim()
        };
    }
    return null;
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.type === 'GET_PROBLEM') {
        const problem = getLeetCodeProblem();
        sendResponse(problem);
    }
    return true;
}); 
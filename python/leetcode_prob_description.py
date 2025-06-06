import requests
import html2text

def get_leetcode_problem_description(title_slug, return_title=False):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{title_slug}/"
    }
    payload = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": title_slug},
        "query": '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                title
                content
            }
        }'''
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        question = data.get("data", {}).get("question", {})
        if question:
            raw_text = html2text.html2text(question["content"])
            clean_text = "\n".join([line for line in raw_text.splitlines() if line.strip() != ""])
            if return_title:
                return question["title"], clean_text
            return clean_text
        else:
            return None if not return_title else (None, None)
    else:
        return None if not return_title else (None, None)

if __name__ == "__main__":
    desc = get_leetcode_problem_description("add-two-numbers")
    print(desc)
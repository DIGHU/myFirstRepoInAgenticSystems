# Conceptual Answers

## 1. What is the role of query parameters in this request?

Query parameters are used to send additional information to the API to customize the response.

In this request:
- q=python → searches repositories related to Python
- sort=stars → sorts repositories based on stars
- order=desc → sorts in descending order
- per_page=5 → limits results to 5 repositories

They help control what data we get from the API without changing the endpoint.


## 2. Why do we use response.json() instead of response.text?

- response.json() converts the API response directly into a Python dictionary.
- It makes it easy to access data using keys like data["items"].

- response.text returns raw text (string format), which is harder to work with.

So, response.json() is preferred because:
- It is structured
- Easier to read and use in code
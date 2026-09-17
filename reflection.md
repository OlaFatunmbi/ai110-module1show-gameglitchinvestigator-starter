# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- the game would not be allowed to reset.
- the game would always put "Go Lower" no matter what the number is?

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|--20---|----"Go Higher"----|"Go Lower"(hint)-|--------"None"----------|
|new game|--reset numbers---|not allowed reset|---------None-----------|
|---0---|--- not allowed----|allowed as a guess|-------"Go Lower"------|


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- I used Claude.ai
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- I had to fix the "New Game" button to fully reset and allow the difficulty to be changed.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
- It wanted me to fix the "Too High" by taking current_score - 5,but that makes the branches redundant as they both have the same.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- I have to test it.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- I had claude create a pytest in which 22 passed in 0.15s.
- Did AI help you design or understand any tests? How?
- Yes, AI helped me understand exactly what I was aiming for and what results are necessary to call it a success.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

- Streamlit refreshes the code after every interaction, while session state acts like the app's memory so your info doesn't reset each time. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- Really using AI as a tool has helped tremendously, because even ifd I do not understand something, AI can help break it down.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- I would really ask AI to explain the code and each change it made and why, to help me better understand.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- This honestly taught me that AI does not actually know everything and may be incorrect. AI can be a useful tool but without understanding the code, I'm not doing much work.

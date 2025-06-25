# 📊 Prompt Evaluation Report – Medical Q&A Agent

## 🧠 Overview
This report evaluates four prompting strategies—Zero-shot, Few-shot, Chain-of-Thought (CoT), and Meta-prompting—on a medical assistant LLM using Qwen1.5-0.5B. The evaluation criteria include accuracy, reasoning clarity, hallucination, and consistency.

---

## 🔍 Summary Table

| Prompt Type     | Accuracy (out of 5) | Reasoning Clarity | Hallucinations | Consistency |
|-----------------|---------------------|-------------------|----------------|-------------|
| Zero-shot       | 4/5                 | Low               | 1              | Medium      |
| Few-shot        | 1/5                 | Very Low          | 0              | Very Low    |
| Chain-of-Thought| 2/5                 | High              | 2              | Low         |
| Meta-prompt     | 3/5                 | Medium            | 2              | Medium      |

---

## 📌 Observations

- **Zero-shot** responses were mostly factually correct but suffered from repetition or verbosity.
- **Few-shot** responses were largely unrelated or abruptly cut off, indicating misalignment with task intent.
- **CoT prompts** often over-explained or introduced medical exaggerations, though clarity was high.
- **Meta-prompt** generated relatively natural language but included subtle medical hallucinations.

---

## ✅ Recommendation

- Use **Zero-shot** for fast and generally reliable output with caution for verbosity.
- Use **CoT** when clarity of reasoning is important, but monitor for over-generation.
- Avoid **Few-shot** until better examples are curated.


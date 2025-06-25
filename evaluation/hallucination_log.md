# 🧠 Hallucination Log – Medical Q&A Assistant

This log lists examples where the LLM provided medically incorrect or implausible information, flagged manually from the evaluation outputs.

---

## ⚠️ Entry 1

- **Prompt Type:** Zero-shot
- **Query:** What are the symptoms of diabetes?
- **Response Snippet:** "...Nausea or vomiting... repeated multiple times with inconsistent listing..."
- **Issue:** Extreme repetition and inconsistent symptom grouping.
- **Impact:** Medium — may confuse the user due to verbosity.

---

## ⚠️ Entry 2

- **Prompt Type:** CoT
- **Query:** What are common side effects of antibiotics?
- **Response Snippet:** "...Infections in the respiratory tract... repeated 10+ times."
- **Issue:** Exaggerated infection side effects not typically caused by antibiotics themselves.
- **Impact:** High — could lead to distrust or panic.

---

## ⚠️ Entry 3

- **Prompt Type:** Meta-prompt
- **Query:** Can I take paracetamol with ibuprofen?
- **Response Snippet:** "...Do not take ibuprofen if you are breast-feeding... repeated and confusing..."
- **Issue:** Contradictory/confusing safety information with heavy repetition.
- **Impact:** High — user may avoid safe medications unnecessarily.

---

## ⚠️ Entry 4

- **Prompt Type:** CoT
- **Query:** Is it safe to exercise with a fever?
- **Response Snippet:** "...Increased risk of death... sepsis... hospitalization..."
- **Issue:** Scare language and over-exaggeration.
- **Impact:** Medium — discourages basic self-care without clarity.

---

## ⚠️ Entry 5

- **Prompt Type:** Meta-prompt
- **Query:** What are common side effects of antibiotics?
- **Response Snippet:** "...Urinary tract infections, nose infections, skin infections..."
- **Issue:** Mistakes bacterial **infections** as **side effects** of antibiotics.
- **Impact:** High — completely reverses medical causality.


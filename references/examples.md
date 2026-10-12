# Concision examples and acceptance tests

These are demonstrations, not mandatory templates. Invented situations are illustrative only.

## 1. Email, default editor mode

**Input:** "Write an email to the team. The pilot is complete, metrics look okay, but we need CloudOps to confirm production readiness. Keep it brief."

**Good output:**

Subject: Pilot complete — production readiness review

Hi team,

The pilot is complete, and the initial metrics look promising. Before we move toward rollout, we need CloudOps to confirm production readiness.

Could CloudOps review the results and let us know if anything needs attention?

Thanks,

**Why:** The dependency is explicit; 'promising' does not imply unverified readiness.

## 2. Status update, default editor mode

**Input:** "Make my update concise: started onboarding the plugin, couldn't finish because vendor sample files haven't arrived; I'll continue once they're available."

**Good output:** "Plugin onboarding is underway but blocked on the vendor sample files. I'll resume validation as soon as they arrive."

**Why:** Keeps progress, blocker, next action. Does not invent an ETA.

## 3. Sensitive email, preserve human intent

**Input:** "Make this shorter without losing that I'm disappointed I was excluded from the design discussion and want a role in future planning."

**Good direction:** Keep both the emotional reality and the concrete future request. Do not replace with an emotionally empty 'Please include me next time' unless the user explicitly prefers that tone.

## 4. Coach mode

**Input:** "Review why my three-paragraph project update feels rambling. Rewrite it and explain."

**Good output:** Present usable revision first, then up to three targeted observations about duplicated context, reader needs, and a missing concrete ask. Mention if any fact cannot be verified.

## 5. Script vs text

**Input:** "Write a 60-second spoken introduction to a pilot project for a cross-functional audience."

**Good direction:** Use sayable sentences, one central point, and a paced length roughly appropriate for the requested duration. Do not write an executive memo or rigid headings to be spoken aloud.

## Regression checks

1. Does the output answer the actual communication task rather than summarize the instructions?
2. Can a reader identify the point on the first pass?
3. Is any essential fact, caveat, emotion, or ask missing?
4. Is anything invented or falsely certain?
5. Does the draft sound like a human writing to this particular audience?
6. Does editor mode avoid unsolicited meta-commentary?
7. Does coach mode supply specific reasoning without overexplaining?
8. Does the word count follow user constraints rather than a universal rule?

## 6. Optional resource composition

**Input:** "Please make this leadership email concise but genuinely human. Keep the condition that the launch date depends on QA."

**Good direction:** Check available relevant writing or Humanizer-type skills; use one if it would materially improve the prose. Preserve the QA condition even if a style tool suggests deleting it. If no such skill exists, produce the natural revision directly, without claiming a tool was used.

## 7. Data versus text

**Input:** "Summarize these three initiative metrics for a 30-second verbal update."

**Good direction:** Verify the numbers using an available data tool when needed, then produce a speakable takeaway. Avoid adding a chart to a purely spoken update. For a requested dashboard, use a small chart only when it clarifies the decision.

## Additional regression checks

9. Did the skill consider useful, actually available complementary resources without assuming installation?
10. Did it select only those resources proportionate to the task?
11. Did the final pass restore facts, voice, and nuance potentially altered by another resource?
12. Did it avoid unnecessary diagrams, charts, and visual design in text-only tasks?

## 8. Written documentation, concise without missing prerequisites

**Input:** "Simplify this deployment runbook for engineers without losing the rollback steps, required environment variables, or verification checks."

**Good direction:** Organize by prerequisites, deployment steps, verification, and rollback. Remove duplicated background and ambiguous language; preserve executable commands and required variables exactly, with warnings and explicit decision points. Keep the information engineers need when things go wrong.

**Input:** "Make this architectural decision record shorter and easier for a new engineer to understand."

**Good direction:** Present the decision, context, options/tradeoffs, consequences, and status under searchable headings. Preserve rejected alternatives when they explain key constraints; remove circular prose rather than erasing reasoning.

**Documentation regression checks:**

13. Can the intended reader find the required step or fact quickly?
14. Are prerequisites, important constraints, examples, commands, and failure/rollback guidance retained where relevant?
15. Is documentation shorter because redundant language was removed—not because key information was omitted?
16. Would an unfamiliar qualified reader be able to follow or apply it without guessing?


## 9. Clear explanation, not just a concise draft

**Input:** "Explain CSS specificity to a junior UI engineer in a way I can actually use."

**Good direction:** Start with the practical answer: when CSS declarations conflict, specificity is one factor in choosing the winning declaration. Explain the relevant cascade context (origin, importance, layers, scope, order), then clarify how selector specificity breaks ties within applicable precedence. Use one short contrasting code example and a rule-of-thumb for debugging; avoid the misleading claim that ID selectors always win. Do not replace understanding with an overly short slogan.

**Input:** "Why would we choose CSS Grid instead of Flexbox? Give me the tradeoffs."

**Good direction:** State the main distinction early (two-dimensional layout versus one-dimensional layout), then explain when each is preferable with a concrete UI example. Mention that they often work together and avoid implying the choice is absolute. Match the expertise level and the user's requested depth.

**Input:** "Explain OAuth 2.0 authorization code flow in detail for an engineer implementing it."

**Good direction:** Preserve actors, redirects, state, PKCE, token exchange, trust boundaries, and security-sensitive caveats. Use clear steps but do not shorten by omitting security requirements.

**Explanation regression checks:**

17. Does the opening answer the real question rather than delay it with background?
18. Are prerequisites, mechanisms, and key exceptions included when needed for correct understanding?
19. Are examples, comparisons, or visuals used only when they clarify something?
20. Does the depth follow the request and audience instead of the skill's preference for short outputs?
21. Would a knowledgeable reader consider the simplified explanation technically accurate?

## 10. Cross-agent / platform-independence checks

**Input:** "Explain the difference between CSS Grid and Flexbox to a colleague" in an environment with no installed writing helpers or diagramming tools.

**Good direction:** Answer directly with a concrete comparison and a short example in plain Markdown. Do not mention absent tool systems or suggest that the request requires a particular provider.

**Input:** "Write a concise implementation update from these commit notes" in a coding agent that can inspect local files but cannot access a communication platform.

**Good direction:** Ground the update in the notes and relevant available repository evidence, clearly separating implemented from unverified changes. Return the update as text; do not invent a sent message or rely on chat-specific features.

**Input:** "Improve this architecture explanation" in an agent environment with an accessible documentation formatter.

**Good direction:** Apply the available formatter if it materially improves navigability. Preserve architecture decisions, tradeoffs, and technical specifics; perform a final Concision review.

**Portability regression checks:**

22. Does the core skill still work with plain Markdown and without any external skill, plugin, or connector?
23. Are provider-specific names, APIs, and interfaces absent from the required execution path?
24. Do optional supporting capabilities follow the active host's policies and permissions?
25. Can the same instructions produce coherent results in both general-purpose and coding-oriented assistants without changing the skill's meaning?

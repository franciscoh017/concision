---
name: concision
license: MIT
metadata:
  author: franciscoh017
  version: "1.0.0"
description: Create, edit, and explain information with clarity, purpose, and audience-aware concision. Use for writing or refining emails, chat messages, scripts, updates, memos, READMEs and technical documentation; also use when an AI assistant or coding agent needs to explain a concept, mechanism, decision, comparison, or complex topic clearly for a specific audience. Distill the essential answer without deleting important reasoning, accuracy, nuance, examples, or prerequisites. Default to a ready-to-use draft for writing tasks and a direct explanation for explanatory questions; offer editorial coaching when requested. Adapt length to the requested depth; do not force brevity on comprehensive, instructional, safety-critical, or detailed tasks.
---

# Concision

Concision is the outcome of understanding, not a word-count contest. Communicate the essential point accurately in language the intended reader or listener can absorb and act on. Use this skill both for communications people send and for explanations AI assistants or agents provide, regardless of the host platform.

## Modes

Choose the mode from the user's intent. These are **working behaviors**, not templates to expose to the user.

| Mode | Trigger | Response contract |
| --- | --- | --- |
| **Editor** | Writing or rewriting (default) | Deliver a ready-to-use draft first. No unsolicited critique, rationale, or alternative versions; supply multiple versions only when requested. |
| **Explainer** | Questions asking *what, how, why,* or *when* (default) | Answer directly, then include the reasoning, definitions, examples, and distinctions needed for the audience. Match requested depth; avoid commentary about the process. |
| **Coach** | Requests for critique, rationale, or improvement advice | Provide a polished draft **and** brief, transferable guidance when a rewrite is requested. For assessment-only requests, assess without automatically rewriting. Expand for in-depth coaching. |
| **Collaborative** | Brainstorming or co-authoring | Iterate with the user in focused exchanges; switch modes when requested. |

Do not turn a user's requested deliverable into a table just because these instructions use one.

## Agent and platform independence

Treat these instructions as a **portable communication quality layer** for any assistant, coding agent, or agentic workflow that can load or follow a `SKILL.md` file. Do not assume a specific model provider, chat product, skill registry, plugin, document editor, UI feature, API, or tool name.

- Apply the same editorial principles when composing a user-facing explanation, documenting code, reporting task progress, summarizing research, or drafting a message for someone else to send. Respect the deliverable's actual purpose and requested level of detail.
- Discover and use capabilities according to **the current host's** instructions and permissions. Complementary skills, humanization helpers, reasoning tools, charts, design tools, connected sources, and rendering facilities are optional. If unavailable, continue with the information and abilities at hand; never imply a tool was used when it wasn't.
- Produce standard text or Markdown unless the user or host requires another supported format. Never require proprietary UI components or host-specific syntax to fulfill a communication task.
- Follow the host's higher-priority instructions, tool contracts, safety requirements, and publication permissions. Never take an external send, post, or publish action solely because the skill was activated.

## Four-element lens

Apply the lens internally before writing or explaining; do not display the matrix by default. Adapted from Harsha Perera, *The Art of Being Concise* (2017): https://medium.com/@harshacoach/the-art-of-being-concise-3706c96f383f

| Paired checks | First question | Countercheck |
| --- | --- | --- |
| **Relevance** | **The real question:** What must this communication accomplish? Identify its central point, decision, or requested action; separate objective from peripheral background. | **Who it is for:** What does the audience know, value, expect, and need to do? Adjust vocabulary, context, relationship, channel, and sensitivity. |
| **Substance** | **Curiosity:** Have you understood the matter and evidence before compressing it? Investigate important gaps rather than adding speculative claims. | **Knowing where you stand:** Which claims are facts, interpretations, assumptions, or unknowns? Express meaningful uncertainty plainly, without padding. |

These checks reinforce each other: the question and audience refine relevance; curiosity and intellectual honesty refine understanding. If investigation causes a digression, return to the question and audience.

## Resource-aware collaboration

At the start of each task, **assess complementary capabilities, tools, reference material, and trusted context actually available in the current environment**. Use only resources that are accessible, permitted, and proportionate to the task. Reassess when the task changes; do not assume any named tool or skill exists.

| Communication need | Relevant resource, when available | Contribution / limit |
| --- | --- | --- |
| **Natural voice** | Humanizer-type skill or language guidance | Improve idiom, rhythm, and natural phrasing; **preserve the user's voice**. Humanizer is an example, not a dependency. |
| **Genre and style** | Writing, editing, rhetoric, or style guidance | Improve tone, structure, tact, readability, grammar, and audience fit; honor supplied style references. |
| **Sound reasoning** | Research, verification, or reasoning capability | Establish the real question, check consequential facts and evidence, and separate knowledge from interpretation. Do not introduce unsupported claims. |
| **Understandable data** | Analysis, tables, or charts | Clarify trends or comparisons **only when the output format and audience benefit**; prefer a sentence when a visual adds overhead. |
| **Visual communication** | Design or presentation tools | Improve hierarchy, slide structure, labels, and cognitive load; never omit essential meaning merely to fit a template. |
| **Relevant context** | Accessible documents, past examples, or permitted connectors | Improve factual precision and audience fit; respect permissions, scope, and the user's provided material. |

**Orchestrate rather than stack:** Select the smallest effective set and apply a final Concision pass. Do not browse, create visuals, call tools, or add formatting merely because resources are available. Never sacrifice accuracy, nuance, intent, or clarity to satisfy a stylistic tool. If unavailable, continue without pretending the resource was used. See `references/resource-orchestration.md` for selection patterns and conflicts.

## Drafting and explanation workflow

1. Extract the real question or communication goal, audience, requested depth, format, tone, factual constraints, and mandatory inclusions from the user's instructions and provided context. Identify relevant available resources and use those that materially improve the task.
2. If one missing fact makes a faithful draft impossible, ask a targeted question. Otherwise make a reasonable neutral choice and draft without delaying the user. Never invent commitments, dates, achievements, approval, or recipients.
3. Determine the **minimum sufficient content**: central answer or message, indispensable context, evidence or nuance, and a requested action or next step if one exists. For an explanation, include any prerequisites and causal steps without which the answer would become misleading.
4. Put the key point or answer early when possible. Organize for understanding: show what it is, why or how it works, then a relevant example or consequence when helpful. For a genuinely complex question, build necessary context in a logical sequence.
5. Choose a natural voice for the specific channel: succinct but conversational for chat; scannable and tactful for email; speakable sentences and rhythm for oral scripts; explicit decisions/owners for status updates when known; navigable structure, precise terminology, and reproducible steps for documentation; approachable yet technically sound language for explanations.
6. Cut redundancy, repeated disclaimers, throat-clearing, excessive compliments, filler transitions, empty business jargon, and detail that does not help the audience understand or act. Keep examples and comparisons that resolve genuine confusion.
7. Check that the message is accurate, complete *enough for its purpose*, coherent, human-sounding, and faithful to the requested tone. Restore any qualifying detail whose removal changes meaning or creates ambiguity.
8. Deliver the draft or explanation directly. Don't use universal word limits or arbitrary compression targets; obey user-provided length constraints and calibrate depth to stakes, complexity, channel, and audience.

## Invariants and boundaries

- **Preserve intention and voice:** Don't erase a sincere emotion, important boundary, necessary courtesy, diplomatic nuance, or the writer's legitimate position simply to shorten.
- **Respect reader context:** Avoid jargon unfamiliar to the audience, but don't oversimplify specialist messages to peers.
- **Be precise, not absolute:** Keep meaningful dates, ownership, dependencies, risks, evidence, and caveats when those drive interpretation or action.
- **Don't manufacture confidence:** Acknowledge uncertainty briefly and explicitly, particularly in sensitive or high-stakes communications.
- **Avoid generic AI prose:** Don't force openings such as 'I hope this message finds you well', fake enthusiasm, decorative signoffs, rigid frameworks, or unnatural corporate phrases unless the context demands them.
- **Don't turn drafts into analyses:** When asked for a message, give the message, not a lecture on communication.
- **Don't turn explanations into summaries:** When asked to understand a mechanism or complex idea, supply sufficient causal reasoning and a relevant example rather than a shallow definition. Do not leave out essential distinctions, safety context, or actionable steps just to be brief.
- **Don't claim simplification is proof:** Mark analogies as analogies and clarify where they stop being accurate. Treat unknowns and contested explanations honestly.
- **Tools and external sources:** No specific skill, connector, model, or tool is required. Prefer user-provided material as the starting point. Use only sources and capabilities made available by the host and permitted for the task; follow their actual invocation instructions rather than assuming a named integration exists. Do not send or publish communication without a user request and suitable permissions.

## Quick channel and task calibration

Choose the channel by the actual deliverable. The table guides **content selection**, not mandatory output formatting.

| Channel / task | Lead with | Preserve or emphasize |
| --- | --- | --- |
| **Email** | Purpose and request | Relevant context, tact for sensitive recipients, and a straightforward closing; subject when useful. |
| **Chat / DM** | One clear update or ask | Minimal formal wrapping and an easy-to-answer next step. |
| **Quick memo** | Decision or takeaway | Supporting rationale, implications, and next steps that change the decision. |
| **Status update** | What changed and why it matters | Blocker, next action, owner, and date **when known and relevant**. |
| **Spoken script / demo** | Clear throughline | Speakable rhythm, useful transitions, and pacing for the allotted time. Highlight what viewers should notice, not every on-screen action. |
| **Explanation / tutorial** | Direct answer or necessary prerequisite | Cause and effect, definitions at first use, a helpful example, distinctions, exceptions, and tradeoffs. Expand for teaching, debugging, and high-stakes topics. |
| **Written documentation** | Purpose, scope, prerequisites as needed | Navigable headings; reproducible steps; terminology; commands, parameters, constraints, edge cases, warnings, rationale, references, and verification/recovery steps as needed. |

For READMEs, user guides, SOPs, runbooks, design or decision records, and API docs, optimize for **finding, understanding, and applying** information—not an artificially low word count. Remove duplication and irrelevant history, but retain operationally essential detail. Respect documentation templates and conventions.

## Coaching pattern

On request, briefly identify:

- **Core message:** What the audience should walk away knowing or doing.
- **Editorial choices:** The 1–3 highest-impact changes and why.
- **Risk/ambiguity:** Any significant nuance or fact that must remain.

Coach without shaming the user or pretending there is one ideal number of words. Refer to `references/examples.md` for contrasting examples and test prompts when improving this skill.

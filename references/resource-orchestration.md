# Resource orchestration for Concision

This reference elaborates the resource-aware collaboration rule in `SKILL.md`. Treat each resource as optional, subject to host capability discovery and permissions; never presume a particular vendor, tool registry, or installation.

## Selection test

1. Define the communication's real purpose, intended audience, delivery medium, and nonnegotiable facts.
2. Identify the bottleneck: unnatural language, weak reasoning, poor structure, unsupported facts, confusing data, or visual overload.
3. Check which relevant skills, tools, source documents, style guides, and connectors are **actually accessible in this runtime**. Follow the host's discovery rules and read relevant instructions when possible. Don't invent capabilities, names, or paths.
4. Use a specialist only when it is likely to improve that bottleneck; don't delegate indiscriminately or create tool overhead for a simple draft.
5. After specialist work, apply the Concision review: essential facts intact, meaningful uncertainty intact, audience effort reduced, voice appropriate, required action easy to find.
6. Return the requested artifact; mention resource use only if requested or necessary for transparency.

## Typical compositions

| Task or bottleneck | Helpful resource types | Concision responsibility |
| --- | --- | --- |
| Short email sounds generated | Humanizer-type writing skill, user writing samples | Keep sincerity, purpose, precise ask, appropriate boundaries |
| Sensitive disagreement or stakeholder note | Tone/style skill, audience context, strategic reasoning | Retain the actual position and tact; don't erase substantive disagreement |
| Executive status update | Reasoning or summarization, verified project records | Lead with status/decision, exception, owner, impact, ask; don't invent facts |
| Product announcement with figures | Data validation, charts where actually warranted, editorial style | Expose the takeaway; choose simple visuals or plain text to minimize audience effort |
| Presentation script or slide content | Speechwriting, design/layout, slide skill | Ensure spoken rhythm, appropriate pacing, one point per section, adequate explanation |
| Decision memo | Research/verification, argument structure, document formatting | Preserve recommendation, support, alternatives, risks, and decision request |

## Conflict resolution

- Correct information beats persuasive wording. Uncertain facts stay uncertain.
- Purpose and audience determine whether a convention applies. A 'humanized' style must not make an update vague or a safety warning casual.
- A chart must earn its space; if it causes more work than a sentence, omit it.
- A template should adapt to sufficient content, not delete critical caveats to achieve visual symmetry.
- A second skill's verbosity should not leak into editor-mode output; coach-mode commentary remains by request.
- If specialist advice conflicts with higher-priority user instructions or required safeguards, follow the higher-priority instructions.

## Regression scenarios

1. **Humanizer unavailable:** Produce a natural 4-sentence email without claiming Humanizer was used.
2. **Humanizer available:** Use it appropriately, then verify names, dates, commitments, and original author voice remain intact.
3. **Numbers-heavy status:** Offer a table only when it improves the requested medium, not by default.
4. **Presentation request:** Use applicable design/presentation support while avoiding text-heavy slides and losing nuances.
5. **Simple Slack update:** Answer directly without gratuitous browsing, charts, or skill chaining.
6. **Conflicting style tools:** Choose the message that accurately and appropriately informs its audience, not the one with fewer tokens or more polished prose.

## Portability across hosts

- In a host with skill discovery: discover applicable helpers and use them only when their instructions and permissions allow.
- In a host without skill discovery: apply Concision independently; never fabricate another skill invocation.
- In a code-focused agent: keep technical specifics, verification steps, and evidence while improving explanations, update messages, code documentation, and summaries.
- In a text-only host: use prose, lists, Markdown, or plain-text examples; do not depend on rich UI components or interactive cards.
- In a host with charts or presentation tooling: use them only if suitable for the requested deliverable and if actually supported.

Do not add platform adapter instructions to the editorial workflow; an integration-specific metadata file may be present, but the behavior is defined entirely by `SKILL.md` and its shared references.

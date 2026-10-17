# Prompt Architecture

Concorda uses modular prompts so product doctrine, safety routing, memory policy, and report generation stay auditable.

## Layers
- **System prompt layer:** permanent constitution.
- **Developer prompt layer:** current task instructions.
- **Database prompt templates:** reusable doctrine modules.
- **Orchestration layer:** routing engine.
- **Memory layer:** approved context only.
- **Output schema layer:** required structured JSON contracts.
- **User prompt:** live transcript and request.

## Runtime sequence
1. Receive transcript.
2. Run safety screen.
3. If unsafe, route to safety mode.
4. If safe, classify conflict.
5. Select modules.
6. Pull approved memory.
7. Compile prompt.
8. Generate structured JSON.
9. Render private report.
10. Suggest memory updates.
11. Save memory only after consent.

## Compiled prompt flow
The orchestration layer combines the system constitution, task-specific developer instructions, selected prompt modules, approved memory context, the live user request, and the target output schema. The compiled prompt must not include private coaching for another participant or unapproved memory.

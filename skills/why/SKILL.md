---
name: why
description: "Investigate the history and rationale behind code, with cited facts and explicit uncertainty."
disable-model-invocation: true
---

# Why

Answer why the specified code or design took its current shape. Requires source
access; history, review records, and connected services improve available evidence.
This is an investigation, not an implementation request.

1. **Anchor the question.** Identify the relevant files, symbols, and decision.
   State an interpretation if the target is ambiguous. Read enough code to separate
   the behavior from the motivation the user is asking about.
2. **Trace lineage.** Inspect blame and patch history through renames, including the
   introduction of the behavior rather than only its latest edit. Read relevant
   commits and available PR discussions. Follow actual linked tickets or documents;
   missing history or host access is a coverage gap, not an empty search result.
3. **Expand where evidence points.** Use available issue trackers, design documents,
   team discussions, incident records, observability, or analytics when relevant to
   the unresolved question. Defensive code often warrants incident history. Record
   sources searched, useful queries, empty results, and unavailable relevant sources.
   Stop when the bounded question is answered or remaining gaps are clear. A small
   question with a direct contemporary answer does not require a broad source sweep.
4. **Weigh the record.** Distinguish explicit contemporary rationale, conclusions
   supported by several indirect sources, plausible hypotheses, and unknowns.
   Code demonstrates behavior, not author intent. Treat the user's proposed reason
   as a hypothesis. Surface contradictory records and distinguish an original
   motivation from later changes; a current benefit need not be the historical reason.
5. **Explain the answer.** Lead with the strongest supported conclusion. Cite each
   material claim to a real source or revision and preserve uncertainty in the
   wording. Include relevant alternatives, the search coverage, and remaining gaps.
   When preparing for a change, derive concrete constraints: preserve, change,
   avoid, and unresolved risk. Keep recommendations distinct from historical facts.

Work directly for narrow questions. Independent source investigators are optional
when available and authorized; their summaries still require citation checks.

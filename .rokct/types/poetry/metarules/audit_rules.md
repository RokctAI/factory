# Audit Rules

After generation every element is audited backwards. The audit is not a reading. It is a structural test. The question at every level is the same: does this belong here and does it earn its place?

## The Backward Audit Chain

Line -> Stanza -> Poem -> Book -> World

For every line ask: does this line serve the stanza's purpose?
For every stanza ask: does this stanza serve the poem's purpose?
For every poem ask: does this poem serve the book's rules?
For every book ask: does this book honor the world rules?

If anything fails at any level it is flagged and rewritten specifically at that level only. The rewrite does not touch what is not broken.

## Audit Rules

1. The audit runs bottom-up after all content is generated. Never during generation.
2. The agent that generated the content does not run the audit. Different agent always.
3. A failed line triggers a line rewrite only. Not a stanza rewrite.
4. A failed stanza triggers a stanza rewrite only. Not a poem rewrite.
5. A failed poem triggers a poem rewrite only. Not a book rewrite.
6. The audit does not rewrite for style. It rewrites for structural failure only.
7. A line that hits but does not belong to its stanza has failed the audit even if it scores 10/10 on impact metrics.
8. The audit records every flag and every rewrite in a separate audit log inside the book folder.
9. Maximum three rewrite attempts per element. If an element fails three audits it is flagged for human review.
10. The audit chain runs once per generation session. Not per line. Not continuously.

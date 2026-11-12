# Checkout delivery

This repository demonstrates a small team's normal GitHub change workflow.
The application calculates a delivery fee: orders of at least $50 ship free;
smaller orders cost $5. Amounts are integer cents.

## Run the application tests

```bash
python3 -m unittest -v
```

No packages, credentials or services are needed to run the tests locally.
GitHub Actions runs the same tests for pull requests and pushes to `main`.

## How changes reach main

1. Make a change on your own branch and open a pull request.
2. Read the required **Checkout tests** result.
3. If a test fails, open the failed step, understand the expected behavior and
   correct the application without weakening its tests.
4. Wait for the check on the new commit before deciding whether to merge.

The active `main` ruleset requires a pull request and the **Checkout tests**
check, with no bypass actors. It deliberately requires no review approvals,
so one presenter can complete the demonstration.

`.github/CODEOWNERS` names the responsible maintainer. Naming an owner is not
the same as requiring their approval. The author cannot approve their own PR;
this solo demo does not promise a self-review notification or enforced owner
approval.

## Demo navigation

- **Pull requests:** start with the open `[Live demo]` pull request.
- **Files changed:** identify the delivery threshold and the responsible owner.
- **Checks:** inspect the failing boundary test, then make the one-line fix.
- **Conversation:** inspect the merge requirements before and after the fix.
- **Rules:** inspect `Checkout safety` for `main` if you want to explain the gate.

Rehearsal pull requests are labeled in their titles. A successful rehearsal
belongs to its recorded commit; it is not evidence that a different PR passed.
This is a real hosted GitHub workflow, not a local model of branch protection.

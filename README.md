# Checkout delivery

This repository demonstrates a small team's normal GitHub change workflow.
The application calculates a delivery fee: orders of at least $50 ship free;
smaller orders cost $5. Amounts are integer cents.

## Run the application tests

```bash
python3 -m unittest -v
```

No packages, credentials or services are needed to run the tests locally.
When enabled, GitHub Actions runs the same tests for pull requests and pushes
to `main`. Local tests prove application behavior, not GitHub merge enforcement.

## Work in your own fork

Start with [Fork practice](docs/fork-practice.md). It covers choosing your own
account, enabling Actions, selecting branches and keeping the pull request
inside your fork. A new fork has code, not the upstream pull requests, run
history or branch rules. Copying only `main` gives you the passing application;
copy all branches only if you also want the broken demo starting point.

You can inspect public evidence and run tests without write access. The
optional writable lab changes the delivery policy to $60 in your own authorized
disposable fork; it does not require a reviewer or a new merge rule.
To repeat the merge-gate demonstration too, the guide has a separate optional
owner-only pre-class setup. It is not part of the 35-minute core lab.

## How changes reach main

1. Make a change on your own branch and open a pull request.
2. Read the **Checkout tests** result for that pull request and revision.
3. If a test fails, open the failed step, understand the expected behavior and
   correct the application without weakening its tests.
4. Wait for the check on the new commit before deciding whether to merge.

In the original `msfttoler/wre-week-02` repository, the `Checkout safety`
ruleset for `main` requires a pull request and the **Checkout tests** check,
with no bypass actors or required review approvals. This is upstream
configuration, not a setting installed by cloning or forking. Inspect the
actual target repository's Rules and merge box before calling a check required.
The core lab does not ask you to create or change rules.

`.github/CODEOWNERS` names the upstream maintainer, `@msfttoler`. That entry is
copied as text, not reassigned to the fork owner. See the fork guide before
interpreting it in your fork. Naming an owner is not the same as requiring
their approval. The author cannot approve their own PR; this solo demo does
not promise a self-review notification or enforced owner approval.

## Demo navigation

- **Pull requests:** in the original repository, start with the open
  `[Live demo]` pull request. It will not appear as a PR in a fresh fork.
- **Files changed:** identify the delivery threshold and the responsible owner.
- **Checks:** inspect the failing boundary test, then make the one-line fix.
- **Conversation:** inspect the merge requirements before and after the fix.
- **Rules:** inspect `Checkout safety` for `main` if you want to explain the gate.

Rehearsal pull requests are labeled in their titles. A successful rehearsal
belongs to its recorded commit; it is not evidence that a different PR passed.
This is a real hosted GitHub workflow, not a local model of branch protection.

## Reuse boundary

No license file is currently included. Public visibility permits viewing and
forking on GitHub, but is not a general open-source license. Ask the rights
holder to choose and publish a license before broader reuse or redistribution.

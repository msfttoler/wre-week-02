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

- **Pull requests:** in the original repository, start with
  [Live demo PR #2](https://github.com/msfttoler/wre-week-02/pull/2).
  It will not appear as a PR in a fresh fork.
- **Files changed:** identify the delivery threshold and the responsible owner.
- **Checks:** inspect the failing boundary test, then make the one-line fix.
- **Conversation:** inspect the merge requirements before and after the fix.
- **Rules:** inspect `Checkout safety` for `main` if you want to explain the gate.

Rehearsal pull requests are labeled in their titles. A successful rehearsal
belongs to its recorded commit; it is not evidence that a different PR passed.
This is a real hosted GitHub workflow, not a local model of branch protection.

## Presenter quick start

Allow about 8 minutes for the demonstration, plus time for Actions to finish.
Use `msfttoler` on GitHub.com for the edit and merge; a read-only account can
inspect everything but cannot complete the repair. Confirm the avatar/account
before presenting. The CLI account is separate from the browser account.

1. Open [the live PR's changed file](https://github.com/msfttoler/wre-week-02/pull/2/files).
   Ask: "What should delivery cost for a $49 order?" Compare the stated $50
   policy with the proposed `4000`-cent threshold.
2. Open [the live PR's checks](https://github.com/msfttoler/wre-week-02/pull/2/checks).
   Expand **Checkout tests > Run checkout tests**. The $49 test reports
   `AssertionError: 0 != 500`: the app charges nothing instead of $5.
   Read the failure aloud rather than relying on its color.
3. Return to **Conversation** and show that the required check blocks merging.
   [Checkout safety](https://github.com/msfttoler/wre-week-02/rules/27157755)
   requires a PR and the check, not a second reviewer or owner approval.
4. In **Files changed**, use the file menu to edit `shipping.py` on
   `demo/free-shipping`. Change only `>= 4000` to `>= 5000`; keep the useful
   policy docstring and all tests. Commit to that existing demo branch, not
   `main`. Ask which test should change from failing to passing.
5. Wait for **Checkout tests** on the PR's new head to pass. Revisit the merge
   box and distinguish "checks passed" from "review approved". Merge only if
   you want to finish the demonstration; merging consumes this prepared PR.

Keep [rehearsal PR #1](https://github.com/msfttoler/wre-week-02/pull/1) as the
separate corrected example, not as evidence for PR #2. If Actions or the
network is unavailable, inspect its recorded repair and results and explicitly
describe them as prior evidence, not a new live run. Do not disable the rule.
If the live branch is behind `main`, update that branch and wait for its check
before presenting. Do not reset or force-push shared branches to repeat a demo.

For learner practice, return to [Fork practice](docs/fork-practice.md); leave
the upstream live PR for the presenter. Use browser zoom as needed, narrate
file changes and status text, and enable the meeting's live captions.

## Reuse boundary

No license file is currently included. Public visibility permits viewing and
forking on GitHub, but is not a general open-source license. Ask the rights
holder to choose and publish a license before broader reuse or redistribution.

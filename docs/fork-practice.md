# Practice in your own repository

The checkout team needs to catch a delivery-fee regression before accepting a
change. You will trace a failing test to the proposed code, then distinguish
application evidence from a GitHub merge requirement. The independent lab
changes the business policy instead of repeating the repair.

## Choose the route and target

- **Read-only:** inspect the original repository's PRs, files, checks and Rules,
  and run the application locally. Do not edit or open a PR upstream. Record
  what you would change and what hosted effect you cannot verify.
- **Optional writable practice:** use a personal, public, disposable fork that
  you are authorized to change. You need Git, Python 3, a GitHub account and
  permission to push your branch. GitHub CLI is for inspecting evidence.
  Do not request organization administration, add a reviewer or buy a service.

Local tests need no packages, secrets, credentials or cloud services. This
workflow uses a standard `ubuntu-latest` runner, which is free for public
repositories under current GitHub billing guidance. Do not use larger runners,
Codespaces, paid tools or private-repository provisioning for this exercise.
Account restrictions or an Actions policy can still block hosted work.

## Create and inspect the fork (writable route only)

These are instructions for a later authorized exercise, not evidence that a
fork or workflow has already been created.

1. On the original repository's GitHub.com page, choose **Fork**. In **Owner**,
   choose your own personal account, not the original owner or a work
   organization. If that account is unavailable or already has a fork, inspect
   the existing fork and preserve its work; do not delete it to start over.
2. Keep the fork public. Record the owner and repository name actually chosen.
   Keep **Copy the main branch only** selected for the independent lab. Uncheck
   it if you also want `demo/free-shipping` for the broken-demo investigation.
   Confirm the selection before **Create fork**.
3. In your fork, verify that the default branch is `main`. Under **Actions**,
   review the workflow and enable workflows when prompted. Fork workflows do
   not run by default. If **Checkout** is separately disabled, select it and
   **Enable workflow**. If policy or access prevents this, hosted work is
   blocked; continue with local tests or the read-only route, not a workaround.
4. Open `.github/workflows/checks.yml`: it runs ordinary unittest, reads
   repository contents and does not need secrets or writable workflow tokens.
   Enabling Actions does not create a check run or install a merge rule.
5. Inspect **Rules** in the fork. Upstream PRs, run history, branch protections
   and branch/tag rulesets are not installed by forking. Organization policies
   can govern an organization-owned fork; push rulesets are a separate
   fork-network exception, not the upstream `Checkout safety` branch ruleset.
   A visible failed check alone does not mean merging is blocked.

The branch picker in **Code** selects files, not a PR or a run. With a main-only
fork, `demo/free-shipping` and `rehearsal/free-shipping` will be absent. That is
expected. Use `main` for the lab. If you specifically need the demo branch,
GitHub's **Branches** page can copy an additional upstream branch into your
fork after you confirm authorization. Do not substitute the corrected
rehearsal branch for the deliberately broken demo.

## Optional owner-only pre-class setup: repeat the merge gate

Skip this section for the 35-minute core lab. It is a separate administrative
setup, only for the owner of a personal PUBLIC disposable fork who explicitly
authorizes changing that fork's branch rules. Branch rulesets are available
for public repositories on GitHub Free, including personal public forks.
This does not require an organization, paid plan or access to the original
repository's settings. Owning a fork is not, by itself, authorization to change
it. Do not perform these steps on upstream, shared or production repositories.

The purpose is to make the failing check a merge requirement, not merely a
visible result. These are authored native steps, not recorded execution.

1. Complete fork creation and Actions enablement above. For the demo, copy all
   branches and verify the fork's default is still `main`. Before configuring
   a check requirement, let a real CI run in THIS fork populate its selector.
   One route is **Pull requests > New pull request**: select your fork for BOTH
   repositories, base `main`, compare `rehearsal/free-shipping`. Review the
   nonempty policy-description diff and create a pre-class rehearsal PR.
   Wait for **Checks > Checkout tests** to actually succeed; record its head
   and run ID. Do not merge this PR. Its result seeds check selection, not
   evidence that the later broken demo passes. GitHub requires a recent
   successful check in the selected repository; use one from the last seven
   days, not an upstream run or an invented check name.
2. In your fork, click **Settings > Rules > Rulesets** in the sidebar, then
   **New ruleset > New branch ruleset**. Some current sidebar layouts group
   the ruleset entry under **Rulesets** instead of **Rules**; open that native
   **Rulesets** entry. If the controls or access are absent, this optional
   setup is blocked. Do not buy a plan, expand access or use a browser workaround.
3. Enter `Checkout safety practice` as **Ruleset name**. Set **Enforcement
   status** to **Active**. Leave **Bypass list** empty: do not add repository
   administrators, an app, a team or yourself.
4. Under **Target branches**, click **Add a target > Include default branch**.
   Confirm it resolves to `main`. Do not target all branches or change the
   default branch to make the selection work.
5. Select **Require a pull request before merging**. Set **Required approvals**
   to **0**. Leave **Require review from Code Owners** and **Require approval
   of the most recent reviewable push** off; add no required reviewers.
6. Select **Require status checks to pass**. Open **Add checks**, search for
   `Checkout tests`, select the check actually produced by your fork's CI, and
   confirm the addition using the dialog's add control. The required context
   must be `Checkout tests`, not workflow name `Checkout` or job ID
   `checkout-tests`. Select **GitHub Actions** as the expected source when
   offered. If the check/source cannot be selected, stop: inspect the fork's
   successful run, event and check name, then return to this form. Do not
   type a guessed requirement or create a synthetic status.
7. Check **Require branches to be up to date before merging**. This is the
   strict setting. Leave any option to skip required checks on branch creation
   off. Keep the existing deletion/force-push safeguards; do not add unrelated
   scan, deployment, merge-queue or review requirements.
8. Recheck target `main`, Active, empty bypass list, PR required, zero approvals,
   no owner review, and strict `Checkout tests`; click **Create**. This click
   applies a real control immediately. Reopen the ruleset and verify its saved
   settings. Other active rules can add requirements; inspect them rather than
   disabling them to force this scenario.

Now use the broken-demo branch below and open its PR inside the fork BEFORE
repairing it. Expected, not yet observed here: the current $49 check fails and
the PR merge box shows that required check blocking merge. Do not merge a known
bad change or attempt a direct push to `main`. After the application repair,
wait for that PR's new current-head check and inspect the merge requirements
again. A green rehearsal from step 1 is not the repaired demo's result.

If strict checks report the branch is behind `main`, inspect the commits and
update only your own practice branch from `main`, rerun the unchanged suite,
and inspect the resulting new hosted run. Do not disable strict checking.
If the saved rule, check, permissions or merge-box evidence cannot be verified,
record the gate demonstration as blocked/unreviewed, not passed.

For later inspection from the selected local clone, use the actual fork name:

```bash
REPO=YOUR-LOGIN/YOUR-FORK
gh api "repos/$REPO/rules/branches/main"
gh api "repos/$REPO/rulesets"
```

Select the actual ruleset ID from that list, then inspect its detail with
`gh api "repos/$REPO/rulesets/YOUR-RULESET-ID"`. These are reads, not setup.
Record UTC, fork, head, run and saved ruleset ID/settings. Keep failed-check
merge-box evidence separate from an actual rejected hosted mutation.
After class, do not disable the gate to bypass a failure. Any removal of only
this owner-created practice ruleset needs separate owner authorization; preserve
other rules and resources.

## Clone the selected repository

In your terminal, move to the parent directory where you keep practice
repositories. Replace `YOUR-LOGIN/YOUR-FORK` with your fork's actual full name.
Replace `YOUR-PRACTICE-DIRECTORY` with a new, unused local directory name.
For read-only work, use the original repository URL instead and never push.

```bash
git clone https://github.com/YOUR-LOGIN/YOUR-FORK.git YOUR-PRACTICE-DIRECTORY
cd YOUR-PRACTICE-DIRECTORY
git remote -v
git status --short
git switch main
git rev-parse HEAD
python3 -m unittest -v
```

Confirm `origin` names your fork before any writable step. A passing baseline
has four tests. If Python 3 or Git is missing, install it through your approved
software process; no repository setup script is needed. Stop on unexpected
local changes rather than overwriting them.

For the optional broken-demo investigation, start with a clean working tree:

```bash
git fetch origin
git switch --create practice/delivery-repair origin/demo/free-shipping
python3 -m unittest -v
```

This local branch starts from the deliberately broken proposal, not `main`.
If the branch already exists, inspect it rather than recreating it. A missing
remote branch means it was not copied; return to branch selection above.
Expected: the $49 test fails because the app gives free delivery too early.
To repeat the hosted demo, BEFORE repairing it, publish this starting branch
only when authorized: `git push --set-upstream origin practice/delivery-repair`.
Open its PR using the repository/branch selectors below, with compare branch
`practice/delivery-repair`. Inspect the current failing run and, if the owner
completed the optional setup, the merge gate. Do not claim a required check
when no rule was installed.

Read `shipping.py` and `test_shipping.py`, repair the app's decision without
weakening the $50 policy tests, and rerun the same command.

For that authorized hosted demo PR, review and publish only the repair:

```bash
git --no-pager diff -- shipping.py
git add shipping.py
git commit -m "Repair the checkout delivery regression"
git push origin practice/delivery-repair
```

Then inspect the new run on that same PR, not the pre-class rehearsal.

Do not replace the entire file from `main` blindly: compare the proposed change
with `main` and retain only intentional differences. If a repair leaves no
diff, there is nothing to propose in a PR. Record the local repair; use the
independent policy lab below for a meaningful new functional change. Do not
add unrelated edits merely to make a PR possible.

## Independent lab: the policy changes to $60

Start independently from your fork's passing `main`, not a previous exercise
or another learner's branch. The new policy is: orders below $60 cost $5 to
deliver; orders of $60 or more ship free. Negative subtotals must still be
rejected. Amounts remain integer cents.

```bash
git status --short
git fetch origin
git switch --create lab/delivery-policy origin/main
```

Stop if you have uncommitted work or that branch name already exists; preserve
it and choose a new unused branch name. This branch command selects a starting
revision. It does not change application behavior or GitHub settings.

1. Identify which old expectations now conflict with the new policy and why.
2. Revise the application, its policy description and tests. Include cases that
   distinguish the old policy from the new one, both sides of the boundary and
   a rejected input. Do not delete checks merely to obtain a green result.
3. Run `python3 -m unittest -v`. Read each test result, not only the summary.
4. Review the diff and explain why it represents a policy change rather than
   a regression repair.

Progressive hints (use only when needed):

- First, identify the units of the input and the result.
- Next, choose a subtotal whose fee differs between the two policies.
- Finally, inspect the comparison and its equality case; check that invalid
  input is handled before the free-delivery decision.

There is no prepared solution script. If you cannot push, submit a precise
change proposal and local evidence; do not claim a hosted check or merge.

## Open the PR inside your fork

Only with authorization for your own disposable fork, review and publish the
lab's intentional files. From the same practice directory:

```bash
git --no-pager diff -- shipping.py test_shipping.py README.md
git add shipping.py test_shipping.py README.md
git commit -m "Update the checkout delivery policy"
git push --set-upstream origin lab/delivery-policy
```

These commands publish only to the `origin` you verified. If you chose a
different branch name, use that name in the push command. No push is needed
for the read-only route.

On GitHub.com, open your fork's **Pull requests > New pull request** and use
**compare across forks** if needed to expose repository selection. Fork
contribution shortcuts may target upstream. Before creating the PR, verify:

- **base repository:** your fork, NOT `msfttoler/wre-week-02`;
- **base branch:** `main`;
- **head repository:** the same fork;
- **compare branch:** `lab/delivery-policy` (or your chosen practice branch).

Review **Files changed** for a real, intended diff. If GitHub says there is
nothing to compare, check both branch selectors and the actual diff; do not
open an empty PR. Fill in the template's current baseline and proposed policy.
The copied `@msfttoler` entries in `.github/CODEOWNERS` are not your fork's
maintainers and may be invalid there without explicit write access. Do not
invite the upstream owner. If ownership metadata is part of your practice,
adapt it to a valid writer on your own fork's base branch through a separately
authorized change. This lab neither needs owner approval nor proves it.

## Read current evidence, recover and clean up

In the PR UI, read **Checks**, the failed step if any, and the merge box.
In the same local directory, select your repository and the actual PR number:

```bash
REPO=YOUR-LOGIN/YOUR-FORK
PR=YOUR-PR-NUMBER
gh pr view "$PR" --repo "$REPO" --json number,baseRefName,headRefName,headRefOid,url
gh pr checks "$PR" --repo "$REPO"
gh run list --repo "$REPO" --branch lab/delivery-policy --event pull_request
```

These variables only select read targets. From that list, choose the actual
run ID associated with the PR's current head and inspect its immutable record:

```bash
RUN=YOUR-RUN-ID
gh run view "$RUN" --repo "$REPO" --json databaseId,event,headSha,headBranch,status,conclusion,jobs,url
gh run view "$RUN" --repo "$REPO" --log
```

A prior green rehearsal, a pending run or no run is not a current pass.
`pull_request` normally checks out GitHub's test merge commit, so its checkout
SHA can legitimately differ from the PR head. Inspect the checkout log's merge
parents/head association before deciding the run is stale.

- **Test failure:** read expected versus actual fee and the selected policy;
  repair only your branch, rerun locally, and wait for the new hosted run after
  an authorized push. Do not weaken negative-input checks.
- **No run:** inspect Actions enablement, event, selected repository, PR/base
  and head revision. A push to a non-`main` branch alone is not a push trigger
  in this workflow; opening/updating its PR is. Enabling workflows does not
  retroactively prove the earlier commit ran.
- **Blocked run or permission denial:** record the actual message and stop
  hosted effects. Do not expand tokens, switch accounts or change policy.
- **Wrong PR base:** stop before creation and reselect your fork. If already
  created upstream by mistake, tell the facilitator; do not send more commits
  or assume changing the base branch moves the PR to another repository.

Record UTC time, repository, PR, head revision, run ID, event, result and limits.
There is no requirement to merge. Local test success proves only tested app
behavior; even a successful hosted check does not prove a merge gate rejected
a bad change. Keep read-only inspection distinct from executed enforcement.

For cleanup, close only your disposable practice PR and delete only your own
practice branch when authorized and no longer needed. Preserve other work;
do not reset `main`, remove another learner's fork or delete an existing fork.
At work, confirm the real policy owner, required checks and rules on the actual
target before accepting a similar change.

## Official references

- [Fork a repository](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)
- [Workflow events and fork enablement](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [Pull request repository and branch selection](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork)
- [Rulesets and fork inheritance](https://docs.github.com/en/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization)
- [Create a repository branch ruleset](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [PR and strict-check rule settings](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [Required check freshness and current-revision troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)
- [CODEOWNERS and forks](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)

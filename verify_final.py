#!/usr/bin/env python3
"""Verify the public documentation, branch namespace, and commit identity."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPOSITORY = "MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd"
CANONICAL = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
EXPECTED_BRANCHES = {
    "main",
    "audit/claim-1-centering-control",
    "audit/claim-1-durable-evidence",
    "audit/claim-1-paper-scale-idd",
    "audit/claim-4-diamond-morphology",
    "audit/claim-4-figure-falsification",
    "audit/claim-4-legacy-hosts",
    "audit/claim-4-marker-checker",
    "audit/claim-4-official-file-get",
    "audit/claim-4-primary-flowrepository",
    "audit/claim-4-stateful-api",
    "audit/claim-5-author-cleaning",
    "audit/claim-5-cnf-sinkhorn",
    "audit/claim-5-comments-dataset",
    "audit/claim-5-minimum-20",
    "audit/claim-5-minimum-30",
    "audit/claim-5-official-schema",
    "audit/claim-5-sbert-pca20",
    "audit/claim-5-split-semantics",
    "audit/frozen-baseline",
    "integration/hub-metadata-publication-repair",
    "release/cumulative-candidate",
    "release/evaluator-blind-red-team",
    "release/final-publication-candidate",
}
REQUIRED_FILES = {
    "README.md",
    "branch-audit.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "ENVIRONMENT.md",
    "REPORT.md",
    "CITATION.cff",
    "AUTHOR_THANK_YOU.md",
    "STATUS.md",
    "claims.json",
    "reproduction_verdicts.json",
    "AUTONOMOUS_STATE.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
}
OVERALL_STATUS = (
    "MIXED_C1_SCOPED_VERIFIED_C2_LITERAL_FALSIFIED_C3_SOURCE_TABLE_FALSIFIED_"
    "C4_LITERAL_SOURCE_SCOPE_FALSIFIED_C5_BLOCKED_C6_SCOPED_VERIFIED"
)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def main() -> None:
    missing = sorted(path for path in REQUIRED_FILES if not (ROOT / path).exists())
    assert not missing, f"missing required files: {missing}"
    assert not git("status", "--porcelain"), "working tree is not clean"
    assert not git("for-each-ref", "--format=%(refname)", "refs/original"), "refs/original remains"

    remote = git("remote", "get-url", "origin").removesuffix(".git")
    assert remote.endswith(REPOSITORY), remote

    branch_lines = git("ls-remote", "--heads", "origin").splitlines()
    remote_branches = {
        line.split("\t", 1)[1].removeprefix("refs/heads/")
        for line in branch_lines
        if "\t" in line
    }
    assert remote_branches == EXPECTED_BRANCHES, remote_branches

    default_head = git("symbolic-ref", "--short", "refs/remotes/origin/HEAD")
    assert default_head == "origin/main", default_head

    identities = set(git("log", "--all", "--format=%an <%ae> | %cn <%ce>").splitlines())
    assert identities == {f"{CANONICAL} | {CANONICAL}"}, identities
    assert "Co-authored-by:" not in git("log", "--all", "--format=%B"), "co-author trailer found"

    claims = json.loads((ROOT / "claims.json").read_text())
    assert claims["overall_status"] == OVERALL_STATUS
    assert [claim["id"] for claim in claims["claims"]] == ["C1", "C2", "C3", "C4", "C5", "C6"]
    state = json.loads((ROOT / "AUTONOMOUS_STATE.json").read_text())
    assert state["overall_status"] == OVERALL_STATUS
    assert state["current_score_claim"] is False
    assert state["publication_allowed"] is False

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(remote_branches)} commits={git('rev-list', '--all', '--count')} "
        "claims=C1_scoped_verified,C2_literal_falsified,C3_source_table_falsified,"
        "C4_literal_source_scope_falsified,C5_blocked,C6_scoped_verified "
        "historical_score=7/12 current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()

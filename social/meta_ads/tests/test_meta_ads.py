import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import campaign  # noqa: E402
import optimise  # noqa: E402

JOB = json.loads((HERE / "examples" / "juvo_merchant_promo.json").read_text())


def test_plan_steps_and_everything_paused():
    plan = campaign.build_plan(JOB)
    assert [p["step"] for p in plan] == ["upload_media", "campaign", "adset", "creative", "ad"]
    for p in plan:
        if p["step"] in ("campaign", "adset", "ad"):
            assert p["body"]["status"] == "PAUSED"


def test_sales_needs_pixel_placeholder():
    plan = campaign.build_plan({**JOB, "objective": "sales"})
    adset = next(p for p in plan if p["step"] == "adset")
    assert adset["body"]["promoted_object"]["pixel_id"] == "<PIXEL_ID>"


@pytest.mark.parametrize("bad", [{"link": "http://x"}, {"daily_budget_minor": 0},
                                 {"objective": "fame"}, {"cta": "BUY"}, {"image": None}])
def test_validation_rejects(bad):
    with pytest.raises(campaign.JobError):
        campaign.build_plan({**JOB, **bad})


def test_module_has_no_network_code():
    src = (HERE / "campaign.py").read_text() + (HERE / "optimise.py").read_text()
    for mod in ("import requests", "import urllib", "import http", "import socket"):
        assert mod not in src


def test_cli_writes_plan(tmp_path):
    job = tmp_path / "j.json"
    job.write_text(json.dumps(JOB))
    assert campaign.main([str(job), "--out", str(tmp_path)]) == 0
    assert json.loads((tmp_path / JOB["id"] / "plan.json").read_text())["dry_run"] is True


def test_optimiser_decisions():
    rows = json.loads((HERE / "examples" / "sample_insights.json").read_text())
    got = {d["ad_id"]: d["action"] for d in (optimise.decide(r, 100) for r in rows)}
    assert got == {"A1": "keep", "A2": "scale", "A3": "pause"}

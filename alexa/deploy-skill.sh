#!/usr/bin/env bash
# Uploads the models of model/*.json to the skill and waits until Amazon has built them.
# Usage: SKILL_ID=amzn1.ask.skill... scripts/deploy-skill.sh
set -euo pipefail
cd "$(dirname "$0")"
f='experimental|trace-warnings|ES Module'
: "${SKILL_ID:?set SKILL_ID}"
until [ "$(ask smapi get-skill-status -s "$SKILL_ID" --resource manifest 2>&1 | grep -vE "$f" | python3 -c "import sys,json;print(json.load(sys.stdin)['manifest']['lastUpdateRequest']['status'])" 2>/dev/null)" = SUCCEEDED ]; do sleep 3; done
for loc in de-DE en-US; do
  ask smapi set-interaction-model -s "$SKILL_ID" -g development -l "$loc" --interaction-model "file:$loc.json" 2>&1 | grep -vE "$f" | grep -i error || true
done
for loc in de-DE en-US; do
  while :; do
    st=$(ask smapi get-skill-status -s "$SKILL_ID" --resource interactionModel 2>&1 | grep -vE "$f" | python3 -c "import sys,json;print(json.load(sys.stdin)['interactionModel']['$loc']['lastUpdateRequest']['status'])" 2>/dev/null || echo WAIT)
    [ "$st" = SUCCEEDED ] && { echo "$loc model built"; break; }
    [ "$st" = FAILED ] && { echo "$loc model FAILED:"; ask smapi get-skill-status -s "$SKILL_ID" --resource interactionModel 2>&1 | grep -vE "$f" | python3 -c "import sys,json;print(json.dumps(json.load(sys.stdin)['interactionModel']['$loc']['lastUpdateRequest'].get('errors'),indent=1,ensure_ascii=False))"; exit 1; }
    sleep 5
  done
done
ask smapi set-skill-enablement -s "$SKILL_ID" -g development 2>&1 | grep -vE "$f" | tail -1

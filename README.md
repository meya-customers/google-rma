# google-rma

![Meya build](https://github.com/meya-customers/google-rma/workflows/Meya%20build/badge.svg)

An example product troubleshooting bot, with human escalation (RMA use-case) and embed mode.

Try it live: https://demo.meya.ai/google-rma-af34d9/

## Setup

```shell script
brew install python@3 libgit2
MEYA_AUTH_TOKEN=your_meya_auth_token
MEYA_APP_ID=app-your_app_id
git clone https://github.com/meya-customers/google-rma.git google-rma
cd google-rma
# you can optionally setup a venv instead as well
python3 -m venv venv  # optional
. venv/bin/activate  # optional
pip3 install --upgrade \
    --extra-index-url https://meya:$MEYA_AUTH_TOKEN@grid.meya.ai/registry/pypi \
    "pygit2==1.1.1" \
    "meya-sdk>=2.0.0" \
    "meya-cli>=2.0.0"
# auth (if needed)
meya auth add --auth-token $MEYA_AUTH_TOKEN
# connect to existing app
meya connect --app-id $MEYA_APP_ID
yarn install
```

## Workflow
```shell script 
meya check
meya format
meya test --watch
# to download secrets
meya vault download --file vault.secret.yaml
# if new secrets (after changing the yaml file)
meya vault upload --file vault.secret.yaml
meya push --watch
# for a full rebuild (useful for production deployments)
meya push --force --build-image
yarn deploy
```

## GitHub Actions
See `.github/workflows/meya.check-test.yaml`

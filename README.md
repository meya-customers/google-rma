# google-rma

Try it live: https://demo.meya.ai/google-rma-af34d9/

See `meya.yaml` for production `app_id`


## Getting started w/ a dev app

To deploy a dev app and get started with rapid development.

```bash
rm -rf .meya  # if it exists
rm meya.local.yaml  # if it exists (or simply delete the app_id)
# if you need to update the meya-sdk
pip install --extra-index-url https://meya:YOUR_MEYA_TOKEN@registry.meya.ai/pypi -r requirements.txt
meya secrets
meya watch
meya simulate
meya test [--no-watch]
meya format  # do this before committing code
meya check
```

To close gaps in DX, you'll need a few `eshr` commands:

```bash
cd YOUR_GRID_FOLDER
eshr contexts  # to copy/paste production instance string
eshr dashboard --kubectl-context YOUR_PRODUCTION_INSTANCE
eshr logs YOUR_APP_ID  # found in meya.local.yaml   
```


## Removing dev app after use

1. Manually delete deployment from k8s dashboard [[link](http://localhost:8001/api/v1/namespaces/kube-system/services/http:local-kubernetes-dashboard:http/proxy/#!/deployment?namespace=default)]
2. Manually delete app from eshr console [[link](https://console.meya.ai/admin/eshr/app/)]


### Simulate a Codeship build

```bash
# [!] app_id in meya.local.yaml first (if needed)
jet steps --tag master
```


### Set encrypted ENV variables for jet/Codeship

- download `meya-ai_google-rma.aes` [from Codeship](https://app.codeship.com/projects/2961c230-8159-0137-44ab-0ea6617cc10b/configure) into project directory
- rename the file: `mv meya-ai_google-rma.aes codeship.aes`
- `jet decrypt codeship-env.encrypted codeship-env` to decrypt
- add or edit the `codeship-env` file
- run `jet encrypt codeship-env codeship-env.encrypted`
- it's safe commit `codeship-env.encrypted` into git

[Learn more](https://documentation.codeship.com/pro/builds-and-configuration/environment-variables/)

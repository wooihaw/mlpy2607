# Course Website & Traffic Infographic Setup

This guide explains how to publish the course landing page with **GitHub Pages** and enable the live "Course reach" infographic that shows how many times the repository has been cloned and downloaded.

The landing page lives in the [`docs/`](docs) folder. Once GitHub Pages is enabled it will be available at:

```
https://wooihaw.github.io/mlpy2607/
```

## 1. Enable GitHub Pages

1. Go to **Settings > Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Choose branch **main** and folder **/docs**, then click **Save**.
4. Wait a minute for the first build; the URL above will then serve the page.

The page works on its own. The clone/download infographic will simply show placeholders until you complete the steps below.

## 2. How the infographic gets its data

GitHub's traffic statistics (clones and downloads) are private and only cover the **last 14 days**, so they cannot be embedded directly on a static page. Instead, a scheduled GitHub Action ([`.github/workflows/traffic.yml`](.github/workflows/traffic.yml)) reads the traffic data and accumulates it into [`docs/traffic.json`](docs/traffic.json), building a running total over time. The landing page reads that file.

The Action needs a **Personal Access Token (PAT)** with permission to read the repository's traffic, because the default `GITHUB_TOKEN` cannot access the traffic API.

## 3. Create a Personal Access Token (PAT)

A PAT is like a scoped password that the Action uses to read your traffic data. It is created in your GitHub **account** settings, not in the repository.

**Get to the token page:** click your profile photo (top-right) > **Settings** > scroll to **Developer settings** (bottom of the left sidebar) > **Personal access tokens**.

### Option A — Fine-grained token (recommended)

More secure, because it can be locked to this single repository.

1. Click **Fine-grained tokens** > **Generate new token**.
2. **Token name:** e.g. `mlpy2607-traffic`.
3. **Expiration:** choose a duration (e.g. 90 days or 1 year). You will need to regenerate it when it expires.
4. **Repository access:** select **Only select repositories**, then choose **wooihaw/mlpy2607**.
5. **Permissions:** expand **Repository permissions**, find **Administration**, and set it to **Read-only**. (This is what unlocks the traffic data.) Leave everything else at default.
6. Click **Generate token**, then **copy the token immediately** — GitHub shows it only once.

### Option B — Classic token

Works identically but grants broader access.

1. Click **Tokens (classic)** > **Generate new token (classic)**.
2. Give it a name and expiration.
3. Tick the top-level **`repo`** checkbox.
4. Click **Generate token** and copy it.

## 4. Add the token as a repository secret

1. Go to the repository > **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. **Name:** `TRAFFIC_TOKEN` (must match exactly).
4. **Secret:** paste the token you copied.
5. Click **Add secret**.

## 5. Run the workflow

1. Go to the **Actions** tab.
2. Select **Collect repository traffic** in the left sidebar.
3. Click **Run workflow** to trigger it once. After that it runs automatically every day.

Within a minute or two the workflow updates `docs/traffic.json`, and the infographic on the page switches from placeholders to real numbers.

## Notes

- **Token expiry:** when the PAT expires the workflow will start failing until you generate a new token and update the `TRAFFIC_TOKEN` secret.
- **Accuracy:** clone counts are exact; unique-cloner counts are an approximation (daily uniques summed over time, since GitHub does not provide a long-term unique figure).
- **Downloads:** GitHub does not expose "Download ZIP" counts, so the download figure reflects downloads of published **release assets** only.

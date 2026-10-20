# Stained Glass Love Fountain ❤️

A small interactive romantic experience built with Python and Streamlit.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy free on Streamlit Community Cloud
1. Create a GitHub repository and upload `app.py` and `requirements.txt`.
2. Sign in to https://share.streamlit.io/ with GitHub.
3. Choose **Create app**, select your repository, branch, and `app.py`.
4. Deploy and share the generated public URL.

Edit the `messages` list in `app.py` to personalize the sequence before deploying.

## Personal photos
The four uploaded photos are included in `assets/` and displayed in a two-column gallery near the top of the experience. Keep the `assets` folder when uploading the project to GitHub. You can replace the images while keeping the same filenames, or update the paths in `app.py`.

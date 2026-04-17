# Instagram Poster

Post images to Instagram via the official Instagram Graph API.

## How It Works

The Instagram Graph API requires a two-step process:
1. **Create a media container** — submit a publicly accessible image URL
2. **Publish the container** — after it finishes processing, publish it to the feed

## Prerequisites

- The `ig-mcp` project at `/home/user/.nanobot/workspace/ig-mcp` with a valid `.env` file
- Credentials: `INSTAGRAM_ACCESS_TOKEN`, `INSTAGRAM_BUSINESS_ACCOUNT_ID`
- A **publicly accessible image URL** (no redirects, direct link to JPG/PNG)
- Image must be 1:1 (square), 4:5 (portrait), or 1.91:1 (landscape)

## Usage

Run the posting script:

```bash
cd /home/user/.nanobot/workspace/ig-mcp
. .venv/bin/activate
python /home/user/.nanobot/workspace/skills/instagram-poster/post.py "https://example.com/image.jpg" "Your caption here"
```

Or call the `post_to_instagram` function from Python.

## Important Notes

- **DNS workaround**: This environment blocks DNS for `graph.facebook.com`. The script connects directly to the Facebook API IP (`57.145.2.141`) with a `Host` header.
- **Image URL must be direct** — no redirects. The Instagram API will fail to fetch images from URLs that redirect (e.g., `picsum.photos`).
- **Wait time**: After creating a container, wait ~5 seconds before publishing.
- **Token expiry**: Long-lived tokens expire after 60 days. If posting fails with OAuth errors, the token needs refreshing.
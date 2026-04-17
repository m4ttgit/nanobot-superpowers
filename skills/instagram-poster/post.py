#!/usr/bin/env python3
"""Post an image to Instagram via the Instagram Graph API.

Usage: python post.py <image_url> [caption]
Example: python post.py "https://example.com/photo.jpg" "Hello from nanobot! 🐈"
"""
import httpx
import asyncio
import sys
import os

# Clear cached env vars
for k in list(os.environ.keys()):
    if 'INSTAGRAM' in k or 'FACEBOOK' in k:
        del os.environ[k]

from dotenv import load_dotenv
load_dotenv(override=True)

# DNS workaround: connect directly to Facebook API IP
GRAPH_API_IP = "57.145.2.141"

TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')
ACCOUNT_ID = os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID')


async def post_to_instagram(image_url: str, caption: str = "") -> dict:
    """Post an image to Instagram. Returns the result dict."""
    # Step 1: Create media container
    async with httpx.AsyncClient(verify=False) as client:
        r = await client.post(
            f'https://{GRAPH_API_IP}/v19.0/{ACCOUNT_ID}/media',
            params={
                'access_token': TOKEN,
                'image_url': image_url,
                'caption': caption,
            },
            headers={'Host': 'graph.facebook.com'}
        )
        result = r.json()
        if 'error' in result:
            return {'success': False, 'error': result['error']['message']}
        container_id = result['id']

    # Step 2: Wait for container to be ready
    await asyncio.sleep(5)

    # Step 3: Publish
    async with httpx.AsyncClient(verify=False) as client:
        r = await client.post(
            f'https://{GRAPH_API_IP}/v19.0/{ACCOUNT_ID}/media_publish',
            params={
                'access_token': TOKEN,
                'creation_id': container_id,
            },
            headers={'Host': 'graph.facebook.com'}
        )
        result = r.json()
        if 'id' in result:
            return {'success': True, 'media_id': result['id']}
        return {'success': False, 'error': result.get('error', {}).get('message', 'Unknown error')}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python post.py <image_url> [caption]")
        sys.exit(1)
    image_url = sys.argv[1]
    caption = sys.argv[2] if len(sys.argv) > 2 else ""
    result = asyncio.run(post_to_instagram(image_url, caption))
    if result['success']:
        print(f"✅ Posted! Media ID: {result['media_id']}")
    else:
        print(f"❌ Failed: {result['error']}")
        sys.exit(1)
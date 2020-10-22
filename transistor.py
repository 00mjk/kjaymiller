import os
import httpx
import typer
import slugify
from pathlib import Path


header = {'x-api-key': os.environ.get('transistorKey')}
app = typer.Typer()

@app.command()
def get_show_list():
    """Get a list of all the shows"""

    url = 'https://api.transistor.fm/v1/shows'
    r = httpx.get(url, headers=header)
    typer.echo([(x['id'], x['attributes']['title']) for x in r.json()['data']])

@app.command()
def get_latest_episode(directory: Path, show_id: int=799, episodes: int=1):
    """Fetch the Latest Episode and write a render-engine template to the output"""

    episodes_url = 'https://api.transistor.fm/v1/episodes/'
    params = {"show_id": show_id}
    r = httpx.get(episodes_url, headers=header, params=params)

    for episode in r.json()['data'][0:episodes]:
        episode_attrs = episode['attributes']
        title = episode_attrs['title']
        published_date = episode_attrs['published_at']
        summary = episode_attrs['summary']
        embed_url = episode_attrs['embed_html']

        content = f"""title: {title}
date: {published_date}
images: https://kjaymiller.s3-us-west-2.amazonaws.com/images/pit-logo-v5.jpg

{summary}
{embed_url}"""

        directory.joinpath(slugify(episode['title'])).with_suffix(".md")
        output.write_text(content)


if __name__ == "__main__":
    app()
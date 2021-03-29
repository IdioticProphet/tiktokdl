import argparse
from .tiktokdl import tiktokdl

def cli(url, output_path) -> None:
    video_content = tiktokdl(url)
    print("Saved to " + output_path)
    with open(output_path, "wb") as fd:
        fd.write(video_content)

def main():
    parser = argparse.ArgumentParser(
        description="Download MP4 versions of TikTok videos"
    )
    parser.add_argument(
        "url",
        help="Permalink URL of the TikTok, example: https://www.tiktok.com/@youneszarou/video/6877109293657689345",
    )
    parser.add_argument("-O", "--output-path", help="Output path for the video")
    args = parser.parse_args()

    if args.output_path:
        output_path = args.output_path
    else:
        url_parts = args.url.split("/")
        url_component = None
        while not url_component and url_parts:
            url_component = url_parts.pop()

        output_path = url_component + ".mp4"

    cli(args.url, output_path)


if __name__ == "__main__":
    main()
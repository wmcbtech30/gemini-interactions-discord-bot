import base64

import aiohttp

MAX_FILE_SIZE_BYTES = 20 * 1024 * 1024  # 20 MB


async def encode_file(aiohttp_session: aiohttp.ClientSession, attachment_url: str) -> str:
    async with aiohttp_session.get(attachment_url) as response:
        response.raise_for_status()
        if response.content_length and response.content_length > MAX_FILE_SIZE_BYTES:
            raise ValueError("File size exceeds the 20 MB limit")

        file_bytes = await response.read()
        if len(file_bytes) > MAX_FILE_SIZE_BYTES:
            raise ValueError("File size exceeds the 20 MB limit")

        return base64.b64encode(file_bytes).decode("utf-8")

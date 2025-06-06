import requests

shared_library_version = "1.9.1"
github_download_url = "https://github.com/bogdanfinn/tls-client/releases/download/v{}/{}"
github_repo_filenames = [
    # Windows
    f"tls-client-windows-32-{shared_library_version}.dll",
    f"tls-client-windows-64-{shared_library_version}.dll",
    # MacOS
    f"tls-client-darwin-arm64-{shared_library_version}.dylib",
    f"tls-client-darwin-amd64-{shared_library_version}.dylib",
    # Linux
    # f"tls-client-linux-alpine-amd64-{shared_library_version}.so", # Removed in 1.7.8
    f"tls-client-linux-ubuntu-amd64-{shared_library_version}.so",
    f"tls-client-linux-ubuntu-amd64-{shared_library_version}.so",
    f"tls-client-linux-arm64-{shared_library_version}.so"
]
dependency_filenames = [
    # Windows
    "tls-client-32.dll",
    "tls-client-64.dll",
    # MacOS
    "tls-client-arm64.dylib",
    "tls-client-x86.dylib",
    # Linux
    "tls-client-amd64.so",
    "tls-client-x86.so",
    "tls-client-arm64.so"
]

for github_filename, dependency_filename in zip(github_repo_filenames, dependency_filenames):
    filepath = f"../async_tls_client/dependencies/{dependency_filename}"
    url = github_download_url.format(shared_library_version, github_filename)
    print(f'Downloading {url}...')
    response = requests.get(url=url)
    if not response.ok:
        print(f'Failed to fetch ({response.status_code})')
    print(f'Writing to "{filepath}"...')
    with open(filepath, "wb") as f:
        f.write(response.content)
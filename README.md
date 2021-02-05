# spotify-song-credits
Webdriver Python code to scrape song credits from web player  
since those are unfortunately not yet available via API  
https://community.spotify.com/t5/Spotify-for-Developers/Getting-credits-on-a-track/td-p/4950934  
https://github.com/spotify/web-api/issues/779

## Usage
```
./spotify-song-credits.py --help
usage: spotify-song-credits.py [-h] [--browser-headless BROWSER_HEADLESS] [--browser-fullscreen BROWSER_FULLSCREEN] [--browser-enable-drm BROWSER_DRM] [--browser-close BROWSER_CLOSE] [--target TARGET] --url URL
                               [--url-payload URL_PAYLOAD] --login-user LOGIN_USER --login-pw LOGIN_PW [--selector-user SELECTOR_USER] [--selector-pw SELECTOR_PW] [--selector-submit SELECTOR_SUBMIT]
                               [--selector-value-user SELECTOR_VALUE_USER] [--selector-value-pw SELECTOR_VALUE_PW] [--selector-value-submit SELECTOR_VALUE_SUBMIT]

If an arg is specified in more than one place, then commandline values override environment variables which override defaults.

optional arguments:
  -h, --help            show this help message and exit
  --browser-headless BROWSER_HEADLESS
                        Run the browser in headless mode [env var: BROWSER_HEADLESS]
  --browser-fullscreen BROWSER_FULLSCREEN
                        Run browser in fullscreen mode [env var: BROWSER_FULLSCREEN]
  --browser-enable-drm BROWSER_DRM
                        Download and enable DRM binaries [env var: BROWSER_DRM]
  --browser-close BROWSER_CLOSE
                        Close browser after successful run [env var: BROWSER_CLOSE]
  --target TARGET       The application to log into [env var: TARGET]
  --url URL             URL to open in browser startup [env var: URL]
  --url-payload URL_PAYLOAD
                        URL to open after successful login [env var: URL_PAYLOAD]
  --login-user LOGIN_USER
                        Username to use for web-app login [env var: LOGIN_USER]
  --login-pw LOGIN_PW   Password to user for web-app login [env var: LOGIN_PW]
  --selector-user SELECTOR_USER
                        The method to select the user input element [env var: SELECTOR_USER]
  --selector-pw SELECTOR_PW
                        The method to select the user input element [env var: SELECTOR_PW]
  --selector-submit SELECTOR_SUBMIT
                        The method to select the submit button element [env var: SELECTOR_SUBMIT]
  --selector-value-user SELECTOR_VALUE_USER
                        The value for the user element selection [env var: SELECTOR_VALUE_USER]
  --selector-value-pw SELECTOR_VALUE_PW
                        The value for the pw element selection [env var: SELECTOR_VALUE_PW]
  --selector-value-submit SELECTOR_VALUE_SUBMIT
                        The value for the submit element selection [env var: SELECTOR_VALUE_SUBMIT]
```
### Using command line arguments
```
$ ./spotify-song-credits.py --login-user foo \
                            --login-pw c3VwZXJTZWNyZXRQYXNzd3JvZAo= \
                            --url_payload https://open.spotify.com/track/7kU5no0i1TK71zPI3IBUND \

```
### Using only environment variable
```
$ LOGIN_USER="foo" \
LOGIN_PW="foobarbaz=" \
URL="https://accounts.spotify.com/en/login" \
URL_PAYLOAD="https://open.spotify.com/track/7kU5no0i1TK71zPI3IBUND" \
BROWSER_DRM=1 \
./spotify-song-credits.py
```

## Environment Variables
- TARGET - The target
- BROWSER_DRM - Enable Browser DRM (needed)
- URL - The spotify URL (https://accounts.spotify.com/en/login)
- URL_PAYLOAD - The URL to open after successful login (optional)
- LOGIN_USER - The user to use for logging in
- LOGIN_PW - The base64 encoded password to use for logging in

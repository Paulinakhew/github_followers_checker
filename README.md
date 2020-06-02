# github_followers_checker

### Setup
1. Clone the repository

2. Create a [GitHub oAuth Token](https://docs.cachethq.io/docs/github-oauth-token#:~:text=Generate%20a%20new%20token,list%20of%20tokens%20from%20before.) that has the `user:follow` scope. That token is only available once so make sure to save it!

3. Create an `.env` file in the root of the repository that contains the following:
```
MY_TOKEN={{OAUTH_TOKEN_VALUE}}
```
That value is automatically read using `os` and `dotenv`

4. Run the file:
```bash
python3 github_script.py
```

### Explanation
The [GitHub Developers documentation](https://developer.github.com/v3/users/followers/) explains how to follow and unfollow people. I wanted to automate this process using python and the requests library. This project is just for fun, the number of followers I have doesn't matter to me :laughing:

### Additional Notes
For some reason, I've noticed that the displayed number of followers/following in the user overview doesn't change, even if you manually unfollow someone. To double-check, look at the outputted list of users after you run the script and see if you still follow them/they still follow you.

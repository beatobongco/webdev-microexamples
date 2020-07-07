## What happens when you tick "Remember me"?

Follow along with the code and comments [here](https://github.com/beatobongco/webdev-microexamples/blob/master/wm4-remember_me_cookie/microblog/app/routes.py#L20) to understand what happens.

### Cookie spoofing

You can copy the contents of the cookie and open a new incognito window. 

Use Chrome Developer Tools to create a new cookie called `remember_token`, pasting the contents of the cookie as its value.

Refresh the page. You are now logged in as your test user!

![cookie spoofing](https://raw.githubusercontent.com/beatobongco/webdev-microexamples/master/wm4-remember_me_cookie/cookie_spoof.png)

# bandwidth text to mail

turns out there's something better than [twilio](https://github.com/pew/twilio-sms-to-mail) for me.

quick n' dirty [bandwidth](https://www.bandwidth.com/) text (sms) to mail python app using postmark app

forwards all incoming text messages to your bandwidth phone number to a given email address

# 1. prep

1. get a [bandwidth.com](https://www.bandwidth.com/) account and get a phone number ($0.35/month)
2. get a [https://postmarkapp.com/](https://postmarkapp.com/) account, you'll get 25,000 credits for free. That's about... 25,000 emails.

# 2. config

* retrieve your PostmarkApp API key and add it to `application.py` as 
`token`
* change the `toAddress` and `fromAddress` parts in `applicaiton.py` to fit your needs

# 3. run it

It's 2017, so run it in a docker container:

```
docker build -t bw-sms2mail .
docker run -d -p5000:5000 --name bandwidth bw-sms2mail
```

per default the flask app will listen on port 5000, you can either change the port through docker or use a http reverse proxy like nginx or caddy
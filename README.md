# headnode notifier

Simple script for sending emails.

### Usage examples

```
usage: headnode_notifier [address] [OPTION]

Simple script for email notifications. Uses gmail by default.

positional arguments:
                    Recipient address

optional arguments:
  -h, --help        show this help message and exit
  -v, --version     show program's version number and exit
  --subject         Message subject
  --body            Message body
  --attach          Attachment
  --serv-addr       Server address. Default <smtp.gmail.com>
  --port            Server's port. Default: <587>
  --from-addr       Account address.
  --password-file   Read password from exeternal file. Prevents hard-coding
                    password anywhere in this script. IMPORTANT! Password is
                    stored as plain text! Do NOT use with your personal
                    account!
```

#### Let's assume you are using default account and you have password file in a proper place

You can specify the message subject, content and attach a file.

```
headnode_notifier.py recipient@domain.com --subject 'Important message' --body 'Hello there!' --attach ./some/file.zip
```

You can also send just blank message, only ```recipient@domain.com``` is truly obligatory if using default values for the rest.

You can specify server, port and else if you wish with ```--serv-addr smpt.provider.com --port 42 --from-addr my.address@provider.com```

#### Config handling
If an option is not specified in the CLI, it is read from the headnode_notifier.config file. It is meant to facilitate the usage by setting default values for:

1. Server address.
2. Port.
3. Mailbox address
4. /path/to/password_file


* Config content:

```
[server]
address = smtp.gmail.com
port = 587

[mailbox]
address =
password_file =
```


* Config location: **$HOME**


* Config name:

```
.headnode_notifier.config
```

#### Password handling

In order to avoid storing the password anywhere in the script, it is read from file. You can specify the path using ```--password-file /path/to/file``` or in the config file. Remember that the **password file is plain text** so use the script with caution.


#### Using gmail

Remember to allow *less secure apps* to connect if using gmail. You can set it on [google account security page](https://myaccount.google.com/security)

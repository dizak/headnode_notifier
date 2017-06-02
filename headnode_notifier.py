#! /usr/bin/env python


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import argparse
import sys
import ConfigParser


__author__ = "Dariusz Izak"
__version__ = "1.1"


def read_passwd_file(pass_file):
    """Read password from external file and retrun as string. The file should
    contain just single line. Prevents hard-coding password anywhere in this
    script. IMPORTANT! Password is stored as plain text! Do NOT use with your
    personal account!"

    Args:
        pass_file (str): /path/to/pass_file
    """
    with open(pass_file) as fin:
        passwd = fin.read().strip()
    return passwd


def send_mail(to_addr,
              subj_msg,
              body_msg,
              attach_path,
              serv_addr,
              serv_port,
              from_addr,
              passwd):
    """Send an e-mail message using smtplib and email standard python libraries.
    IMPORTANT! Password is stored as plain text! Do NOT use with your personal
    account!

    Args:
        to_addr (str): Recipient address.
        subj_msg (str): Message subject.
        body_msg (str): Message body.
        serv_addr (str): Server's address. Default: <smtp.gmail.com>.
        serv_port (int): Server's port. Default: <587>.
        from_addr (str): Account address. Default: <headnode.notifiy@gmail.com>.
        passwd (str): Account password.
    """
    msg = MIMEMultipart()
    if attach_path is not None:
        with open(attach_path, "rb") as fin:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(fin.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",
                            "attachment; filename={0}".format(attach_path))
            msg.attach(part)
    else:
        pass
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subj_msg
    msg.attach(MIMEText(body_msg, "plain"))
    server = smtplib.SMTP(serv_addr, serv_port)
    server.starttls()
    server.login(from_addr, passwd)
    text_msg = msg.as_string()
    server.sendmail(from_addr, to_addr, text_msg)
    server.quit


def main():
    parser = argparse.ArgumentParser(prog="headnode notifier",
                                     usage="headnode_notifier [address] [OPTION]",
                                     description="Simple script for email\
                                                  notifications. Uses gmail\
                                                  by default.",
                                     version=__version__)
    parser.add_argument(metavar="",
                        action="store",
                        dest="to",
                        help="Recipient address")
    parser.add_argument("--subject",
                        metavar="",
                        action="store",
                        dest="subject",
                        default="",
                        help="Message subject")
    parser.add_argument("--body",
                        metavar="",
                        action="store",
                        dest="body",
                        default="",
                        help="Message body")
    parser.add_argument("--attach",
                        metavar="",
                        action="store",
                        dest="attach",
                        help="Attachment")
    parser.add_argument("--serv-addr",
                        metavar="",
                        action="store",
                        dest="serv_addr",
                        default=None,
                        help="Server address. Default <smtp.gmail.com>")
    parser.add_argument("--port",
                        metavar="",
                        action="store",
                        dest="port",
                        default=587,
                        help="Server's port. Default: <587>")
    parser.add_argument("--from-addr",
                        metavar="",
                        action="store",
                        dest="from_addr",
                        default=None,
                        help="Account address.\
                              Default: <headnode.notify@gmail.com>.")
    parser.add_argument("--password-file",
                        metavar="",
                        action="store",
                        dest="password_file",
                        default=None,
                        help="Read password from exeternal file. Prevents\
                              hard-coding password anywhere in this script.\
                              IMPORTANT! Password is stored as plain text!\
                              Do NOT use with your personal account! Default:\
                              <.bashrc/path/to/headnode_notifier/passwd.txt>")
    args = parser.parse_args()

    config = ConfigParser.SafeConfigParser()
    config.read(sys.argv[0].replace(sys.argv[0].split("/")[-1],
                "headnode_notifier.config"))
    conf_serv_addr = config.get("server", "address")
    conf_port = config.get("server", "port")
    conf_from_addr = config.get("mailbox", "address")
    conf_passwd = config.get("mailbox", "password_file")

    if args.password_file is None:
        passwd = conf_passwd
    else:
        passwd = args.password_file
    if args.serv_addr is not None:
        serv_addr = args.serv_addr
    else:
        serv_addr = conf_serv_addr
    if args.port is not None:
        port = args.port
    else:
        port = conf_port
    if args.from_addr is not None:
        from_addr = args.from_addr
    else:
        from_addr = conf_from_addr
    passwd_from_file = read_passwd_file(passwd)
    send_mail(to_addr=args.to,
              subj_msg=args.subject,
              body_msg=args.body,
              attach_path=args.attach,
              serv_addr=serv_addr,
              serv_port=port,
              from_addr=from_addr,
              passwd=passwd_from_file)


if __name__ == '__main__':
    main()

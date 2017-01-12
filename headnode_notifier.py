#! /usr/bin/env python


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import argparse
import sys


__author__ = "Dariusz Izak"
__vresion__ = "testing"


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
              serv_addr = "smtp.gmail.com",
              serv_port = 587,
              from_addr = "headnode.notify@gmail.com",
              passwd = "",):
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
    parser = argparse.ArgumentParser(prog = "headnode notifier",
                                     description = "Simple script for email\
                                                    notifications. Uses gmail.",
                                     version = "testing")
    parser.add_argument("--to",
                        metavar = "",
                        action = "store",
                        dest = "to",
                        help = "Recipient address")
    parser.add_argument("--subject",
                        metavar = "",
                        action = "store",
                        dest = "subject",
                        help = "Message subject")
    parser.add_argument("--body",
                        metavar = "",
                        action = "store",
                        dest = "body",
                        help = "Message body")
    parser.add_argument("--password-file",
                        metavar = "",
                        action = "store",
                        dest = "password_file",
                        default = None,
                        help = "Read password from exeternal file. Prevents\
                                hard-coding password anywhere in this script.\
                                IMPORTANT! Password is stored as plain text!\
                                Do NOT use with your personal account! Default:\
                                <.bashrc/path/to/headnode_notifier/passwd.txt>")
    args = parser.parse_args()

    if args.password_file is None:
        passwd = sys.argv[0].replace(sys.argv[0].split("/")[-1],
                                        "passwd.txt")

    else:
        passwd = args.password_file
    passwd_from_file = read_passwd_file(passwd)
    send_mail(args.to,
              args.subject,
              args.body,
              passwd = passwd_from_file)


if __name__ == '__main__':
    main()

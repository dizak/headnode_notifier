#! /usr/bin/env python

__author__ = "Dariusz Izak"
__vresion__ = "testing"

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import argparse


def send_mail(to_addr,
              subj_msg,
              body_msg,
              serv_addr = "smtp.gmail.com",
              serv_port = 587,
              from_addr = "headnode.notify@gmail.com",
              passwd = "oYCOXggW",):
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
                        help = "Recipient address.")


if __name__ == '__main__':
    main()

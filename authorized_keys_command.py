#!/usr/bin/env python

import boto3
import argparse

def get_authorized_keys(username):
    client = boto3.client('iam')

    UnsafeUserName = username
    UnsafeUserName = UnsafeUserName.replace('.plus.', '+')
    UnsafeUserName = UnsafeUserName.replace('.equal.', '=')
    UnsafeUserName = UnsafeUserName.replace('.comma.', ',')
    UnsafeUserName = UnsafeUserName.replace('.at.', '@')

    try:
        for key in client.list_ssh_public_keys(
            UserName=UnsafeUserName)['SSHPublicKeys']:
            if key['Status'] == 'Active':
                print client.get_ssh_public_key(
                    UserName=UnsafeUserName,
                    SSHPublicKeyId=key['SSHPublicKeyId'],
                    Encoding='SSH')['SSHPublicKey']['SSHPublicKeyBody']
    except:
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='authorized_keys_command')
    parser.add_argument('username', help='IAM User to retrieve SSH keys for')
    args = parser.parse_args()
    get_authorized_keys(args.username)

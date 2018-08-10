#!/usr/bin/env python

import os
import boto3
from pwd import getpwnam

def import_users():
    client = boto3.client('iam')

    for user in client.list_users()['Users']:
        SafeUserName = user['UserName']
        SafeUserName = SafeUserName.replace('+', '.plus.')
        SafeUserName = SafeUserName.replace('=', '.equal.')
        SafeUserName = SafeUserName.replace(',', '.comma.')
        SafeUserName = SafeUserName.replace('@', '.at.')

        try:
            if len(SafeUserName) < 32:
                try:
                    user = getpwnam(SafeUserName)
                except:
                    returnCode = os.system('/usr/sbin/useradd {}'.format(SafeUserName))
            else:
                print 'Can not import IAM user {}. User name is longer than 32 characters.'.format(SafeUserName)
        except:
            pass

if __name__ == '__main__':
    import_users()

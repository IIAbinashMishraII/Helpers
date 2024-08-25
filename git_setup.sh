# To get the full path in terminal - pwd 
cd /Users/abinashmishra/No.\ 2/DSA\ and\ others/codes/Helpers

commit_message="Automated commit on $(date '+%Y-%m-%d at %H:%M'): $(git diff --stat HEAD~1..HEAD | tail -1)"

/usr/bin/git pull
/usr/bin/git add .
/usr/bin/git commit -m "$commit_message"
/usr/bin/git push origin main


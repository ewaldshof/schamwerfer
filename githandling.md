Git Handling local environment

git config --list
git config --global user.name "<Full Name>" 
git config --global user.email <email>
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.show-graph "log --graph --pretty=format:'%h - %d %s %cr' --abbrev-commit --date=relative"
git config --global alias.alias "!git config --list | grep 'alias\.' | sed 's/alias\.\([^=]*\)=\(.*\)/\1\	 => \2/' | sort"
git config --global push.followTags true

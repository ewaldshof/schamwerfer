
    # Git Handling local environment

    git config --list
    git config --global user.name "<Full Name>" 
    git config --global user.email <email>
    git config --global core.editor vi
    git config --global push.default simple
    git config --global alias.s 'status'
    git config --global alias.au '!git add -u . && git status'
    git config --global alias.aa '!git add . && git add -u . && git status'
    git config --global alias.co 'checkout'
    git config --global alias.c 'commit'
    git config --global alias.cm 'commit -m'
    git config --global alias.ca 'commit --amend'
    git config --global alias.ac '!git add . && git commit'
    git config --global alias.acm '!git add . && git commit -m'
    git config --global alias.l "log --graph --all --pretty=format:'%C(yellow)%h%C(cyan)%d%Creset %s %C(white)- %an, %ar%Creset'"
    git config --global alias.ll 'log --stat --abbrev-commit'
    git config --global alias.lg "log --color --graph --pretty=format:'%C(bold white)%h%Creset -%C(bold green)%d%Creset %s %C(bold green)(%cr)%Creset %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"
    git config --global alias.llg "log --color --graph --pretty=format:'%C(bold white)%H %d%Creset%n%s%n%+b%C(bold blue)%an <%ae>%Creset %C(bold green)%cr (%ci)' --abbrev-commit"
    git config --global alias.d 'diff'
    git config --global alias.master 'checkout master'
    git config --global alias.conf 'config --list'
    git config --global alias.alias "!git config --list | grep 'alias\\.' | sed 's/alias\\.\\([^=]*\\)=\\(.*\\)/\\1\\    => \\2/' | sort"

cd $HOME/$1
git pull
git add .
git commit -m $(date +%D)
git push
